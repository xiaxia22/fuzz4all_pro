# Interface CSSMediaRule

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSSMediaRule.html`

### Class Description

```java
public interface
CSSMediaRule

extends
CSSRule
```

The

CSSMediaRule

interface represents a @media rule in a CSS
style sheet. A

@media

rule can be used to delimit style
rules for specific media types.

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

#### MediaList
getMedia()

A list of media types for this rule.

---

#### CSSRuleList
getCssRules()

A list of all CSS rules contained within the media block.

---

#### int insertRule​(
String
rule,
int index)
throws
DOMException

Used to insert a new rule into the media block.

**Parameters:**
- rule

- The parsable text representing the rule. For rule sets
this contains both the selector and the style declaration. For
at-rules, this specifies both the at-identifier and the rule
content.
- index

- The index within the media block's rule collection of
the rule before which to insert the specified rule. If the
specified index is equal to the length of the media blocks's rule
collection, the rule will be added to the end of the media block.

**Returns:**
- The index within the media block's rule collection of the
newly inserted rule.

**Throws:**
- DOMException

- HIERARCHY_REQUEST_ERR: Raised if the rule cannot be inserted at the
specified index, e.g., if an

@import

rule is inserted
after a standard rule set or other at-rule.

INDEX_SIZE_ERR: Raised if the specified index is not a valid
insertion point.

NO_MODIFICATION_ALLOWED_ERR: Raised if this media rule is
readonly.

SYNTAX_ERR: Raised if the specified rule has a syntax error and
is unparsable.

---

#### void deleteRule​(int index)
throws
DOMException

Used to delete a rule from the media block.

**Parameters:**
- index

- The index within the media block's rule collection of
the rule to remove.

**Throws:**
- DOMException

- INDEX_SIZE_ERR: Raised if the specified index does not correspond to
a rule in the media rule list.

NO_MODIFICATION_ALLOWED_ERR: Raised if this media rule is
readonly.

---

### Additional Sections

#### Interface CSSMediaRule

**All Superinterfaces:** CSSRule

```java
public interface
CSSMediaRule

extends
CSSRule
```

The

CSSMediaRule

interface represents a @media rule in a CSS
style sheet. A

@media

rule can be used to delimit style
rules for specific media types.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSSMediaRule

extends

CSSRule

The

CSSMediaRule

interface represents a @media rule in a CSS
style sheet. A

@media

rule can be used to delimit style
rules for specific media types.

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

void

deleteRule

​(int index)

Used to delete a rule from the media block.

CSSRuleList

getCssRules

()

A list of all CSS rules contained within the media block.

MediaList

getMedia

()

A list of media types for this rule.

int

insertRule

​(

String

rule,
int index)

Used to insert a new rule into the media block.

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

void

deleteRule

​(int index)

Used to delete a rule from the media block.

CSSRuleList

getCssRules

()

A list of all CSS rules contained within the media block.

MediaList

getMedia

()

A list of media types for this rule.

int

insertRule

​(

String

rule,
int index)

Used to insert a new rule into the media block.

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

Used to delete a rule from the media block.

A list of all CSS rules contained within the media block.

A list of media types for this rule.

Used to insert a new rule into the media block.

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

- getMedia

```java
MediaList
getMedia()
```

A list of media types for this rule.

- getCssRules

```java
CSSRuleList
getCssRules()
```

A list of all CSS rules contained within the media block.

- insertRule

```java
int insertRule​(
String
rule,
int index)
throws
DOMException
```

Used to insert a new rule into the media block.

**Parameters:** rule

- The parsable text representing the rule. For rule sets
this contains both the selector and the style declaration. For
at-rules, this specifies both the at-identifier and the rule
content.
**Parameters:** index

- The index within the media block's rule collection of
the rule before which to insert the specified rule. If the
specified index is equal to the length of the media blocks's rule
collection, the rule will be added to the end of the media block.
**Returns:** The index within the media block's rule collection of the
newly inserted rule.
**Throws:** DOMException

- HIERARCHY_REQUEST_ERR: Raised if the rule cannot be inserted at the
specified index, e.g., if an

@import

rule is inserted
after a standard rule set or other at-rule.

INDEX_SIZE_ERR: Raised if the specified index is not a valid
insertion point.

NO_MODIFICATION_ALLOWED_ERR: Raised if this media rule is
readonly.

SYNTAX_ERR: Raised if the specified rule has a syntax error and
is unparsable.

- deleteRule

```java
void deleteRule​(int index)
throws
DOMException
```

Used to delete a rule from the media block.

**Parameters:** index

- The index within the media block's rule collection of
the rule to remove.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index does not correspond to
a rule in the media rule list.

NO_MODIFICATION_ALLOWED_ERR: Raised if this media rule is
readonly.

Method Detail

- getMedia

```java
MediaList
getMedia()
```

A list of media types for this rule.

- getCssRules

```java
CSSRuleList
getCssRules()
```

A list of all CSS rules contained within the media block.

- insertRule

```java
int insertRule​(
String
rule,
int index)
throws
DOMException
```

Used to insert a new rule into the media block.

**Parameters:** rule

- The parsable text representing the rule. For rule sets
this contains both the selector and the style declaration. For
at-rules, this specifies both the at-identifier and the rule
content.
**Parameters:** index

- The index within the media block's rule collection of
the rule before which to insert the specified rule. If the
specified index is equal to the length of the media blocks's rule
collection, the rule will be added to the end of the media block.
**Returns:** The index within the media block's rule collection of the
newly inserted rule.
**Throws:** DOMException

- HIERARCHY_REQUEST_ERR: Raised if the rule cannot be inserted at the
specified index, e.g., if an

@import

rule is inserted
after a standard rule set or other at-rule.

INDEX_SIZE_ERR: Raised if the specified index is not a valid
insertion point.

NO_MODIFICATION_ALLOWED_ERR: Raised if this media rule is
readonly.

SYNTAX_ERR: Raised if the specified rule has a syntax error and
is unparsable.

- deleteRule

```java
void deleteRule​(int index)
throws
DOMException
```

Used to delete a rule from the media block.

**Parameters:** index

- The index within the media block's rule collection of
the rule to remove.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index does not correspond to
a rule in the media rule list.

NO_MODIFICATION_ALLOWED_ERR: Raised if this media rule is
readonly.

---

#### Method Detail

getMedia

```java
MediaList
getMedia()
```

A list of media types for this rule.

---

#### getMedia

MediaList

getMedia()

A list of media types for this rule.

getCssRules

```java
CSSRuleList
getCssRules()
```

A list of all CSS rules contained within the media block.

---

#### getCssRules

CSSRuleList

getCssRules()

A list of all CSS rules contained within the media block.

insertRule

```java
int insertRule​(
String
rule,
int index)
throws
DOMException
```

Used to insert a new rule into the media block.

**Parameters:** rule

- The parsable text representing the rule. For rule sets
this contains both the selector and the style declaration. For
at-rules, this specifies both the at-identifier and the rule
content.
**Parameters:** index

- The index within the media block's rule collection of
the rule before which to insert the specified rule. If the
specified index is equal to the length of the media blocks's rule
collection, the rule will be added to the end of the media block.
**Returns:** The index within the media block's rule collection of the
newly inserted rule.
**Throws:** DOMException

- HIERARCHY_REQUEST_ERR: Raised if the rule cannot be inserted at the
specified index, e.g., if an

@import

rule is inserted
after a standard rule set or other at-rule.

INDEX_SIZE_ERR: Raised if the specified index is not a valid
insertion point.

NO_MODIFICATION_ALLOWED_ERR: Raised if this media rule is
readonly.

SYNTAX_ERR: Raised if the specified rule has a syntax error and
is unparsable.

---

#### insertRule

int insertRule​(

String

rule,
int index)
throws

DOMException

Used to insert a new rule into the media block.

deleteRule

```java
void deleteRule​(int index)
throws
DOMException
```

Used to delete a rule from the media block.

**Parameters:** index

- The index within the media block's rule collection of
the rule to remove.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index does not correspond to
a rule in the media rule list.

NO_MODIFICATION_ALLOWED_ERR: Raised if this media rule is
readonly.

---

#### deleteRule

void deleteRule​(int index)
throws

DOMException

Used to delete a rule from the media block.

---

