import SwiftUI

// ALL text is either ALL CAPS or all lowercase. never mixed case.

public enum Typo {
    // app wordmark — Satoshi Bold, always lowercase (OFL swap from Matter-SemiBold 2026-04-20)
    public static let wordmark = Font.custom("Satoshi", size: 16).weight(.bold)

    // page titles — JetBrains Mono, ALL CAPS via .textCase(.uppercase)
    public static let pageTitle = Font.custom("JetBrains Mono", size: 22).weight(.bold)

    // section headings — ALL CAPS
    public static let heading = Font.custom("JetBrains Mono", size: 15).weight(.semibold)

    // body — lowercase
    public static let body = Font.custom("JetBrains Mono", size: 13)

    // data numbers
    public static let data = Font.custom("JetBrains Mono", size: 14).weight(.medium)
    public static let dataBig = Font.custom("JetBrains Mono", size: 32).weight(.bold)

    // labels — ALL CAPS
    public static let label = Font.custom("JetBrains Mono", size: 11).weight(.medium)

    // captions — lowercase
    public static let caption = Font.custom("JetBrains Mono", size: 11)
}
