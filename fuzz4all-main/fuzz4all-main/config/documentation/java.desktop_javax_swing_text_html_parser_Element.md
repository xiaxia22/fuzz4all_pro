# Class Element

**Source:** `java.desktop\javax\swing\text\html\parser\Element.html`

### Class Description

```java
public final class
Element

extends
Object

implements
DTDConstants
,
Serializable
```

An element as described in a DTD using the ELEMENT construct.
This is essential the description of a tag. It describes the
type, content model, attributes, attribute types etc. It is used
to correctly parse a document by the Parser.

**All Implemented Interfaces:** Serializable

,

DTDConstants

---

### Field Details

#### public int index

The element index

---

#### public
String
name

The name of the element

---

#### public boolean oStart

true

if the start tag can be omitted

---

#### public boolean oEnd

true

if the end tag can be omitted

---

#### public
BitSet
inclusions

The set of elements that can occur inside the element

---

#### public
BitSet
exclusions

The set of elements that must not occur inside the element

---

#### public int type

The element type

---

#### public
ContentModel
content

The content model

---

#### public
AttributeList
atts

The attributes

---

#### public
Object
data

A field to store user data. Mostly used to store
style sheets.

---

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getName()

Get the name of the element.

**Returns:**
- the name of the element

---

#### public boolean omitStart()

Return true if the start tag can be omitted.

**Returns:**
- true

if the start tag can be omitted

---

#### public boolean omitEnd()

Return true if the end tag can be omitted.

**Returns:**
- true

if the end tag can be omitted

---

#### public int getType()

Get type.

**Returns:**
- the type of the element

---

#### public
ContentModel
getContent()

Get content model

**Returns:**
- the content model

---

#### public
AttributeList
getAttributes()

Get the attributes.

**Returns:**
- the

AttributeList

specifying the element

---

#### public int getIndex()

Get index.

**Returns:**
- the element index

---

#### public boolean isEmpty()

Check if empty

**Returns:**
- true if the current element is empty

---

#### public
String
toString()

Convert to a string.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation for the given

Element

instance

---

#### public
AttributeList
getAttribute​(
String
name)

Get an attribute by name.

**Parameters:**
- name

- the attribute name

**Returns:**
- the

AttributeList

for the given

name

---

#### public
AttributeList
getAttributeByValue​(
String
value)

Get an attribute by value.

**Parameters:**
- value

- the string representation of value

**Returns:**
- the

AttributeList

for the given

value

---

#### public static int name2type​(
String
nm)

Converts

nm

to type. Returns appropriate DTDConstants
if the

nm

is equal to CDATA, RCDATA, EMPTY or ANY, 0 otherwise.

**Parameters:**
- nm

- a name

**Returns:**
- appropriate DTDConstants if the

nm

is equal to
CDATA, RCDATA, EMPTY or ANY, 0 otherwise.

---

### Additional Sections

#### Class Element

java.lang.Object

- javax.swing.text.html.parser.Element

javax.swing.text.html.parser.Element

**All Implemented Interfaces:** Serializable

,

DTDConstants

```java
public final class
Element

extends
Object

implements
DTDConstants
,
Serializable
```

An element as described in a DTD using the ELEMENT construct.
This is essential the description of a tag. It describes the
type, content model, attributes, attribute types etc. It is used
to correctly parse a document by the Parser.

**See Also:** DTD

,

AttributeList

,

Serialized Form

public final class

Element

extends

Object

implements

DTDConstants

,

Serializable

An element as described in a DTD using the ELEMENT construct.
This is essential the description of a tag. It describes the
type, content model, attributes, attribute types etc. It is used
to correctly parse a document by the Parser.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

AttributeList

atts

The attributes

ContentModel

content

The content model

Object

data

A field to store user data.

BitSet

exclusions

The set of elements that must not occur inside the element

BitSet

inclusions

The set of elements that can occur inside the element

int

index

The element index

String

name

The name of the element

boolean

oEnd

true

if the end tag can be omitted

boolean

oStart

true

if the start tag can be omitted

int

type

The element type

- Fields declared in interface javax.swing.text.html.parser.

DTDConstants

ANY

,

CDATA

,

CONREF

,

CURRENT

,

DEFAULT

,

EMPTY

,

ENDTAG

,

ENTITIES

,

ENTITY

,

FIXED

,

GENERAL

,

ID

,

IDREF

,

IDREFS

,

IMPLIED

,

MD

,

MODEL

,

MS

,

NAME

,

NAMES

,

NMTOKEN

,

NMTOKENS

,

NOTATION

,

NUMBER

,

NUMBERS

,

NUTOKEN

,

NUTOKENS

,

PARAMETER

,

PI

,

PUBLIC

,

RCDATA

,

REQUIRED

,

SDATA

,

STARTTAG

,

SYSTEM

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AttributeList

getAttribute

​(

String

name)

Get an attribute by name.

AttributeList

getAttributeByValue

​(

String

value)

Get an attribute by value.

AttributeList

getAttributes

()

Get the attributes.

ContentModel

getContent

()

Get content model

int

getIndex

()

Get index.

String

getName

()

Get the name of the element.

int

getType

()

Get type.

boolean

isEmpty

()

Check if empty

static int

name2type

​(

String

nm)

Converts

nm

to type.

boolean

omitEnd

()

Return true if the end tag can be omitted.

boolean

omitStart

()

Return true if the start tag can be omitted.

String

toString

()

Convert to a string.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

AttributeList

atts

The attributes

ContentModel

content

The content model

Object

data

A field to store user data.

BitSet

exclusions

The set of elements that must not occur inside the element

BitSet

inclusions

The set of elements that can occur inside the element

int

index

The element index

String

name

The name of the element

boolean

oEnd

true

if the end tag can be omitted

boolean

oStart

true

if the start tag can be omitted

int

type

The element type

- Fields declared in interface javax.swing.text.html.parser.

DTDConstants

ANY

,

CDATA

,

CONREF

,

CURRENT

,

DEFAULT

,

EMPTY

,

ENDTAG

,

ENTITIES

,

ENTITY

,

FIXED

,

GENERAL

,

ID

,

IDREF

,

IDREFS

,

IMPLIED

,

MD

,

MODEL

,

MS

,

NAME

,

NAMES

,

NMTOKEN

,

NMTOKENS

,

NOTATION

,

NUMBER

,

NUMBERS

,

NUTOKEN

,

NUTOKENS

,

PARAMETER

,

PI

,

PUBLIC

,

RCDATA

,

REQUIRED

,

SDATA

,

STARTTAG

,

SYSTEM

---

#### Field Summary

The attributes

The content model

A field to store user data.

The set of elements that must not occur inside the element

The set of elements that can occur inside the element

The element index

The name of the element

true

if the end tag can be omitted

true

if the start tag can be omitted

The element type

Fields declared in interface javax.swing.text.html.parser.

DTDConstants

ANY

,

CDATA

,

CONREF

,

CURRENT

,

DEFAULT

,

EMPTY

,

ENDTAG

,

ENTITIES

,

ENTITY

,

FIXED

,

GENERAL

,

ID

,

IDREF

,

IDREFS

,

IMPLIED

,

MD

,

MODEL

,

MS

,

NAME

,

NAMES

,

NMTOKEN

,

NMTOKENS

,

NOTATION

,

NUMBER

,

NUMBERS

,

NUTOKEN

,

NUTOKENS

,

PARAMETER

,

PI

,

PUBLIC

,

RCDATA

,

REQUIRED

,

SDATA

,

STARTTAG

,

SYSTEM

---

#### Fields declared in interface javax.swing.text.html.parser. DTDConstants

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AttributeList

getAttribute

​(

String

name)

Get an attribute by name.

AttributeList

getAttributeByValue

​(

String

value)

Get an attribute by value.

AttributeList

getAttributes

()

Get the attributes.

ContentModel

getContent

()

Get content model

int

getIndex

()

Get index.

String

getName

()

Get the name of the element.

int

getType

()

Get type.

boolean

isEmpty

()

Check if empty

static int

name2type

​(

String

nm)

Converts

nm

to type.

boolean

omitEnd

()

Return true if the end tag can be omitted.

boolean

omitStart

()

Return true if the start tag can be omitted.

String

toString

()

Convert to a string.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Get an attribute by name.

Get an attribute by value.

Get the attributes.

Get content model

Get index.

Get the name of the element.

Get type.

Check if empty

Converts

nm

to type.

Return true if the end tag can be omitted.

Return true if the start tag can be omitted.

Convert to a string.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- index

```java
public int index
```

The element index

- name

```java
public
String
name
```

The name of the element

- oStart

```java
public boolean oStart
```

true

if the start tag can be omitted

- oEnd

```java
public boolean oEnd
```

true

if the end tag can be omitted

- inclusions

```java
public
BitSet
inclusions
```

The set of elements that can occur inside the element

- exclusions

```java
public
BitSet
exclusions
```

The set of elements that must not occur inside the element

- type

```java
public int type
```

The element type

- content

```java
public
ContentModel
content
```

The content model

- atts

```java
public
AttributeList
atts
```

The attributes

- data

```java
public
Object
data
```

A field to store user data. Mostly used to store
style sheets.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Get the name of the element.

**Returns:** the name of the element

- omitStart

```java
public boolean omitStart()
```

Return true if the start tag can be omitted.

**Returns:** true

if the start tag can be omitted

- omitEnd

```java
public boolean omitEnd()
```

Return true if the end tag can be omitted.

**Returns:** true

if the end tag can be omitted

- getType

```java
public int getType()
```

Get type.

**Returns:** the type of the element

- getContent

```java
public
ContentModel
getContent()
```

Get content model

**Returns:** the content model

- getAttributes

```java
public
AttributeList
getAttributes()
```

Get the attributes.

**Returns:** the

AttributeList

specifying the element

- getIndex

```java
public int getIndex()
```

Get index.

**Returns:** the element index

- isEmpty

```java
public boolean isEmpty()
```

Check if empty

**Returns:** true if the current element is empty

- toString

```java
public
String
toString()
```

Convert to a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation for the given

Element

instance

- getAttribute

```java
public
AttributeList
getAttribute​(
String
name)
```

Get an attribute by name.

**Parameters:** name

- the attribute name
**Returns:** the

AttributeList

for the given

name

- getAttributeByValue

```java
public
AttributeList
getAttributeByValue​(
String
value)
```

Get an attribute by value.

**Parameters:** value

- the string representation of value
**Returns:** the

AttributeList

for the given

value

- name2type

```java
public static int name2type​(
String
nm)
```

Converts

nm

to type. Returns appropriate DTDConstants
if the

nm

is equal to CDATA, RCDATA, EMPTY or ANY, 0 otherwise.

**Parameters:** nm

- a name
**Returns:** appropriate DTDConstants if the

nm

is equal to
CDATA, RCDATA, EMPTY or ANY, 0 otherwise.

Field Detail

- index

```java
public int index
```

The element index

- name

```java
public
String
name
```

The name of the element

- oStart

```java
public boolean oStart
```

true

if the start tag can be omitted

- oEnd

```java
public boolean oEnd
```

true

if the end tag can be omitted

- inclusions

```java
public
BitSet
inclusions
```

The set of elements that can occur inside the element

- exclusions

```java
public
BitSet
exclusions
```

The set of elements that must not occur inside the element

- type

```java
public int type
```

The element type

- content

```java
public
ContentModel
content
```

The content model

- atts

```java
public
AttributeList
atts
```

The attributes

- data

```java
public
Object
data
```

A field to store user data. Mostly used to store
style sheets.

---

#### Field Detail

index

```java
public int index
```

The element index

---

#### index

public int index

The element index

name

```java
public
String
name
```

The name of the element

---

#### name

public

String

name

The name of the element

oStart

```java
public boolean oStart
```

true

if the start tag can be omitted

---

#### oStart

public boolean oStart

true

if the start tag can be omitted

oEnd

```java
public boolean oEnd
```

true

if the end tag can be omitted

---

#### oEnd

public boolean oEnd

true

if the end tag can be omitted

inclusions

```java
public
BitSet
inclusions
```

The set of elements that can occur inside the element

---

#### inclusions

public

BitSet

inclusions

The set of elements that can occur inside the element

exclusions

```java
public
BitSet
exclusions
```

The set of elements that must not occur inside the element

---

#### exclusions

public

BitSet

exclusions

The set of elements that must not occur inside the element

type

```java
public int type
```

The element type

---

#### type

public int type

The element type

content

```java
public
ContentModel
content
```

The content model

---

#### content

public

ContentModel

content

The content model

atts

```java
public
AttributeList
atts
```

The attributes

---

#### atts

public

AttributeList

atts

The attributes

data

```java
public
Object
data
```

A field to store user data. Mostly used to store
style sheets.

---

#### data

public

Object

data

A field to store user data. Mostly used to store
style sheets.

Method Detail

- getName

```java
public
String
getName()
```

Get the name of the element.

**Returns:** the name of the element

- omitStart

```java
public boolean omitStart()
```

Return true if the start tag can be omitted.

**Returns:** true

if the start tag can be omitted

- omitEnd

```java
public boolean omitEnd()
```

Return true if the end tag can be omitted.

**Returns:** true

if the end tag can be omitted

- getType

```java
public int getType()
```

Get type.

**Returns:** the type of the element

- getContent

```java
public
ContentModel
getContent()
```

Get content model

**Returns:** the content model

- getAttributes

```java
public
AttributeList
getAttributes()
```

Get the attributes.

**Returns:** the

AttributeList

specifying the element

- getIndex

```java
public int getIndex()
```

Get index.

**Returns:** the element index

- isEmpty

```java
public boolean isEmpty()
```

Check if empty

**Returns:** true if the current element is empty

- toString

```java
public
String
toString()
```

Convert to a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation for the given

Element

instance

- getAttribute

```java
public
AttributeList
getAttribute​(
String
name)
```

Get an attribute by name.

**Parameters:** name

- the attribute name
**Returns:** the

AttributeList

for the given

name

- getAttributeByValue

```java
public
AttributeList
getAttributeByValue​(
String
value)
```

Get an attribute by value.

**Parameters:** value

- the string representation of value
**Returns:** the

AttributeList

for the given

value

- name2type

```java
public static int name2type​(
String
nm)
```

Converts

nm

to type. Returns appropriate DTDConstants
if the

nm

is equal to CDATA, RCDATA, EMPTY or ANY, 0 otherwise.

**Parameters:** nm

- a name
**Returns:** appropriate DTDConstants if the

nm

is equal to
CDATA, RCDATA, EMPTY or ANY, 0 otherwise.

---

#### Method Detail

getName

```java
public
String
getName()
```

Get the name of the element.

**Returns:** the name of the element

---

#### getName

public

String

getName()

Get the name of the element.

omitStart

```java
public boolean omitStart()
```

Return true if the start tag can be omitted.

**Returns:** true

if the start tag can be omitted

---

#### omitStart

public boolean omitStart()

Return true if the start tag can be omitted.

omitEnd

```java
public boolean omitEnd()
```

Return true if the end tag can be omitted.

**Returns:** true

if the end tag can be omitted

---

#### omitEnd

public boolean omitEnd()

Return true if the end tag can be omitted.

getType

```java
public int getType()
```

Get type.

**Returns:** the type of the element

---

#### getType

public int getType()

Get type.

getContent

```java
public
ContentModel
getContent()
```

Get content model

**Returns:** the content model

---

#### getContent

public

ContentModel

getContent()

Get content model

getAttributes

```java
public
AttributeList
getAttributes()
```

Get the attributes.

**Returns:** the

AttributeList

specifying the element

---

#### getAttributes

public

AttributeList

getAttributes()

Get the attributes.

getIndex

```java
public int getIndex()
```

Get index.

**Returns:** the element index

---

#### getIndex

public int getIndex()

Get index.

isEmpty

```java
public boolean isEmpty()
```

Check if empty

**Returns:** true if the current element is empty

---

#### isEmpty

public boolean isEmpty()

Check if empty

toString

```java
public
String
toString()
```

Convert to a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation for the given

Element

instance

---

#### toString

public

String

toString()

Convert to a string.

getAttribute

```java
public
AttributeList
getAttribute​(
String
name)
```

Get an attribute by name.

**Parameters:** name

- the attribute name
**Returns:** the

AttributeList

for the given

name

---

#### getAttribute

public

AttributeList

getAttribute​(

String

name)

Get an attribute by name.

getAttributeByValue

```java
public
AttributeList
getAttributeByValue​(
String
value)
```

Get an attribute by value.

**Parameters:** value

- the string representation of value
**Returns:** the

AttributeList

for the given

value

---

#### getAttributeByValue

public

AttributeList

getAttributeByValue​(

String

value)

Get an attribute by value.

name2type

```java
public static int name2type​(
String
nm)
```

Converts

nm

to type. Returns appropriate DTDConstants
if the

nm

is equal to CDATA, RCDATA, EMPTY or ANY, 0 otherwise.

**Parameters:** nm

- a name
**Returns:** appropriate DTDConstants if the

nm

is equal to
CDATA, RCDATA, EMPTY or ANY, 0 otherwise.

---

#### name2type

public static int name2type​(

String

nm)

Converts

nm

to type. Returns appropriate DTDConstants
if the

nm

is equal to CDATA, RCDATA, EMPTY or ANY, 0 otherwise.

---

