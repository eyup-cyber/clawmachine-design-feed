import SwiftUI

/// 16x16 pixel grid icon — each row is a UInt16 bitmask (bit 15 = leftmost pixel).
public struct PixelIcon: Shape {
    private let rows: [UInt16]

    public init(rows: [UInt16]) {
        self.rows = rows
    }

    public func path(in rect: CGRect) -> Path {
        var path = Path()
        let unitW = rect.width / 16
        let unitH = rect.height / CGFloat(rows.count)

        for (r, mask) in rows.enumerated() {
            for c in 0..<16 {
                if mask & (1 << (15 - c)) != 0 {
                    path.addRect(CGRect(
                        x: CGFloat(c) * unitW,
                        y: CGFloat(r) * unitH,
                        width: unitW,
                        height: unitH
                    ))
                }
            }
        }
        return path
    }
}

// 16x16 sidebar glyphs. Heavy strokes, legible at 16px without anti-alias smudge.

public enum SidebarIcons {

    /// dashboard — four panels in a 2x2 grid
    public static let dashboard = PixelIcon(rows: [
        0b0000000000000000,
        0b0000000000000000,
        0b0001111001111000,
        0b0001111001111000,
        0b0001111001111000,
        0b0001111001111000,
        0b0001111001111000,
        0b0000000000000000,
        0b0000000000000000,
        0b0001111001111000,
        0b0001111001111000,
        0b0001111001111000,
        0b0001111001111000,
        0b0001111001111000,
        0b0000000000000000,
        0b0000000000000000,
    ])

    /// live feed — chunky lightning bolt
    public static let liveFeed = PixelIcon(rows: [
        0b0000000000000000,
        0b0000000000000000,
        0b0000000111100000,
        0b0000001111000000,
        0b0000011110000000,
        0b0000111100000000,
        0b0001111111110000,
        0b0000000011110000,
        0b0000000111100000,
        0b0000001111000000,
        0b0000011110000000,
        0b0000111100000000,
        0b0001111000000000,
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000000000,
    ])

    /// inventory — closed package box with lid
    public static let inventory = PixelIcon(rows: [
        0b0000000000000000,
        0b0000000000000000,
        0b0001111111111000,
        0b0001000000001000,
        0b0011111111111100,
        0b0011000000001100,
        0b0011000000001100,
        0b0011000000001100,
        0b0011000110001100,
        0b0011000110001100,
        0b0011000000001100,
        0b0011000000001100,
        0b0011000000001100,
        0b0011111111111100,
        0b0000000000000000,
        0b0000000000000000,
    ])

    /// analytics — 3 ascending bars on a baseline
    public static let analytics = PixelIcon(rows: [
        0b0000000000000000,
        0b0000000000000000,
        0b0000000000001110,
        0b0000000000001110,
        0b0000000000001110,
        0b0000000000001110,
        0b0000000000001110,
        0b0000000111001110,
        0b0000000111001110,
        0b0000000111001110,
        0b0011100111001110,
        0b0011100111001110,
        0b0011100111001110,
        0b0011100111001110,
        0b0111111111111110,
        0b0000000000000000,
    ])

    /// brain — filled lightbulb with screw base
    public static let brain = PixelIcon(rows: [
        0b0000000000000000,
        0b0000000000000000,
        0b0000111111000000,
        0b0001111111100000,
        0b0011111111110000,
        0b0011111111110000,
        0b0011111111110000,
        0b0011111111110000,
        0b0001111111100000,
        0b0000111111000000,
        0b0000011110000000,
        0b0000111111000000,
        0b0000111111000000,
        0b0000011110000000,
        0b0000000000000000,
        0b0000000000000000,
    ])

    /// mesh — 3 connected nodes, triangle topology
    public static let mesh = PixelIcon(rows: [
        0b0000000000000000,
        0b0000000000000000,
        0b0000001111000000,
        0b0000001111000000,
        0b0000011001100000,
        0b0000110000110000,
        0b0001100000011000,
        0b0011000000001100,
        0b0000000000000000,
        0b0000000000000000,
        0b1111000000001111,
        0b1111000000001111,
        0b1111000000001111,
        0b1111000000001111,
        0b0000000000000000,
        0b0000000000000000,
    ])

    /// settings — gear with 4 teeth
    public static let settings = PixelIcon(rows: [
        0b0000000000000000,
        0b0000000110000000,
        0b0001100110011000,
        0b0001110000111000,
        0b0011111111111100,
        0b0011110000111100,
        0b0111100000011110,
        0b0111100000011110,
        0b0111100000011110,
        0b0111100000011110,
        0b0011110000111100,
        0b0011111111111100,
        0b0001110000111000,
        0b0001100110011000,
        0b0000000110000000,
        0b0000000000000000,
    ])
}
