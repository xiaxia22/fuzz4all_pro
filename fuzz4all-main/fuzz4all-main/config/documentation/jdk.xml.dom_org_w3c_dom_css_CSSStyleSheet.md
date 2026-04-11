# Interface CSSStyleSheet

**Source:** `jdk.xml.dom\org\w3c\dom\css\CSSStyleSheet.html`

### Class Description

```java
public interface
CSSStyleSheet

extends
StyleSheet
```

The

CSSStyleSheet

interface is a concrete interface used to
represent a CSS style sheet i.e., a style sheet whose content type is
"text/css".

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**All Superinterfaces:** StyleSheet

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### CSSRule
getOwnerRule()

If this style sheet comes from an

@import

rule, the

ownerRule

attribute will contain the

CSSImportRule

. In that case, the

ownerNode

attribute in the

StyleSheet

interface will be

null

. If the style sheet comes from an element or a
processing instruction, the

ownerRule

attribute will be

null

and the

ownerNode

attribute will
contain the

Node

.

---

#### CSSRuleList
getCssRules()

The list of all CSS rules contained within the style sheet. This
includes both rule sets and at-rules.

---

#### int insertRule​(
String
rule,
int index)
throws
DOMException

Used to insert a new rule into the style sheet. The new rule now
becomes part of the cascade.

**Parameters:**
- rule

- The parsable text representing the rule. For rule sets
this contains both the selector and the style declaration. For
at-rules, this specifies both the at-identifier and the rule
content.
- index

- The index within the style sheet's rule list of the rule
before which to insert the specified rule. If the specified index
is equal to the length of the style sheet's rule collection, the
rule will be added to the end of the style sheet.

**Returns:**
- The index within the style sheet's rule collection of the
newly inserted rule.

**Throws:**
- DOMException

- HIERARCHY_REQUEST_ERR: Raised if the rule cannot be inserted at the
specified index e.g. if an

@import

rule is inserted
after a standard rule set or other at-rule.

INDEX_SIZE_ERR: Raised if the specified index is not a valid
insertion point.

NO_MODIFICATION_ALLOWED_ERR: Raised if this style sheet is
readonly.

SYNTAX_ERR: Raised if the specified rule has a syntax error and
is unparsable.

---

#### void deleteRule​(int index)
throws
DOMException

Used to delete a rule from the style sheet.

**Parameters:**
- index

- The index within the style sheet's rule list of the rule
to remove.

**Throws:**
- DOMException

- INDEX_SIZE_ERR: Raised if the specified index does not correspond to
a rule in the style sheet's rule list.

NO_MODIFICATION_ALLOWED_ERR: Raised if this style sheet is
readonly.

---

### Additional Sections

#### Interface CSSStyleSheet

**All Superinterfaces:** StyleSheet

```java
public interface
CSSStyleSheet

extends
StyleSheet
```

The

CSSStyleSheet

interface is a concrete interface used to
represent a CSS style sheet i.e., a style sheet whose content type is
"text/css".

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

CSSStyleSheet

extends

StyleSheet

The

CSSStyleSheet

interface is a concrete interface used to
represent a CSS style sheet i.e., a style sheet whose content type is
"text/css".

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

void

deleteRule

​(int index)

Used to delete a rule from the style sheet.

CSSRuleList

getCssRules

()

The list of all CSS rules contained within the style sheet.

CSSRule

getOwnerRule

()

If this style sheet comes from an

@import

rule, the

ownerRule

attribute will contain the

CSSImportRule

.

int

insertRule

​(

String

rule,
int index)

Used to insert a new rule into the style sheet.

- Methods declared in interface org.w3c.dom.stylesheets.

StyleSheet

getDisabled

,

getHref

,

getMedia

,

getOwnerNode

,

getParentStyleSheet

,

getTitle

,

getType

,

setDisabled

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

Used to delete a rule from the style sheet.

CSSRuleList

getCssRules

()

The list of all CSS rules contained within the style sheet.

CSSRule

getOwnerRule

()

If this style sheet comes from an

@import

rule, the

ownerRule

attribute will contain the

CSSImportRule

.

int

insertRule

​(

String

rule,
int index)

Used to insert a new rule into the style sheet.

- Methods declared in interface org.w3c.dom.stylesheets.

StyleSheet

getDisabled

,

getHref

,

getMedia

,

getOwnerNode

,

getParentStyleSheet

,

getTitle

,

getType

,

setDisabled

---

#### Method Summary

Used to delete a rule from the style sheet.

The list of all CSS rules contained within the style sheet.

If this style sheet comes from an

@import

rule, the

ownerRule

attribute will contain the

CSSImportRule

.

Used to insert a new rule into the style sheet.

Methods declared in interface org.w3c.dom.stylesheets.

StyleSheet

getDisabled

,

getHref

,

getMedia

,

getOwnerNode

,

getParentStyleSheet

,

getTitle

,

getType

,

setDisabled

---

#### Methods declared in interface org.w3c.dom.stylesheets. StyleSheet

============ METHOD DETAIL ==========

- Method Detail

- getOwnerRule

```java
CSSRule
getOwnerRule()
```

If this style sheet comes from an

@import

rule, the

ownerRule

attribute will contain the

CSSImportRule

. In that case, the

ownerNode

attribute in the

StyleSheet

interface will be

null

. If the style sheet comes from an element or a
processing instruction, the

ownerRule

attribute will be

null

and the

ownerNode

attribute will
contain the

Node

.

- getCssRules

```java
CSSRuleList
getCssRules()
```

The list of all CSS rules contained within the style sheet. This
includes both rule sets and at-rules.

- insertRule

```java
int insertRule​(
String
rule,
int index)
throws
DOMException
```

Used to insert a new rule into the style sheet. The new rule now
becomes part of the cascade.

**Parameters:** rule

- The parsable text representing the rule. For rule sets
this contains both the selector and the style declaration. For
at-rules, this specifies both the at-identifier and the rule
content.
**Parameters:** index

- The index within the style sheet's rule list of the rule
before which to insert the specified rule. If the specified index
is equal to the length of the style sheet's rule collection, the
rule will be added to the end of the style sheet.
**Returns:** The index within the style sheet's rule collection of the
newly inserted rule.
**Throws:** DOMException

- HIERARCHY_REQUEST_ERR: Raised if the rule cannot be inserted at the
specified index e.g. if an

@import

rule is inserted
after a standard rule set or other at-rule.

INDEX_SIZE_ERR: Raised if the specified index is not a valid
insertion point.

NO_MODIFICATION_ALLOWED_ERR: Raised if this style sheet is
readonly.

SYNTAX_ERR: Raised if the specified rule has a syntax error and
is unparsable.

- deleteRule

```java
void deleteRule​(int index)
throws
DOMException
```

Used to delete a rule from the style sheet.

**Parameters:** index

- The index within the style sheet's rule list of the rule
to remove.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index does not correspond to
a rule in the style sheet's rule list.

NO_MODIFICATION_ALLOWED_ERR: Raised if this style sheet is
readonly.

Method Detail

- getOwnerRule

```java
CSSRule
getOwnerRule()
```

If this style sheet comes from an

@import

rule, the

ownerRule

attribute will contain the

CSSImportRule

. In that case, the

ownerNode

attribute in the

StyleSheet

interface will be

null

. If the style sheet comes from an element or a
processing instruction, the

ownerRule

attribute will be

null

and the

ownerNode

attribute will
contain the

Node

.

- getCssRules

```java
CSSRuleList
getCssRules()
```

The list of all CSS rules contained within the style sheet. This
includes both rule sets and at-rules.

- insertRule

```java
int insertRule​(
String
rule,
int index)
throws
DOMException
```

Used to insert a new rule into the style sheet. The new rule now
becomes part of the cascade.

**Parameters:** rule

- The parsable text representing the rule. For rule sets
this contains both the selector and the style declaration. For
at-rules, this specifies both the at-identifier and the rule
content.
**Parameters:** index

- The index within the style sheet's rule list of the rule
before which to insert the specified rule. If the specified index
is equal to the length of the style sheet's rule collection, the
rule will be added to the end of the style sheet.
**Returns:** The index within the style sheet's rule collection of the
newly inserted rule.
**Throws:** DOMException

- HIERARCHY_REQUEST_ERR: Raised if the rule cannot be inserted at the
specified index e.g. if an

@import

rule is inserted
after a standard rule set or other at-rule.

INDEX_SIZE_ERR: Raised if the specified index is not a valid
insertion point.

NO_MODIFICATION_ALLOWED_ERR: Raised if this style sheet is
readonly.

SYNTAX_ERR: Raised if the specified rule has a syntax error and
is unparsable.

- deleteRule

```java
void deleteRule​(int index)
throws
DOMException
```

Used to delete a rule from the style sheet.

**Parameters:** index

- The index within the style sheet's rule list of the rule
to remove.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index does not correspond to
a rule in the style sheet's rule list.

NO_MODIFICATION_ALLOWED_ERR: Raised if this style sheet is
readonly.

---

#### Method Detail

getOwnerRule

```java
CSSRule
getOwnerRule()
```

If this style sheet comes from an

@import

rule, the

ownerRule

attribute will contain the

CSSImportRule

. In that case, the

ownerNode

attribute in the

StyleSheet

interface will be

null

. If the style sheet comes from an element or a
processing instruction, the

ownerRule

attribute will be

null

and the

ownerNode

attribute will
contain the

Node

.

---

#### getOwnerRule

CSSRule

getOwnerRule()

If this style sheet comes from an

@import

rule, the

ownerRule

attribute will contain the

CSSImportRule

. In that case, the

ownerNode

attribute in the

StyleSheet

interface will be

null

. If the style sheet comes from an element or a
processing instruction, the

ownerRule

attribute will be

null

and the

ownerNode

attribute will
contain the

Node

.

getCssRules

```java
CSSRuleList
getCssRules()
```

The list of all CSS rules contained within the style sheet. This
includes both rule sets and at-rules.

---

#### getCssRules

CSSRuleList

getCssRules()

The list of all CSS rules contained within the style sheet. This
includes both rule sets and at-rules.

insertRule

```java
int insertRule​(
String
rule,
int index)
throws
DOMException
```

Used to insert a new rule into the style sheet. The new rule now
becomes part of the cascade.

**Parameters:** rule

- The parsable text representing the rule. For rule sets
this contains both the selector and the style declaration. For
at-rules, this specifies both the at-identifier and the rule
content.
**Parameters:** index

- The index within the style sheet's rule list of the rule
before which to insert the specified rule. If the specified index
is equal to the length of the style sheet's rule collection, the
rule will be added to the end of the style sheet.
**Returns:** The index within the style sheet's rule collection of the
newly inserted rule.
**Throws:** DOMException

- HIERARCHY_REQUEST_ERR: Raised if the rule cannot be inserted at the
specified index e.g. if an

@import

rule is inserted
after a standard rule set or other at-rule.

INDEX_SIZE_ERR: Raised if the specified index is not a valid
insertion point.

NO_MODIFICATION_ALLOWED_ERR: Raised if this style sheet is
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

Used to insert a new rule into the style sheet. The new rule now
becomes part of the cascade.

deleteRule

```java
void deleteRule​(int index)
throws
DOMException
```

Used to delete a rule from the style sheet.

**Parameters:** index

- The index within the style sheet's rule list of the rule
to remove.
**Throws:** DOMException

- INDEX_SIZE_ERR: Raised if the specified index does not correspond to
a rule in the style sheet's rule list.

NO_MODIFICATION_ALLOWED_ERR: Raised if this style sheet is
readonly.

---

#### deleteRule

void deleteRule​(int index)
throws

DOMException

Used to delete a rule from the style sheet.

---

