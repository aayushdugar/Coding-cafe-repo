# Practice archive data dictionary

In the examples below, `records` means the list returned by `load_ytd(...)`.
The archive wraps each record in a file-specific key, so a path such as
`record["tweet"]["created_at"]` starts from one item in that list.

| File | What a record contains and useful paths |
| --- | --- |
| `account.js` | One account object at `record["account"]`. Useful fields include `email`, `username`, `accountId`, `accountDisplayName`, `createdVia`, and `createdAt`. |
| `tweets.js` | A tweet at `record["tweet"]`. Useful fields include `created_at`, `full_text`, `id_str`, `source`, `favorite_count`, `retweet_count`, `entities`, and `edit_info`. `created_at` uses a Twitter-style date string; this record does not include the author's profile object. |
| `like.js` | A liked-tweet entry at `record["like"]`, with `tweetId`, `fullText`, and `expandedUrl`. The archive does not say when the like was made or identify the tweet's author in this entry. |
| `follower.js` / `following.js` | An account at `record["follower"]` or `record["following"]`, with `accountId` and `userLink`. These entries have no follow date. |
| `direct-messages.js` | A conversation at `record["dmConversation"]`; messages are in `["messages"]`. Each message is wrapped in `["messageCreate"]`, with fields such as `senderId`, `recipientId`, `id`, `createdAt`, and `text`. A message may also include `urls`, `mediaUrls`, or `reactions`. |
| `ad-engagements.js` | Engagements are in `record["ad"]["adsUserData"]["adEngagements"]["engagements"]`. Each entry has `impressionAttributes` (for example, `deviceInfo`, `promotedTweetInfo`, `advertiserInfo`, and `impressionTime`) and an `engagementAttributes` list (engagement type and time). |
| `personalization.js` | Inferences are under `record["p13nData"]`: `demographics` (including `languages` and `genderInfo`), `interests` (including `interests`, `partnerInterests`, advertiser audiences, and `shows`), `locationHistory`, and `inferredAgeInfo` (including `age` and `birthDate`). Some values may be inferred. |
| `ad-mobile-conversions-attributed.js` | Conversion entries are in `record["ad"]["adsUserData"]["attributedMobileAppConversions"]["conversions"]`. Fields include `attributedConversionType`, `mobilePlatform`, `conversionEvent`, `applicationName`, `conversionValue`, and `conversionTime`. |
| `ad-mobile-conversions-unattributed.js` | Conversion entries are in `record["ad"]["adsUserData"]["unattributedMobileAppConversions"]["conversions"]`. Fields include `mobilePlatform`, `conversionEvent`, `applicationName`, `conversionValue`, and `conversionTime`; there is no `attributedConversionType` in the practice records. |

Dates have several formats: account and message dates use ISO 8601 strings ending
in `Z`; tweet dates look like `Sat May 18 14:26:29 +0000 2024`; ad conversion
and engagement times look like `2024-06-16 16:18:25` and have no timezone suffix.
The archive keeps identifiers such as `accountId` and `tweetId` as strings.
