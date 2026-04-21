'use client'

// Catalyst-aesthetic dashboard layout template.
// Composes SidebarLayout + StackedLayout primitives from ./components.
// Clean-room; not an extraction from the paid Catalyst package.

import { SidebarLayout } from '../components/sidebar-layout'
import { Sidebar } from '../components/sidebar'
import { Navbar } from '../components/navbar'
import { Heading } from '../components/heading'

export default function DashboardTemplate() {
  return (
    <SidebarLayout
      sidebar={
        <Sidebar>
          <nav className="flex flex-col gap-1 text-sm">
            <a className="rounded-md bg-zinc-100 px-3 py-2 font-medium text-zinc-900 dark:bg-zinc-800 dark:text-white">Dashboard</a>
            <a className="rounded-md px-3 py-2 text-zinc-700 hover:bg-zinc-50 dark:text-zinc-300 dark:hover:bg-zinc-800">Inventory</a>
            <a className="rounded-md px-3 py-2 text-zinc-700 hover:bg-zinc-50 dark:text-zinc-300 dark:hover:bg-zinc-800">Sourcing</a>
            <a className="rounded-md px-3 py-2 text-zinc-700 hover:bg-zinc-50 dark:text-zinc-300 dark:hover:bg-zinc-800">Reports</a>
          </nav>
        </Sidebar>
      }
      navbar={<Navbar><div className="text-sm font-semibold">Clawmachine</div></Navbar>}
    >
      <Heading>Dashboard</Heading>
      <dl className="mt-6 grid grid-cols-1 gap-4 sm:grid-cols-4">
        <div className="rounded-lg bg-white p-5 ring-1 ring-zinc-950/5 dark:bg-zinc-900 dark:ring-white/10">
          <dt className="text-sm text-zinc-500">GMV</dt>
          <dd className="mt-1 text-2xl font-semibold">£42,187</dd>
        </div>
        <div className="rounded-lg bg-white p-5 ring-1 ring-zinc-950/5 dark:bg-zinc-900 dark:ring-white/10">
          <dt className="text-sm text-zinc-500">Margin</dt>
          <dd className="mt-1 text-2xl font-semibold">38.2%</dd>
        </div>
        <div className="rounded-lg bg-white p-5 ring-1 ring-zinc-950/5 dark:bg-zinc-900 dark:ring-white/10">
          <dt className="text-sm text-zinc-500">In-stock</dt>
          <dd className="mt-1 text-2xl font-semibold">147</dd>
        </div>
        <div className="rounded-lg bg-white p-5 ring-1 ring-zinc-950/5 dark:bg-zinc-900 dark:ring-white/10">
          <dt className="text-sm text-zinc-500">Cash cycle</dt>
          <dd className="mt-1 text-2xl font-semibold">21d</dd>
        </div>
      </dl>
    </SidebarLayout>
  )
}
