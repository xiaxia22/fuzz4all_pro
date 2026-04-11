# Interface StyleSheet

**Source:** `jdk.xml.dom\org\w3c\dom\stylesheets\StyleSheet.html`

### Class Description

```java
public interface
StyleSheet
```

The

StyleSheet

interface is the abstract base interface for
any type of style sheet. It represents a single style sheet associated
with a structured document. In HTML, the StyleSheet interface represents
either an external style sheet, included via the HTML LINK element, or
an inline STYLE element. In XML, this interface represents an external
style sheet, included via a style sheet processing instruction.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**All Known Subinterfaces:** CSSStyleSheet

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getType()

This specifies the style sheet language for this style sheet. The
style sheet language is specified as a content type (e.g.
"text/css"). The content type is often specified in the

ownerNode

. Also see the type attribute definition for
the

LINK

element in HTML 4.0, and the type
pseudo-attribute for the XML style sheet processing instruction.

---

#### boolean getDisabled()

false

if the style sheet is applied to the document.

true

if it is not. Modifying this attribute may cause a
new resolution of style for the document. A stylesheet only applies
if both an appropriate medium definition is present and the disabled
attribute is false. So, if the media doesn't apply to the current
user agent, the

disabled

attribute is ignored.

---

#### void setDisabled​(boolean disabled)

false

if the style sheet is applied to the document.

true

if it is not. Modifying this attribute may cause a
new resolution of style for the document. A stylesheet only applies
if both an appropriate medium definition is present and the disabled
attribute is false. So, if the media doesn't apply to the current
user agent, the

disabled

attribute is ignored.

---

#### Node
getOwnerNode()

The node that associates this style sheet with the document. For HTML,
this may be the corresponding

LINK

or

STYLE

element. For XML, it may be the linking processing instruction. For
style sheets that are included by other style sheets, the value of
this attribute is

null

.

---

#### StyleSheet
getParentStyleSheet()

For style sheet languages that support the concept of style sheet
inclusion, this attribute represents the including style sheet, if
one exists. If the style sheet is a top-level style sheet, or the
style sheet language does not support inclusion, the value of this
attribute is

null

.

---

#### String
getHref()

If the style sheet is a linked style sheet, the value of its attribute
is its location. For inline style sheets, the value of this attribute
is

null

. See the href attribute definition for the

LINK

element in HTML 4.0, and the href pseudo-attribute
for the XML style sheet processing instruction.

---

#### String
getTitle()

The advisory title. The title is often specified in the

ownerNode

. See the title attribute definition for the

LINK

element in HTML 4.0, and the title pseudo-attribute
for the XML style sheet processing instruction.

---

#### MediaList
getMedia()

The intended destination media for style information. The media is
often specified in the

ownerNode

. If no media has been
specified, the

MediaList

will be empty. See the media
attribute definition for the

LINK

element in HTML 4.0,
and the media pseudo-attribute for the XML style sheet processing
instruction . Modifying the media list may cause a change to the
attribute

disabled

.

---

### Additional Sections

#### Interface StyleSheet

**All Known Subinterfaces:** CSSStyleSheet

```java
public interface
StyleSheet
```

The

StyleSheet

interface is the abstract base interface for
any type of style sheet. It represents a single style sheet associated
with a structured document. In HTML, the StyleSheet interface represents
either an external style sheet, included via the HTML LINK element, or
an inline STYLE element. In XML, this interface represents an external
style sheet, included via a style sheet processing instruction.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

StyleSheet

The

StyleSheet

interface is the abstract base interface for
any type of style sheet. It represents a single style sheet associated
with a structured document. In HTML, the StyleSheet interface represents
either an external style sheet, included via the HTML LINK element, or
an inline STYLE element. In XML, this interface represents an external
style sheet, included via a style sheet processing instruction.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

getDisabled

()

false

if the style sheet is applied to the document.

String

getHref

()

If the style sheet is a linked style sheet, the value of its attribute
is its location.

MediaList

getMedia

()

The intended destination media for style information.

Node

getOwnerNode

()

The node that associates this style sheet with the document.

StyleSheet

getParentStyleSheet

()

For style sheet languages that support the concept of style sheet
inclusion, this attribute represents the including style sheet, if
one exists.

String

getTitle

()

The advisory title.

String

getType

()

This specifies the style sheet language for this style sheet.

void

setDisabled

​(boolean disabled)

false

if the style sheet is applied to the document.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

getDisabled

()

false

if the style sheet is applied to the document.

String

getHref

()

If the style sheet is a linked style sheet, the value of its attribute
is its location.

MediaList

getMedia

()

The intended destination media for style information.

Node

getOwnerNode

()

The node that associates this style sheet with the document.

StyleSheet

getParentStyleSheet

()

For style sheet languages that support the concept of style sheet
inclusion, this attribute represents the including style sheet, if
one exists.

String

getTitle

()

The advisory title.

String

getType

()

This specifies the style sheet language for this style sheet.

void

setDisabled

​(boolean disabled)

false

if the style sheet is applied to the document.

---

#### Method Summary

false

if the style sheet is applied to the document.

If the style sheet is a linked style sheet, the value of its attribute
is its location.

The intended destination media for style information.

The node that associates this style sheet with the document.

For style sheet languages that support the concept of style sheet
inclusion, this attribute represents the including style sheet, if
one exists.

The advisory title.

This specifies the style sheet language for this style sheet.

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
String
getType()
```

This specifies the style sheet language for this style sheet. The
style sheet language is specified as a content type (e.g.
"text/css"). The content type is often specified in the

ownerNode

. Also see the type attribute definition for
the

LINK

element in HTML 4.0, and the type
pseudo-attribute for the XML style sheet processing instruction.

- getDisabled

```java
boolean getDisabled()
```

false

if the style sheet is applied to the document.

true

if it is not. Modifying this attribute may cause a
new resolution of style for the document. A stylesheet only applies
if both an appropriate medium definition is present and the disabled
attribute is false. So, if the media doesn't apply to the current
user agent, the

disabled

attribute is ignored.

- setDisabled

```java
void setDisabled​(boolean disabled)
```

false

if the style sheet is applied to the document.

true

if it is not. Modifying this attribute may cause a
new resolution of style for the document. A stylesheet only applies
if both an appropriate medium definition is present and the disabled
attribute is false. So, if the media doesn't apply to the current
user agent, the

disabled

attribute is ignored.

- getOwnerNode

```java
Node
getOwnerNode()
```

The node that associates this style sheet with the document. For HTML,
this may be the corresponding

LINK

or

STYLE

element. For XML, it may be the linking processing instruction. For
style sheets that are included by other style sheets, the value of
this attribute is

null

.

- getParentStyleSheet

```java
StyleSheet
getParentStyleSheet()
```

For style sheet languages that support the concept of style sheet
inclusion, this attribute represents the including style sheet, if
one exists. If the style sheet is a top-level style sheet, or the
style sheet language does not support inclusion, the value of this
attribute is

null

.

- getHref

```java
String
getHref()
```

If the style sheet is a linked style sheet, the value of its attribute
is its location. For inline style sheets, the value of this attribute
is

null

. See the href attribute definition for the

LINK

element in HTML 4.0, and the href pseudo-attribute
for the XML style sheet processing instruction.

- getTitle

```java
String
getTitle()
```

The advisory title. The title is often specified in the

ownerNode

. See the title attribute definition for the

LINK

element in HTML 4.0, and the title pseudo-attribute
for the XML style sheet processing instruction.

- getMedia

```java
MediaList
getMedia()
```

The intended destination media for style information. The media is
often specified in the

ownerNode

. If no media has been
specified, the

MediaList

will be empty. See the media
attribute definition for the

LINK

element in HTML 4.0,
and the media pseudo-attribute for the XML style sheet processing
instruction . Modifying the media list may cause a change to the
attribute

disabled

.

Method Detail

- getType

```java
String
getType()
```

This specifies the style sheet language for this style sheet. The
style sheet language is specified as a content type (e.g.
"text/css"). The content type is often specified in the

ownerNode

. Also see the type attribute definition for
the

LINK

element in HTML 4.0, and the type
pseudo-attribute for the XML style sheet processing instruction.

- getDisabled

```java
boolean getDisabled()
```

false

if the style sheet is applied to the document.

true

if it is not. Modifying this attribute may cause a
new resolution of style for the document. A stylesheet only applies
if both an appropriate medium definition is present and the disabled
attribute is false. So, if the media doesn't apply to the current
user agent, the

disabled

attribute is ignored.

- setDisabled

```java
void setDisabled​(boolean disabled)
```

false

if the style sheet is applied to the document.

true

if it is not. Modifying this attribute may cause a
new resolution of style for the document. A stylesheet only applies
if both an appropriate medium definition is present and the disabled
attribute is false. So, if the media doesn't apply to the current
user agent, the

disabled

attribute is ignored.

- getOwnerNode

```java
Node
getOwnerNode()
```

The node that associates this style sheet with the document. For HTML,
this may be the corresponding

LINK

or

STYLE

element. For XML, it may be the linking processing instruction. For
style sheets that are included by other style sheets, the value of
this attribute is

null

.

- getParentStyleSheet

```java
StyleSheet
getParentStyleSheet()
```

For style sheet languages that support the concept of style sheet
inclusion, this attribute represents the including style sheet, if
one exists. If the style sheet is a top-level style sheet, or the
style sheet language does not support inclusion, the value of this
attribute is

null

.

- getHref

```java
String
getHref()
```

If the style sheet is a linked style sheet, the value of its attribute
is its location. For inline style sheets, the value of this attribute
is

null

. See the href attribute definition for the

LINK

element in HTML 4.0, and the href pseudo-attribute
for the XML style sheet processing instruction.

- getTitle

```java
String
getTitle()
```

The advisory title. The title is often specified in the

ownerNode

. See the title attribute definition for the

LINK

element in HTML 4.0, and the title pseudo-attribute
for the XML style sheet processing instruction.

- getMedia

```java
MediaList
getMedia()
```

The intended destination media for style information. The media is
often specified in the

ownerNode

. If no media has been
specified, the

MediaList

will be empty. See the media
attribute definition for the

LINK

element in HTML 4.0,
and the media pseudo-attribute for the XML style sheet processing
instruction . Modifying the media list may cause a change to the
attribute

disabled

.

---

#### Method Detail

getType

```java
String
getType()
```

This specifies the style sheet language for this style sheet. The
style sheet language is specified as a content type (e.g.
"text/css"). The content type is often specified in the

ownerNode

. Also see the type attribute definition for
the

LINK

element in HTML 4.0, and the type
pseudo-attribute for the XML style sheet processing instruction.

---

#### getType

String

getType()

This specifies the style sheet language for this style sheet. The
style sheet language is specified as a content type (e.g.
"text/css"). The content type is often specified in the

ownerNode

. Also see the type attribute definition for
the

LINK

element in HTML 4.0, and the type
pseudo-attribute for the XML style sheet processing instruction.

getDisabled

```java
boolean getDisabled()
```

false

if the style sheet is applied to the document.

true

if it is not. Modifying this attribute may cause a
new resolution of style for the document. A stylesheet only applies
if both an appropriate medium definition is present and the disabled
attribute is false. So, if the media doesn't apply to the current
user agent, the

disabled

attribute is ignored.

---

#### getDisabled

boolean getDisabled()

false

if the style sheet is applied to the document.

true

if it is not. Modifying this attribute may cause a
new resolution of style for the document. A stylesheet only applies
if both an appropriate medium definition is present and the disabled
attribute is false. So, if the media doesn't apply to the current
user agent, the

disabled

attribute is ignored.

setDisabled

```java
void setDisabled​(boolean disabled)
```

false

if the style sheet is applied to the document.

true

if it is not. Modifying this attribute may cause a
new resolution of style for the document. A stylesheet only applies
if both an appropriate medium definition is present and the disabled
attribute is false. So, if the media doesn't apply to the current
user agent, the

disabled

attribute is ignored.

---

#### setDisabled

void setDisabled​(boolean disabled)

false

if the style sheet is applied to the document.

true

if it is not. Modifying this attribute may cause a
new resolution of style for the document. A stylesheet only applies
if both an appropriate medium definition is present and the disabled
attribute is false. So, if the media doesn't apply to the current
user agent, the

disabled

attribute is ignored.

getOwnerNode

```java
Node
getOwnerNode()
```

The node that associates this style sheet with the document. For HTML,
this may be the corresponding

LINK

or

STYLE

element. For XML, it may be the linking processing instruction. For
style sheets that are included by other style sheets, the value of
this attribute is

null

.

---

#### getOwnerNode

Node

getOwnerNode()

The node that associates this style sheet with the document. For HTML,
this may be the corresponding

LINK

or

STYLE

element. For XML, it may be the linking processing instruction. For
style sheets that are included by other style sheets, the value of
this attribute is

null

.

getParentStyleSheet

```java
StyleSheet
getParentStyleSheet()
```

For style sheet languages that support the concept of style sheet
inclusion, this attribute represents the including style sheet, if
one exists. If the style sheet is a top-level style sheet, or the
style sheet language does not support inclusion, the value of this
attribute is

null

.

---

#### getParentStyleSheet

StyleSheet

getParentStyleSheet()

For style sheet languages that support the concept of style sheet
inclusion, this attribute represents the including style sheet, if
one exists. If the style sheet is a top-level style sheet, or the
style sheet language does not support inclusion, the value of this
attribute is

null

.

getHref

```java
String
getHref()
```

If the style sheet is a linked style sheet, the value of its attribute
is its location. For inline style sheets, the value of this attribute
is

null

. See the href attribute definition for the

LINK

element in HTML 4.0, and the href pseudo-attribute
for the XML style sheet processing instruction.

---

#### getHref

String

getHref()

If the style sheet is a linked style sheet, the value of its attribute
is its location. For inline style sheets, the value of this attribute
is

null

. See the href attribute definition for the

LINK

element in HTML 4.0, and the href pseudo-attribute
for the XML style sheet processing instruction.

getTitle

```java
String
getTitle()
```

The advisory title. The title is often specified in the

ownerNode

. See the title attribute definition for the

LINK

element in HTML 4.0, and the title pseudo-attribute
for the XML style sheet processing instruction.

---

#### getTitle

String

getTitle()

The advisory title. The title is often specified in the

ownerNode

. See the title attribute definition for the

LINK

element in HTML 4.0, and the title pseudo-attribute
for the XML style sheet processing instruction.

getMedia

```java
MediaList
getMedia()
```

The intended destination media for style information. The media is
often specified in the

ownerNode

. If no media has been
specified, the

MediaList

will be empty. See the media
attribute definition for the

LINK

element in HTML 4.0,
and the media pseudo-attribute for the XML style sheet processing
instruction . Modifying the media list may cause a change to the
attribute

disabled

.

---

#### getMedia

MediaList

getMedia()

The intended destination media for style information. The media is
often specified in the

ownerNode

. If no media has been
specified, the

MediaList

will be empty. See the media
attribute definition for the

LINK

element in HTML 4.0,
and the media pseudo-attribute for the XML style sheet processing
instruction . Modifying the media list may cause a change to the
attribute

disabled

.

---

