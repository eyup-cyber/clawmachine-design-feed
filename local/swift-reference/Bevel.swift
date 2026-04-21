import SwiftUI

/// Derives bevel highlight and shadow colours from a given accent.
/// macOS 9 raised panels use a bright top-left edge and dark bottom-right edge.
/// NO gradients — these are solid colours for 1-2px border edges.
public struct Bevel: Sendable {
    public let highlight: Color
    public let shadow: Color

    /// Create a bevel pair from an accent colour.
    /// Per Mac OS 9 HIG: highlight = 20-30% white, shadow = 30-40% black.
    /// With an accent, the highlight is tinted by the accent colour.
    public init(accent: Color) {
        // bright top-left edge — accent-tinted highlight
        self.highlight = accent.opacity(0.35)
        // dark bottom-right edge
        self.shadow = Color.black.opacity(0.45)
    }

    /// Default bevel for panels without a page accent — neutral light/dark.
    /// Per Mac OS 9 platinum appearance: white highlight, black shadow.
    public static let neutral = Bevel(
        highlight: Color.white.opacity(0.22),
        shadow: Color.black.opacity(0.38)
    )

    /// Private init for static presets.
    private init(highlight: Color, shadow: Color) {
        self.highlight = highlight
        self.shadow = shadow
    }
}
