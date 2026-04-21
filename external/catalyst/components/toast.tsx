'use client'

import clsx from 'clsx'
import type React from 'react'
import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react'

// Catalyst-style Toast (reimplementation from public docs pattern).
// Paired with Catalyst's zinc neutrals + white accents and same ring/shadow stack.

type Variant = 'default' | 'success' | 'warning' | 'danger'

type Toast = {
  id: string
  title: string
  description?: string
  variant?: Variant
  ttl?: number
}

type Ctx = {
  toasts: Toast[]
  push: (t: Omit<Toast, 'id'>) => void
  dismiss: (id: string) => void
}

const ToastContext = createContext<Ctx | null>(null)

export function ToastProvider({ children }: { children: React.ReactNode }) {
  const [toasts, setToasts] = useState<Toast[]>([])

  const dismiss = useCallback((id: string) => {
    setToasts((t) => t.filter((x) => x.id !== id))
  }, [])

  const push = useCallback(
    (t: Omit<Toast, 'id'>) => {
      const id = Math.random().toString(36).slice(2)
      const next: Toast = { ttl: 5000, variant: 'default', ...t, id }
      setToasts((curr) => [...curr, next])
      if (next.ttl) window.setTimeout(() => dismiss(id), next.ttl)
    },
    [dismiss]
  )

  const value = useMemo(() => ({ toasts, push, dismiss }), [toasts, push, dismiss])

  return (
    <ToastContext.Provider value={value}>
      {children}
      <div className="pointer-events-none fixed inset-x-0 bottom-0 z-50 flex flex-col items-end gap-3 p-6 sm:items-end">
        {toasts.map((t) => (
          <ToastItem key={t.id} toast={t} onDismiss={() => dismiss(t.id)} />
        ))}
      </div>
    </ToastContext.Provider>
  )
}

export function useToast() {
  const ctx = useContext(ToastContext)
  if (!ctx) throw new Error('useToast must be used inside <ToastProvider>')
  return ctx
}

const variantClasses: Record<Variant, string> = {
  default: 'bg-white ring-zinc-950/5 dark:bg-zinc-900 dark:ring-white/10',
  success: 'bg-emerald-50 ring-emerald-600/20 dark:bg-emerald-950/40 dark:ring-emerald-400/20',
  warning: 'bg-amber-50 ring-amber-600/20 dark:bg-amber-950/40 dark:ring-amber-400/20',
  danger: 'bg-red-50 ring-red-600/20 dark:bg-red-950/40 dark:ring-red-400/20',
}

function ToastItem({ toast, onDismiss }: { toast: Toast; onDismiss: () => void }) {
  useEffect(() => {
    // reserved for future animation stubs
  }, [])
  return (
    <div
      role="status"
      className={clsx(
        'pointer-events-auto w-full max-w-sm overflow-hidden rounded-lg p-4 shadow-lg ring-1 transition-all',
        variantClasses[toast.variant ?? 'default']
      )}
    >
      <div className="flex items-start gap-3">
        <div className="flex-1">
          <p className="text-sm font-medium text-zinc-900 dark:text-white">{toast.title}</p>
          {toast.description && <p className="mt-1 text-sm text-zinc-500 dark:text-zinc-400">{toast.description}</p>}
        </div>
        <button
          onClick={onDismiss}
          className="text-zinc-400 hover:text-zinc-600 dark:hover:text-zinc-200"
          aria-label="Dismiss"
        >
          ×
        </button>
      </div>
    </div>
  )
}
