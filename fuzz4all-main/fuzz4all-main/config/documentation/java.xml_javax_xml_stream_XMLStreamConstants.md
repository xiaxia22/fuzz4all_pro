# Interface XMLStreamConstants

**Source:** `java.xml\javax\xml\stream\XMLStreamConstants.html`

### Class Description

```java
public interface
XMLStreamConstants
```

This interface declares the constants used in this API.
Numbers in the range 0 to 256 are reserved for the specification,
user defined events must use event codes outside that range.

**All Known Subinterfaces:** Attribute

,

Characters

,

Comment

,

DTD

,

EndDocument

,

EndElement

,

EntityDeclaration

,

EntityReference

,

Namespace

,

NotationDeclaration

,

ProcessingInstruction

,

StartDocument

,

StartElement

,

XMLEvent

,

XMLStreamReader

---

### Field Details

#### static final int START_ELEMENT

Indicates an event is a start element

**See Also:**
- StartElement

,

Constant Field Values

---

#### static final int END_ELEMENT

Indicates an event is an end element

**See Also:**
- EndElement

,

Constant Field Values

---

#### static final int PROCESSING_INSTRUCTION

Indicates an event is a processing instruction

**See Also:**
- ProcessingInstruction

,

Constant Field Values

---

#### static final int CHARACTERS

Indicates an event is characters

**See Also:**
- Characters

,

Constant Field Values

---

#### static final int COMMENT

Indicates an event is a comment

**See Also:**
- Comment

,

Constant Field Values

---

#### static final int SPACE

The characters are white space
(see [XML], 2.10 "White Space Handling").
Events are only reported as SPACE if they are ignorable white
space. Otherwise they are reported as CHARACTERS.

**See Also:**
- Characters

,

Constant Field Values

---

#### static final int START_DOCUMENT

Indicates an event is a start document

**See Also:**
- StartDocument

,

Constant Field Values

---

#### static final int END_DOCUMENT

Indicates an event is an end document

**See Also:**
- EndDocument

,

Constant Field Values

---

#### static final int ENTITY_REFERENCE

Indicates an event is an entity reference

**See Also:**
- EntityReference

,

Constant Field Values

---

#### static final int ATTRIBUTE

Indicates an event is an attribute

**See Also:**
- Attribute

,

Constant Field Values

---

#### static final int DTD

Indicates an event is a DTD

**See Also:**
- DTD

,

Constant Field Values

---

#### static final int CDATA

Indicates an event is a CDATA section

**See Also:**
- Characters

,

Constant Field Values

---

#### static final int NAMESPACE

Indicates the event is a namespace declaration

**See Also:**
- Namespace

,

Constant Field Values

---

#### static final int NOTATION_DECLARATION

Indicates a Notation

**See Also:**
- NotationDeclaration

,

Constant Field Values

---

#### static final int ENTITY_DECLARATION

Indicates a Entity Declaration

**See Also:**
- NotationDeclaration

,

Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface XMLStreamConstants

**All Known Subinterfaces:** Attribute

,

Characters

,

Comment

,

DTD

,

EndDocument

,

EndElement

,

EntityDeclaration

,

EntityReference

,

Namespace

,

NotationDeclaration

,

ProcessingInstruction

,

StartDocument

,

StartElement

,

XMLEvent

,

XMLStreamReader

**All Known Implementing Classes:** StreamReaderDelegate

```java
public interface
XMLStreamConstants
```

This interface declares the constants used in this API.
Numbers in the range 0 to 256 are reserved for the specification,
user defined events must use event codes outside that range.

**Since:** 1.6

public interface

XMLStreamConstants

This interface declares the constants used in this API.
Numbers in the range 0 to 256 are reserved for the specification,
user defined events must use event codes outside that range.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ATTRIBUTE

Indicates an event is an attribute

static int

CDATA

Indicates an event is a CDATA section

static int

CHARACTERS

Indicates an event is characters

static int

COMMENT

Indicates an event is a comment

static int

DTD

Indicates an event is a DTD

static int

END_DOCUMENT

Indicates an event is an end document

static int

END_ELEMENT

Indicates an event is an end element

static int

ENTITY_DECLARATION

Indicates a Entity Declaration

static int

ENTITY_REFERENCE

Indicates an event is an entity reference

static int

NAMESPACE

Indicates the event is a namespace declaration

static int

NOTATION_DECLARATION

Indicates a Notation

static int

PROCESSING_INSTRUCTION

Indicates an event is a processing instruction

static int

SPACE

The characters are white space
(see [XML], 2.10 "White Space Handling").

static int

START_DOCUMENT

Indicates an event is a start document

static int

START_ELEMENT

Indicates an event is a start element

Field Summary

Fields

Modifier and Type

Field

Description

static int

ATTRIBUTE

Indicates an event is an attribute

static int

CDATA

Indicates an event is a CDATA section

static int

CHARACTERS

Indicates an event is characters

static int

COMMENT

Indicates an event is a comment

static int

DTD

Indicates an event is a DTD

static int

END_DOCUMENT

Indicates an event is an end document

static int

END_ELEMENT

Indicates an event is an end element

static int

ENTITY_DECLARATION

Indicates a Entity Declaration

static int

ENTITY_REFERENCE

Indicates an event is an entity reference

static int

NAMESPACE

Indicates the event is a namespace declaration

static int

NOTATION_DECLARATION

Indicates a Notation

static int

PROCESSING_INSTRUCTION

Indicates an event is a processing instruction

static int

SPACE

The characters are white space
(see [XML], 2.10 "White Space Handling").

static int

START_DOCUMENT

Indicates an event is a start document

static int

START_ELEMENT

Indicates an event is a start element

---

#### Field Summary

Indicates an event is an attribute

Indicates an event is a CDATA section

Indicates an event is characters

Indicates an event is a comment

Indicates an event is a DTD

Indicates an event is an end document

Indicates an event is an end element

Indicates a Entity Declaration

Indicates an event is an entity reference

Indicates the event is a namespace declaration

Indicates a Notation

Indicates an event is a processing instruction

The characters are white space
(see [XML], 2.10 "White Space Handling").

Indicates an event is a start document

Indicates an event is a start element

============ FIELD DETAIL ===========

- Field Detail

- START_ELEMENT

```java
static final int START_ELEMENT
```

Indicates an event is a start element

**See Also:** StartElement

,

Constant Field Values

- END_ELEMENT

```java
static final int END_ELEMENT
```

Indicates an event is an end element

**See Also:** EndElement

,

Constant Field Values

- PROCESSING_INSTRUCTION

```java
static final int PROCESSING_INSTRUCTION
```

Indicates an event is a processing instruction

**See Also:** ProcessingInstruction

,

Constant Field Values

- CHARACTERS

```java
static final int CHARACTERS
```

Indicates an event is characters

**See Also:** Characters

,

Constant Field Values

- COMMENT

```java
static final int COMMENT
```

Indicates an event is a comment

**See Also:** Comment

,

Constant Field Values

- SPACE

```java
static final int SPACE
```

The characters are white space
(see [XML], 2.10 "White Space Handling").
Events are only reported as SPACE if they are ignorable white
space. Otherwise they are reported as CHARACTERS.

**See Also:** Characters

,

Constant Field Values

- START_DOCUMENT

```java
static final int START_DOCUMENT
```

Indicates an event is a start document

**See Also:** StartDocument

,

Constant Field Values

- END_DOCUMENT

```java
static final int END_DOCUMENT
```

Indicates an event is an end document

**See Also:** EndDocument

,

Constant Field Values

- ENTITY_REFERENCE

```java
static final int ENTITY_REFERENCE
```

Indicates an event is an entity reference

**See Also:** EntityReference

,

Constant Field Values

- ATTRIBUTE

```java
static final int ATTRIBUTE
```

Indicates an event is an attribute

**See Also:** Attribute

,

Constant Field Values

- DTD

```java
static final int DTD
```

Indicates an event is a DTD

**See Also:** DTD

,

Constant Field Values

- CDATA

```java
static final int CDATA
```

Indicates an event is a CDATA section

**See Also:** Characters

,

Constant Field Values

- NAMESPACE

```java
static final int NAMESPACE
```

Indicates the event is a namespace declaration

**See Also:** Namespace

,

Constant Field Values

- NOTATION_DECLARATION

```java
static final int NOTATION_DECLARATION
```

Indicates a Notation

**See Also:** NotationDeclaration

,

Constant Field Values

- ENTITY_DECLARATION

```java
static final int ENTITY_DECLARATION
```

Indicates a Entity Declaration

**See Also:** NotationDeclaration

,

Constant Field Values

Field Detail

- START_ELEMENT

```java
static final int START_ELEMENT
```

Indicates an event is a start element

**See Also:** StartElement

,

Constant Field Values

- END_ELEMENT

```java
static final int END_ELEMENT
```

Indicates an event is an end element

**See Also:** EndElement

,

Constant Field Values

- PROCESSING_INSTRUCTION

```java
static final int PROCESSING_INSTRUCTION
```

Indicates an event is a processing instruction

**See Also:** ProcessingInstruction

,

Constant Field Values

- CHARACTERS

```java
static final int CHARACTERS
```

Indicates an event is characters

**See Also:** Characters

,

Constant Field Values

- COMMENT

```java
static final int COMMENT
```

Indicates an event is a comment

**See Also:** Comment

,

Constant Field Values

- SPACE

```java
static final int SPACE
```

The characters are white space
(see [XML], 2.10 "White Space Handling").
Events are only reported as SPACE if they are ignorable white
space. Otherwise they are reported as CHARACTERS.

**See Also:** Characters

,

Constant Field Values

- START_DOCUMENT

```java
static final int START_DOCUMENT
```

Indicates an event is a start document

**See Also:** StartDocument

,

Constant Field Values

- END_DOCUMENT

```java
static final int END_DOCUMENT
```

Indicates an event is an end document

**See Also:** EndDocument

,

Constant Field Values

- ENTITY_REFERENCE

```java
static final int ENTITY_REFERENCE
```

Indicates an event is an entity reference

**See Also:** EntityReference

,

Constant Field Values

- ATTRIBUTE

```java
static final int ATTRIBUTE
```

Indicates an event is an attribute

**See Also:** Attribute

,

Constant Field Values

- DTD

```java
static final int DTD
```

Indicates an event is a DTD

**See Also:** DTD

,

Constant Field Values

- CDATA

```java
static final int CDATA
```

Indicates an event is a CDATA section

**See Also:** Characters

,

Constant Field Values

- NAMESPACE

```java
static final int NAMESPACE
```

Indicates the event is a namespace declaration

**See Also:** Namespace

,

Constant Field Values

- NOTATION_DECLARATION

```java
static final int NOTATION_DECLARATION
```

Indicates a Notation

**See Also:** NotationDeclaration

,

Constant Field Values

- ENTITY_DECLARATION

```java
static final int ENTITY_DECLARATION
```

Indicates a Entity Declaration

**See Also:** NotationDeclaration

,

Constant Field Values

---

#### Field Detail

START_ELEMENT

```java
static final int START_ELEMENT
```

Indicates an event is a start element

**See Also:** StartElement

,

Constant Field Values

---

#### START_ELEMENT

static final int START_ELEMENT

Indicates an event is a start element

END_ELEMENT

```java
static final int END_ELEMENT
```

Indicates an event is an end element

**See Also:** EndElement

,

Constant Field Values

---

#### END_ELEMENT

static final int END_ELEMENT

Indicates an event is an end element

PROCESSING_INSTRUCTION

```java
static final int PROCESSING_INSTRUCTION
```

Indicates an event is a processing instruction

**See Also:** ProcessingInstruction

,

Constant Field Values

---

#### PROCESSING_INSTRUCTION

static final int PROCESSING_INSTRUCTION

Indicates an event is a processing instruction

CHARACTERS

```java
static final int CHARACTERS
```

Indicates an event is characters

**See Also:** Characters

,

Constant Field Values

---

#### CHARACTERS

static final int CHARACTERS

Indicates an event is characters

COMMENT

```java
static final int COMMENT
```

Indicates an event is a comment

**See Also:** Comment

,

Constant Field Values

---

#### COMMENT

static final int COMMENT

Indicates an event is a comment

SPACE

```java
static final int SPACE
```

The characters are white space
(see [XML], 2.10 "White Space Handling").
Events are only reported as SPACE if they are ignorable white
space. Otherwise they are reported as CHARACTERS.

**See Also:** Characters

,

Constant Field Values

---

#### SPACE

static final int SPACE

The characters are white space
(see [XML], 2.10 "White Space Handling").
Events are only reported as SPACE if they are ignorable white
space. Otherwise they are reported as CHARACTERS.

START_DOCUMENT

```java
static final int START_DOCUMENT
```

Indicates an event is a start document

**See Also:** StartDocument

,

Constant Field Values

---

#### START_DOCUMENT

static final int START_DOCUMENT

Indicates an event is a start document

END_DOCUMENT

```java
static final int END_DOCUMENT
```

Indicates an event is an end document

**See Also:** EndDocument

,

Constant Field Values

---

#### END_DOCUMENT

static final int END_DOCUMENT

Indicates an event is an end document

ENTITY_REFERENCE

```java
static final int ENTITY_REFERENCE
```

Indicates an event is an entity reference

**See Also:** EntityReference

,

Constant Field Values

---

#### ENTITY_REFERENCE

static final int ENTITY_REFERENCE

Indicates an event is an entity reference

ATTRIBUTE

```java
static final int ATTRIBUTE
```

Indicates an event is an attribute

**See Also:** Attribute

,

Constant Field Values

---

#### ATTRIBUTE

static final int ATTRIBUTE

Indicates an event is an attribute

DTD

```java
static final int DTD
```

Indicates an event is a DTD

**See Also:** DTD

,

Constant Field Values

---

#### DTD

static final int DTD

Indicates an event is a DTD

CDATA

```java
static final int CDATA
```

Indicates an event is a CDATA section

**See Also:** Characters

,

Constant Field Values

---

#### CDATA

static final int CDATA

Indicates an event is a CDATA section

NAMESPACE

```java
static final int NAMESPACE
```

Indicates the event is a namespace declaration

**See Also:** Namespace

,

Constant Field Values

---

#### NAMESPACE

static final int NAMESPACE

Indicates the event is a namespace declaration

NOTATION_DECLARATION

```java
static final int NOTATION_DECLARATION
```

Indicates a Notation

**See Also:** NotationDeclaration

,

Constant Field Values

---

#### NOTATION_DECLARATION

static final int NOTATION_DECLARATION

Indicates a Notation

ENTITY_DECLARATION

```java
static final int ENTITY_DECLARATION
```

Indicates a Entity Declaration

**See Also:** NotationDeclaration

,

Constant Field Values

---

#### ENTITY_DECLARATION

static final int ENTITY_DECLARATION

Indicates a Entity Declaration

---

