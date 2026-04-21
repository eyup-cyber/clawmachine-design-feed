import SwiftUI

public enum Spacing {
    public static let xs:   CGFloat = 4
    public static let sm:   CGFloat = 8
    public static let md:   CGFloat = 12
    public static let lg:   CGFloat = 16
    public static let xl:   CGFloat = 24
    public static let xxl:  CGFloat = 32
}

public enum Radius {
    public static let none: CGFloat = 0
    public static let sm:   CGFloat = 2
    public static let md:   CGFloat = 4   // max for this app
}

/// macOS 9 bevel border widths (from HIG: small/medium/large)
public enum BevelWidth {
    public static let sm:  CGFloat = 2   // subtle raised — default for panels
    public static let md:  CGFloat = 3   // standard — buttons, interactive controls
    public static let lg:  CGFloat = 4   // heavy raised — emphasis, group boxes
}
