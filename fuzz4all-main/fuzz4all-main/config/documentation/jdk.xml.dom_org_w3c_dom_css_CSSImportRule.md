# Interface CSSImportRule

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSSImportRule.html`

### Class Description

```java
public interface
CSSImportRule

extends
CSSRule
```

The

CSSImportRule

interface represents a @import rule within
a CSS style sheet. The

@import

rule is used to import style
rules from other style sheets.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**All Superinterfaces:** CSSRule

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getHref()

The location of the style sheet to be imported. The attribute will not
contain the

"url(...)"

specifier around the URI.

---

#### MediaList
getMedia()

A list of media types for which this style sheet may be used.

---

#### CSSStyleSheet
getStyleSheet()

The style sheet referred to by this rule, if it has been loaded. The
value of this attribute is

null

if the style sheet has
not yet been loaded or if it will not be loaded (e.g. if the style
sheet is for a media type not supported by the user agent).

---

### Additional Sections

#### Interface CSSImportRule

**All Superinterfaces:** CSSRule

```java
public interface
CSSImportRule

extends
CSSRule
```

The

CSSImportRule

interface represents a @import rule within
a CSS style sheet. The

@import

rule is used to import style
rules from other style sheets.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSSImportRule

extends

CSSRule

The

CSSImportRule

interface represents a @import rule within
a CSS style sheet. The

@import

rule is used to import style
rules from other style sheets.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface org.w3c.dom.css.

CSSRule

CHARSET_RULE

,

FONT_FACE_RULE

,

IMPORT_RULE

,

MEDIA_RULE

,

PAGE_RULE

,

STYLE_RULE

,

UNKNOWN_RULE

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getHref

()

The location of the style sheet to be imported.

MediaList

getMedia

()

A list of media types for which this style sheet may be used.

CSSStyleSheet

getStyleSheet

()

The style sheet referred to by this rule, if it has been loaded.

- Methods declared in interface org.w3c.dom.css.

CSSRule

getCssText

,

getParentRule

,

getParentStyleSheet

,

getType

,

setCssText

Field Summary

- Fields declared in interface org.w3c.dom.css.

CSSRule

CHARSET_RULE

,

FONT_FACE_RULE

,

IMPORT_RULE

,

MEDIA_RULE

,

PAGE_RULE

,

STYLE_RULE

,

UNKNOWN_RULE

---

#### Field Summary

Fields declared in interface org.w3c.dom.css.

CSSRule

CHARSET_RULE

,

FONT_FACE_RULE

,

IMPORT_RULE

,

MEDIA_RULE

,

PAGE_RULE

,

STYLE_RULE

,

UNKNOWN_RULE

---

#### Fields declared in interface org.w3c.dom.css. CSSRule

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getHref

()

The location of the style sheet to be imported.

MediaList

getMedia

()

A list of media types for which this style sheet may be used.

CSSStyleSheet

getStyleSheet

()

The style sheet referred to by this rule, if it has been loaded.

- Methods declared in interface org.w3c.dom.css.

CSSRule

getCssText

,

getParentRule

,

getParentStyleSheet

,

getType

,

setCssText

---

#### Method Summary

The location of the style sheet to be imported.

A list of media types for which this style sheet may be used.

The style sheet referred to by this rule, if it has been loaded.

Methods declared in interface org.w3c.dom.css.

CSSRule

getCssText

,

getParentRule

,

getParentStyleSheet

,

getType

,

setCssText

---

#### Methods declared in interface org.w3c.dom.css. CSSRule

============ METHOD DETAIL ==========

- Method Detail

- getHref

```java
String
getHref()
```

The location of the style sheet to be imported. The attribute will not
contain the

"url(...)"

specifier around the URI.

- getMedia

```java
MediaList
getMedia()
```

A list of media types for which this style sheet may be used.

- getStyleSheet

```java
CSSStyleSheet
getStyleSheet()
```

The style sheet referred to by this rule, if it has been loaded. The
value of this attribute is

null

if the style sheet has
not yet been loaded or if it will not be loaded (e.g. if the style
sheet is for a media type not supported by the user agent).

Method Detail

- getHref

```java
String
getHref()
```

The location of the style sheet to be imported. The attribute will not
contain the

"url(...)"

specifier around the URI.

- getMedia

```java
MediaList
getMedia()
```

A list of media types for which this style sheet may be used.

- getStyleSheet

```java
CSSStyleSheet
getStyleSheet()
```

The style sheet referred to by this rule, if it has been loaded. The
value of this attribute is

null

if the style sheet has
not yet been loaded or if it will not be loaded (e.g. if the style
sheet is for a media type not supported by the user agent).

---

#### Method Detail

getHref

```java
String
getHref()
```

The location of the style sheet to be imported. The attribute will not
contain the

"url(...)"

specifier around the URI.

---

#### getHref

String

getHref()

The location of the style sheet to be imported. The attribute will not
contain the

"url(...)"

specifier around the URI.

getMedia

```java
MediaList
getMedia()
```

A list of media types for which this style sheet may be used.

---

#### getMedia

MediaList

getMedia()

A list of media types for which this style sheet may be used.

getStyleSheet

```java
CSSStyleSheet
getStyleSheet()
```

The style sheet referred to by this rule, if it has been loaded. The
value of this attribute is

null

if the style sheet has
not yet been loaded or if it will not be loaded (e.g. if the style
sheet is for a media type not supported by the user agent).

---

#### getStyleSheet

CSSStyleSheet

getStyleSheet()

The style sheet referred to by this rule, if it has been loaded. The
value of this attribute is

null

if the style sheet has
not yet been loaded or if it will not be loaded (e.g. if the style
sheet is for a media type not supported by the user agent).

---

