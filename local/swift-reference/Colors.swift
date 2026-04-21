import SwiftUI

// Per-page palettes — 2026-04-20 rewrite using operator-authored palettes from
// `.triage/chromatic-schemes.json` (62 schemes from clawmachine-codex/chromatic-lab.html).
//
// Each page carries a DIFFERENT authored palette. Voids + accents are the
// authored hex values, not hand-rolled. Previous hand-picked hex stacks read
// drab; this round pulls straight from the lab schemes that were designed to
// look alive at full-screen.
//
// Mapping:
//   dashboard   — TEKKI SHOCK      (indigo void, hot-pink accent)
//   liveFeed    — alias to dashboard
//   inventory   — BURNT CIRCUIT    (warm-black void, burnt orange accent)
//   analytics   — PHOSPHOR BURN    (olive-black void, neon-lime accent)
//   brain       — SIGNAL NOIR      (inkwell void, magenta accent)
//   mesh        — DEEP CURRENT     (teal-black void, cyan-green accent)
//   settings    — CHROMATIC FORGE  (graphite void, orange-red accent)
//   onboarding  — SOLAR FLARE      (brown-black void, solar orange accent)

public enum PageAccent {
    public static let dashboard  = Color(hex: 0xFF0066)  // TEKKI SHOCK   pg.dashboard
    public static let liveFeed   = Color(hex: 0xFF0066)
    public static let inventory  = Color(hex: 0xE87430)  // BURNT CIRCUIT pg.inventory (p)
    public static let analytics  = Color(hex: 0x39FF14)  // PHOSPHOR BURN p (neon lime)
    public static let brain      = Color(hex: 0xD946EF)  // SIGNAL NOIR   pg.brain (magenta)
    public static let mesh       = Color(hex: 0x00E5A0)  // DEEP CURRENT  p (cyan-green)
    public static let settings   = Color(hex: 0xFF5530)  // CHROMATIC FORGE p (orange-red)
    public static let onboarding = Color(hex: 0xFF9B17)  // SOLAR FLARE   p (solar orange)
}

public enum TextColor {
    public static let primary     = Color(hex: 0xFFFFFF)
    public static let body        = Color(hex: 0xD6D6E8)
    public static let muted       = Color(hex: 0x8A8AA8)
    public static let ghost       = Color(hex: 0x5C5C7A)
    public static let darkPrimary = Color(hex: 0x05000A)
    public static let darkMuted   = Color(hex: 0x2A0040)
}

public enum Surface {
    public static let backdrop = Color(hex: 0x050014)
    @available(*, deprecated, renamed: "backdrop")
    // swiftlint:disable:next identifier_name
    public static let void_ = backdrop
    public static let base   = Color(hex: 0x0A001C)
    public static let card   = Color(hex: 0x140033)
    public static let raised = Color(hex: 0x1A0040)
    public static let bright = Color(hex: 0x250059)
}

public enum Brand {
    public static let teal   = Color(hex: 0x00E5A0)  // DEEP CURRENT p — live/connected
    public static let purple = Color(hex: 0xA855F7)  // VELVET TERMINAL pg.brain — vivid violet
    public static let coral  = Color(hex: 0xFF2D55)  // SIGNAL NOIR p — loss/alert
    public static let neon   = Color(hex: 0xBFFF00)  // TEKKI SHOCK p — acid lime
}

public enum Status {
    public static let profit = Color(hex: 0x00E5A0)  // DEEP CURRENT p — positive
    public static let loss   = Color(hex: 0xFF2D55)  // SIGNAL NOIR p — negative
    public static let gold   = Color(hex: 0xFFD23D)  // SOLAR FLARE pg.onboarding — amber
    public static let alert  = Color(hex: 0xFF8C42)  // SIGNAL NOIR pg.onboarding — warn
}

public enum PlatformColor {
    public static func color(for platform: String) -> Color {
        switch platform.lowercased() {
        case "ebay":       return Color(hex: 0xFF2D55)  // magenta-coral
        case "cex":        return Color(hex: 0xFF8C42)  // warn orange
        case "facebook":   return Color(hex: 0x3B82F6)  // electric blue
        case "gumtree":    return Color(hex: 0x39FF14)  // signal lime
        case "shpock":     return Color(hex: 0xFF0080)  // hot pink
        case "preloved":   return Color(hex: 0xA855F7)  // violet
        case "backmarket": return Color(hex: 0x00E5FF)  // cyan
        default:           return TextColor.muted
        }
    }
}

// MARK: - page themes
//
// Each page uses one operator-authored palette from the codex chromatic lab.
// 5-tier surface stack per page: {background, panel, panelAlt, chrome, detail}
// plus an accent + complement. Backgrounds are the authored `void`; panel/etc
// are hand-picked tints of the void toward the accent, keeping ≥ 0x10 per
// channel spacing so bevels read. All dark-only — light mode deferred.

public struct PageTheme: Sendable {
    public let backgroundTint: Color
    public let panelFill: Color
    public let panelAltFill: Color
    public let chromeFill: Color
    public let detailFill: Color
    public let panelBorder: Color
    public let textHighlight: Color
    public let statColour: Color
    public let complement: Color

    public init(
        background: Color,
        panel: Color,
        panelAlt: Color,
        chrome: Color,
        detail: Color,
        border: Color,
        accent: Color,
        complement: Color
    ) {
        self.backgroundTint = background
        self.panelFill = panel
        self.panelAltFill = panelAlt
        self.chromeFill = chrome
        self.detailFill = detail
        self.panelBorder = border
        self.textHighlight = accent
        self.statColour = accent
        self.complement = complement
    }

    // DASHBOARD — TEKKI SHOCK  (indigo void + hot-pink accent, lime complement)
    public static let dashboard = PageTheme(
        background: Color(hex: 0x0A0A2E),
        panel:      Color(hex: 0x14143A),
        panelAlt:   Color(hex: 0x1E1E4A),
        chrome:     Color(hex: 0x2A2A5E),
        detail:     Color(hex: 0x05051E),
        border: PageAccent.dashboard,
        accent: PageAccent.dashboard,
        complement: Color(hex: 0xBFFF00)
    )

    public static let liveFeed = dashboard

    // INVENTORY — BURNT CIRCUIT  (warm-black + burnt orange, teal-green complement)
    public static let inventory = PageTheme(
        background: Color(hex: 0x1C120A),
        panel:      Color(hex: 0x2C1E14),
        panelAlt:   Color(hex: 0x3C2A1E),
        chrome:     Color(hex: 0x4C382A),
        detail:     Color(hex: 0x100805),
        border: PageAccent.inventory,
        accent: PageAccent.inventory,
        complement: Color(hex: 0x30C8B0)
    )

    // ANALYTICS — PHOSPHOR BURN  (olive-black + neon-lime, cyan complement)
    public static let analytics = PageTheme(
        background: Color(hex: 0x0A1A0A),
        panel:      Color(hex: 0x142A14),
        panelAlt:   Color(hex: 0x1E3A1E),
        chrome:     Color(hex: 0x2A4A2A),
        detail:     Color(hex: 0x051405),
        border: PageAccent.analytics,
        accent: PageAccent.analytics,
        complement: Color(hex: 0xFF1744)
    )

    // BRAIN — SIGNAL NOIR  (inkwell + magenta accent, mint complement)
    public static let brain = PageTheme(
        background: Color(hex: 0x1A0A1A),
        panel:      Color(hex: 0x2A1424),
        panelAlt:   Color(hex: 0x3A1E30),
        chrome:     Color(hex: 0x4A2A3C),
        detail:     Color(hex: 0x0F050F),
        border: PageAccent.brain,
        accent: PageAccent.brain,
        complement: Color(hex: 0x00D4AA)
    )

    // MESH — DEEP CURRENT  (teal-black + cyan-green, coral complement)
    public static let mesh = PageTheme(
        background: Color(hex: 0x062018),
        panel:      Color(hex: 0x0A3024),
        panelAlt:   Color(hex: 0x104030),
        chrome:     Color(hex: 0x165040),
        detail:     Color(hex: 0x03100C),
        border: PageAccent.mesh,
        accent: PageAccent.mesh,
        complement: Color(hex: 0xFF5C8A)
    )

    // SETTINGS — CHROMATIC FORGE  (graphite + orange-red, teal complement)
    public static let settings = PageTheme(
        background: Color(hex: 0x1A1A1E),
        panel:      Color(hex: 0x2A2A30),
        panelAlt:   Color(hex: 0x3A3A42),
        chrome:     Color(hex: 0x4A4A54),
        detail:     Color(hex: 0x0F0F12),
        border: PageAccent.settings,
        accent: PageAccent.settings,
        complement: Color(hex: 0x20CCAA)
    )

    // ONBOARDING — SOLAR FLARE  (brown-black + solar orange, mint complement)
    public static let onboarding = PageTheme(
        background: Color(hex: 0x1A150A),
        panel:      Color(hex: 0x2A2414),
        panelAlt:   Color(hex: 0x3A321E),
        chrome:     Color(hex: 0x4A402A),
        detail:     Color(hex: 0x100A05),
        border: PageAccent.onboarding,
        accent: PageAccent.onboarding,
        complement: Color(hex: 0x17D4A8)
    )
}

extension Color {
    public init(hex: UInt, alpha: Double = 1.0) {
        self.init(
            .sRGB,
            red: Double((hex >> 16) & 0xFF) / 255.0,
            green: Double((hex >> 8) & 0xFF) / 255.0,
            blue: Double(hex & 0xFF) / 255.0,
            opacity: alpha
        )
    }
}
