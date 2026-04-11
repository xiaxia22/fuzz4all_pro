# Class DTD

**Source:** `java.desktop\javax\swing\text\html\parser\DTD.html`

### Class Description

```java
public class
DTD

extends
Object

implements
DTDConstants
```

The representation of an SGML DTD. DTD describes a document
syntax and is used in parsing of HTML documents. It contains
a list of elements and their attributes as well as a list of
entities defined in the DTD.

**All Implemented Interfaces:** DTDConstants

---

### Field Details

#### public
String
name

the name of the DTD

---

#### public
Vector
<
Element
> elements

The vector of elements

---

#### public
Hashtable
<
String
,​
Element
> elementHash

The hash table contains the name of element and
the corresponding element.

---

#### public
Hashtable
<
Object
,​
Entity
> entityHash

The hash table contains an

Object

and the corresponding

Entity

---

#### public final
Element
pcdata

The element corresponding to pcdata.

---

#### public final
Element
html

The element corresponding to html.

---

#### public final
Element
meta

The element corresponding to meta.

---

#### public final
Element
base

The element corresponding to base.

---

#### public final
Element
isindex

The element corresponding to isindex.

---

#### public final
Element
head

The element corresponding to head.

---

#### public final
Element
body

The element corresponding to body.

---

#### public final
Element
applet

The element corresponding to applet.

---

#### public final
Element
param

The element corresponding to param.

---

#### public final
Element
p

The element corresponding to p.

---

#### public final
Element
title

The element corresponding to title.

---

#### public static final int FILE_VERSION

The version of a file

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected DTD​(
String
name)

Creates a new DTD with the specified name.

**Parameters:**
- name

- the name, as a

String

of the new DTD

---

### Method Details

#### public
String
getName()

Gets the name of the DTD.

**Returns:**
- the name of the DTD

---

#### public
Entity
getEntity​(
String
name)

Gets an entity by name.

**Parameters:**
- name

- the entity name

**Returns:**
- the

Entity

corresponding to the

name

String

---

#### public
Entity
getEntity​(int ch)

Gets a character entity.

**Parameters:**
- ch

- the character

**Returns:**
- the

Entity

corresponding to the

ch

character

---

#### public
Element
getElement​(
String
name)

Gets an element by name. A new element is
created if the element doesn't exist.

**Parameters:**
- name

- the requested

String

**Returns:**
- the

Element

corresponding to

name

, which may be newly created

---

#### public
Element
getElement​(int index)

Gets an element by index.

**Parameters:**
- index

- the requested index

**Returns:**
- the

Element

corresponding to

index

---

#### public
Entity
defineEntity​(
String
name,
int type,
char[] data)

Defines an entity. If the

Entity

specified
by

name

,

type

, and

data

exists, it is returned; otherwise a new

Entity

is created and is returned.

**Parameters:**
- name

- the name of the

Entity

as a

String
- type

- the type of the

Entity
- data

- the

Entity

's data

**Returns:**
- the

Entity

requested or a new

Entity

if not found

---

#### public
Element
defineElement​(
String
name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel
content,

BitSet
exclusions,

BitSet
inclusions,

AttributeList
atts)

Returns the

Element

which matches the
specified parameters. If one doesn't exist, a new
one is created and returned.

**Parameters:**
- name

- the name of the

Element
- type

- the type of the

Element
- omitStart

-

true

if start should be omitted
- omitEnd

-

true

if end should be omitted
- content

- the

ContentModel
- exclusions

- the set of elements that must not occur inside the element
- inclusions

- the set of elements that can occur inside the element
- atts

- the

AttributeList

specifying the

Element

**Returns:**
- the

Element

specified

---

#### public void defineAttributes​(
String
name,

AttributeList
atts)

Defines attributes for an

Element

.

**Parameters:**
- name

- the name of the

Element
- atts

- the

AttributeList

specifying the

Element

---

#### public
Entity
defEntity​(
String
name,
int type,
int ch)

Creates and returns a character

Entity

.

**Parameters:**
- name

- the entity's name
- type

- the entity's type
- ch

- the entity's value (character)

**Returns:**
- the new character

Entity

---

#### protected
Entity
defEntity​(
String
name,
int type,

String
str)

Creates and returns an

Entity

.

**Parameters:**
- name

- the entity's name
- type

- the entity's type
- str

- the entity's data section

**Returns:**
- the new

Entity

---

#### protected
Element
defElement​(
String
name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel
content,

String
[] exclusions,

String
[] inclusions,

AttributeList
atts)

Creates and returns an

Element

.

**Parameters:**
- name

- the element's name
- type

- the element's type
- omitStart

-

true

if the element needs no starting tag
- omitEnd

-

true

if the element needs no closing tag
- content

- the element's content
- exclusions

- the elements that must be excluded from the content of the element
- inclusions

- the elements that can be included as the content of the element
- atts

- the attributes of the element

**Returns:**
- the new

Element

---

#### protected
AttributeList
defAttributeList​(
String
name,
int type,
int modifier,

String
value,

String
values,

AttributeList
atts)

Creates and returns an

AttributeList

responding to a new attribute.

**Parameters:**
- name

- the attribute's name
- type

- the attribute's type
- modifier

- the attribute's modifier
- value

- the default value of the attribute
- values

- the allowed values for the attribute (multiple values could be separated by '|')
- atts

- the previous attribute of the element; to be placed to

AttributeList.next

,
creating a linked list

**Returns:**
- the new

AttributeList

---

#### protected
ContentModel
defContentModel​(int type,

Object
obj,

ContentModel
next)

Creates and returns a new content model.

**Parameters:**
- type

- the type of the new content model
- obj

- the content of the content model
- next

- pointer to the next content model

**Returns:**
- the new

ContentModel

---

#### public
String
toString()

Returns a string representation of this DTD.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation of this DTD

---

#### public static void putDTDHash​(
String
name,

DTD
dtd)

Put a name and appropriate DTD to hashtable.

**Parameters:**
- name

- the name of the DTD
- dtd

- the DTD

---

#### public static
DTD
getDTD​(
String
name)
throws
IOException

Returns a DTD with the specified

name

. If
a DTD with that name doesn't exist, one is created
and returned. Any uppercase characters in the name
are converted to lowercase.

**Parameters:**
- name

- the name of the DTD

**Returns:**
- the DTD which corresponds to

name

**Throws:**
- IOException

- if an I/O error occurs

---

#### public void read​(
DataInputStream
in)
throws
IOException

Recreates a DTD from an archived format.

**Parameters:**
- in

- the

DataInputStream

to read from

**Throws:**
- IOException

- if an I/O error occurs

---

### Additional Sections

#### Class DTD

java.lang.Object

- javax.swing.text.html.parser.DTD

javax.swing.text.html.parser.DTD

**All Implemented Interfaces:** DTDConstants

```java
public class
DTD

extends
Object

implements
DTDConstants
```

The representation of an SGML DTD. DTD describes a document
syntax and is used in parsing of HTML documents. It contains
a list of elements and their attributes as well as a list of
entities defined in the DTD.

**See Also:** Element

,

AttributeList

,

ContentModel

,

Parser

public class

DTD

extends

Object

implements

DTDConstants

The representation of an SGML DTD. DTD describes a document
syntax and is used in parsing of HTML documents. It contains
a list of elements and their attributes as well as a list of
entities defined in the DTD.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

Element

applet

The element corresponding to applet.

Element

base

The element corresponding to base.

Element

body

The element corresponding to body.

Hashtable

<

String

,​

Element

>

elementHash

The hash table contains the name of element and
the corresponding element.

Vector

<

Element

>

elements

The vector of elements

Hashtable

<

Object

,​

Entity

>

entityHash

The hash table contains an

Object

and the corresponding

Entity

static int

FILE_VERSION

The version of a file

Element

head

The element corresponding to head.

Element

html

The element corresponding to html.

Element

isindex

The element corresponding to isindex.

Element

meta

The element corresponding to meta.

String

name

the name of the DTD

Element

p

The element corresponding to p.

Element

param

The element corresponding to param.

Element

pcdata

The element corresponding to pcdata.

Element

title

The element corresponding to title.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DTD

​(

String

name)

Creates a new DTD with the specified name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

AttributeList

defAttributeList

​(

String

name,
int type,
int modifier,

String

value,

String

values,

AttributeList

atts)

Creates and returns an

AttributeList

responding to a new attribute.

protected

ContentModel

defContentModel

​(int type,

Object

obj,

ContentModel

next)

Creates and returns a new content model.

protected

Element

defElement

​(

String

name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel

content,

String

[] exclusions,

String

[] inclusions,

AttributeList

atts)

Creates and returns an

Element

.

Entity

defEntity

​(

String

name,
int type,
int ch)

Creates and returns a character

Entity

.

protected

Entity

defEntity

​(

String

name,
int type,

String

str)

Creates and returns an

Entity

.

void

defineAttributes

​(

String

name,

AttributeList

atts)

Defines attributes for an

Element

.

Element

defineElement

​(

String

name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel

content,

BitSet

exclusions,

BitSet

inclusions,

AttributeList

atts)

Returns the

Element

which matches the
specified parameters.

Entity

defineEntity

​(

String

name,
int type,
char[] data)

Defines an entity.

static

DTD

getDTD

​(

String

name)

Returns a DTD with the specified

name

.

Element

getElement

​(int index)

Gets an element by index.

Element

getElement

​(

String

name)

Gets an element by name.

Entity

getEntity

​(int ch)

Gets a character entity.

Entity

getEntity

​(

String

name)

Gets an entity by name.

String

getName

()

Gets the name of the DTD.

static void

putDTDHash

​(

String

name,

DTD

dtd)

Put a name and appropriate DTD to hashtable.

void

read

​(

DataInputStream

in)

Recreates a DTD from an archived format.

String

toString

()

Returns a string representation of this DTD.

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

Element

applet

The element corresponding to applet.

Element

base

The element corresponding to base.

Element

body

The element corresponding to body.

Hashtable

<

String

,​

Element

>

elementHash

The hash table contains the name of element and
the corresponding element.

Vector

<

Element

>

elements

The vector of elements

Hashtable

<

Object

,​

Entity

>

entityHash

The hash table contains an

Object

and the corresponding

Entity

static int

FILE_VERSION

The version of a file

Element

head

The element corresponding to head.

Element

html

The element corresponding to html.

Element

isindex

The element corresponding to isindex.

Element

meta

The element corresponding to meta.

String

name

the name of the DTD

Element

p

The element corresponding to p.

Element

param

The element corresponding to param.

Element

pcdata

The element corresponding to pcdata.

Element

title

The element corresponding to title.

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

The element corresponding to applet.

The element corresponding to base.

The element corresponding to body.

The hash table contains the name of element and
the corresponding element.

The vector of elements

The hash table contains an

Object

and the corresponding

Entity

The version of a file

The element corresponding to head.

The element corresponding to html.

The element corresponding to isindex.

The element corresponding to meta.

the name of the DTD

The element corresponding to p.

The element corresponding to param.

The element corresponding to pcdata.

The element corresponding to title.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DTD

​(

String

name)

Creates a new DTD with the specified name.

---

#### Constructor Summary

Creates a new DTD with the specified name.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

AttributeList

defAttributeList

​(

String

name,
int type,
int modifier,

String

value,

String

values,

AttributeList

atts)

Creates and returns an

AttributeList

responding to a new attribute.

protected

ContentModel

defContentModel

​(int type,

Object

obj,

ContentModel

next)

Creates and returns a new content model.

protected

Element

defElement

​(

String

name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel

content,

String

[] exclusions,

String

[] inclusions,

AttributeList

atts)

Creates and returns an

Element

.

Entity

defEntity

​(

String

name,
int type,
int ch)

Creates and returns a character

Entity

.

protected

Entity

defEntity

​(

String

name,
int type,

String

str)

Creates and returns an

Entity

.

void

defineAttributes

​(

String

name,

AttributeList

atts)

Defines attributes for an

Element

.

Element

defineElement

​(

String

name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel

content,

BitSet

exclusions,

BitSet

inclusions,

AttributeList

atts)

Returns the

Element

which matches the
specified parameters.

Entity

defineEntity

​(

String

name,
int type,
char[] data)

Defines an entity.

static

DTD

getDTD

​(

String

name)

Returns a DTD with the specified

name

.

Element

getElement

​(int index)

Gets an element by index.

Element

getElement

​(

String

name)

Gets an element by name.

Entity

getEntity

​(int ch)

Gets a character entity.

Entity

getEntity

​(

String

name)

Gets an entity by name.

String

getName

()

Gets the name of the DTD.

static void

putDTDHash

​(

String

name,

DTD

dtd)

Put a name and appropriate DTD to hashtable.

void

read

​(

DataInputStream

in)

Recreates a DTD from an archived format.

String

toString

()

Returns a string representation of this DTD.

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

Creates and returns an

AttributeList

responding to a new attribute.

Creates and returns a new content model.

Creates and returns an

Element

.

Creates and returns a character

Entity

.

Creates and returns an

Entity

.

Defines attributes for an

Element

.

Returns the

Element

which matches the
specified parameters.

Defines an entity.

Returns a DTD with the specified

name

.

Gets an element by index.

Gets an element by name.

Gets a character entity.

Gets an entity by name.

Gets the name of the DTD.

Put a name and appropriate DTD to hashtable.

Recreates a DTD from an archived format.

Returns a string representation of this DTD.

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

- name

```java
public
String
name
```

the name of the DTD

- elements

```java
public
Vector
<
Element
> elements
```

The vector of elements

- elementHash

```java
public
Hashtable
<
String
,​
Element
> elementHash
```

The hash table contains the name of element and
the corresponding element.

- entityHash

```java
public
Hashtable
<
Object
,​
Entity
> entityHash
```

The hash table contains an

Object

and the corresponding

Entity

- pcdata

```java
public final
Element
pcdata
```

The element corresponding to pcdata.

- html

```java
public final
Element
html
```

The element corresponding to html.

- meta

```java
public final
Element
meta
```

The element corresponding to meta.

- base

```java
public final
Element
base
```

The element corresponding to base.

- isindex

```java
public final
Element
isindex
```

The element corresponding to isindex.

- head

```java
public final
Element
head
```

The element corresponding to head.

- body

```java
public final
Element
body
```

The element corresponding to body.

- applet

```java
public final
Element
applet
```

The element corresponding to applet.

- param

```java
public final
Element
param
```

The element corresponding to param.

- p

```java
public final
Element
p
```

The element corresponding to p.

- title

```java
public final
Element
title
```

The element corresponding to title.

- FILE_VERSION

```java
public static final int FILE_VERSION
```

The version of a file

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DTD

```java
protected DTD​(
String
name)
```

Creates a new DTD with the specified name.

**Parameters:** name

- the name, as a

String

of the new DTD

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Gets the name of the DTD.

**Returns:** the name of the DTD

- getEntity

```java
public
Entity
getEntity​(
String
name)
```

Gets an entity by name.

**Parameters:** name

- the entity name
**Returns:** the

Entity

corresponding to the

name

String

- getEntity

```java
public
Entity
getEntity​(int ch)
```

Gets a character entity.

**Parameters:** ch

- the character
**Returns:** the

Entity

corresponding to the

ch

character

- getElement

```java
public
Element
getElement​(
String
name)
```

Gets an element by name. A new element is
created if the element doesn't exist.

**Parameters:** name

- the requested

String
**Returns:** the

Element

corresponding to

name

, which may be newly created

- getElement

```java
public
Element
getElement​(int index)
```

Gets an element by index.

**Parameters:** index

- the requested index
**Returns:** the

Element

corresponding to

index

- defineEntity

```java
public
Entity
defineEntity​(
String
name,
int type,
char[] data)
```

Defines an entity. If the

Entity

specified
by

name

,

type

, and

data

exists, it is returned; otherwise a new

Entity

is created and is returned.

**Parameters:** name

- the name of the

Entity

as a

String
**Parameters:** type

- the type of the

Entity
**Parameters:** data

- the

Entity

's data
**Returns:** the

Entity

requested or a new

Entity

if not found

- defineElement

```java
public
Element
defineElement​(
String
name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel
content,

BitSet
exclusions,

BitSet
inclusions,

AttributeList
atts)
```

Returns the

Element

which matches the
specified parameters. If one doesn't exist, a new
one is created and returned.

**Parameters:** name

- the name of the

Element
**Parameters:** type

- the type of the

Element
**Parameters:** omitStart

-

true

if start should be omitted
**Parameters:** omitEnd

-

true

if end should be omitted
**Parameters:** content

- the

ContentModel
**Parameters:** exclusions

- the set of elements that must not occur inside the element
**Parameters:** inclusions

- the set of elements that can occur inside the element
**Parameters:** atts

- the

AttributeList

specifying the

Element
**Returns:** the

Element

specified

- defineAttributes

```java
public void defineAttributes​(
String
name,

AttributeList
atts)
```

Defines attributes for an

Element

.

**Parameters:** name

- the name of the

Element
**Parameters:** atts

- the

AttributeList

specifying the

Element

- defEntity

```java
public
Entity
defEntity​(
String
name,
int type,
int ch)
```

Creates and returns a character

Entity

.

**Parameters:** name

- the entity's name
**Parameters:** type

- the entity's type
**Parameters:** ch

- the entity's value (character)
**Returns:** the new character

Entity

- defEntity

```java
protected
Entity
defEntity​(
String
name,
int type,

String
str)
```

Creates and returns an

Entity

.

**Parameters:** name

- the entity's name
**Parameters:** type

- the entity's type
**Parameters:** str

- the entity's data section
**Returns:** the new

Entity

- defElement

```java
protected
Element
defElement​(
String
name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel
content,

String
[] exclusions,

String
[] inclusions,

AttributeList
atts)
```

Creates and returns an

Element

.

**Parameters:** name

- the element's name
**Parameters:** type

- the element's type
**Parameters:** omitStart

-

true

if the element needs no starting tag
**Parameters:** omitEnd

-

true

if the element needs no closing tag
**Parameters:** content

- the element's content
**Parameters:** exclusions

- the elements that must be excluded from the content of the element
**Parameters:** inclusions

- the elements that can be included as the content of the element
**Parameters:** atts

- the attributes of the element
**Returns:** the new

Element

- defAttributeList

```java
protected
AttributeList
defAttributeList​(
String
name,
int type,
int modifier,

String
value,

String
values,

AttributeList
atts)
```

Creates and returns an

AttributeList

responding to a new attribute.

**Parameters:** name

- the attribute's name
**Parameters:** type

- the attribute's type
**Parameters:** modifier

- the attribute's modifier
**Parameters:** value

- the default value of the attribute
**Parameters:** values

- the allowed values for the attribute (multiple values could be separated by '|')
**Parameters:** atts

- the previous attribute of the element; to be placed to

AttributeList.next

,
creating a linked list
**Returns:** the new

AttributeList

- defContentModel

```java
protected
ContentModel
defContentModel​(int type,

Object
obj,

ContentModel
next)
```

Creates and returns a new content model.

**Parameters:** type

- the type of the new content model
**Parameters:** obj

- the content of the content model
**Parameters:** next

- pointer to the next content model
**Returns:** the new

ContentModel

- toString

```java
public
String
toString()
```

Returns a string representation of this DTD.

**Overrides:** toString

in class

Object
**Returns:** the string representation of this DTD

- putDTDHash

```java
public static void putDTDHash​(
String
name,

DTD
dtd)
```

Put a name and appropriate DTD to hashtable.

**Parameters:** name

- the name of the DTD
**Parameters:** dtd

- the DTD

- getDTD

```java
public static
DTD
getDTD​(
String
name)
throws
IOException
```

Returns a DTD with the specified

name

. If
a DTD with that name doesn't exist, one is created
and returned. Any uppercase characters in the name
are converted to lowercase.

**Parameters:** name

- the name of the DTD
**Returns:** the DTD which corresponds to

name
**Throws:** IOException

- if an I/O error occurs

- read

```java
public void read​(
DataInputStream
in)
throws
IOException
```

Recreates a DTD from an archived format.

**Parameters:** in

- the

DataInputStream

to read from
**Throws:** IOException

- if an I/O error occurs

Field Detail

- name

```java
public
String
name
```

the name of the DTD

- elements

```java
public
Vector
<
Element
> elements
```

The vector of elements

- elementHash

```java
public
Hashtable
<
String
,​
Element
> elementHash
```

The hash table contains the name of element and
the corresponding element.

- entityHash

```java
public
Hashtable
<
Object
,​
Entity
> entityHash
```

The hash table contains an

Object

and the corresponding

Entity

- pcdata

```java
public final
Element
pcdata
```

The element corresponding to pcdata.

- html

```java
public final
Element
html
```

The element corresponding to html.

- meta

```java
public final
Element
meta
```

The element corresponding to meta.

- base

```java
public final
Element
base
```

The element corresponding to base.

- isindex

```java
public final
Element
isindex
```

The element corresponding to isindex.

- head

```java
public final
Element
head
```

The element corresponding to head.

- body

```java
public final
Element
body
```

The element corresponding to body.

- applet

```java
public final
Element
applet
```

The element corresponding to applet.

- param

```java
public final
Element
param
```

The element corresponding to param.

- p

```java
public final
Element
p
```

The element corresponding to p.

- title

```java
public final
Element
title
```

The element corresponding to title.

- FILE_VERSION

```java
public static final int FILE_VERSION
```

The version of a file

**See Also:** Constant Field Values

---

#### Field Detail

name

```java
public
String
name
```

the name of the DTD

---

#### name

public

String

name

the name of the DTD

elements

```java
public
Vector
<
Element
> elements
```

The vector of elements

---

#### elements

public

Vector

<

Element

> elements

The vector of elements

elementHash

```java
public
Hashtable
<
String
,​
Element
> elementHash
```

The hash table contains the name of element and
the corresponding element.

---

#### elementHash

public

Hashtable

<

String

,​

Element

> elementHash

The hash table contains the name of element and
the corresponding element.

entityHash

```java
public
Hashtable
<
Object
,​
Entity
> entityHash
```

The hash table contains an

Object

and the corresponding

Entity

---

#### entityHash

public

Hashtable

<

Object

,​

Entity

> entityHash

The hash table contains an

Object

and the corresponding

Entity

pcdata

```java
public final
Element
pcdata
```

The element corresponding to pcdata.

---

#### pcdata

public final

Element

pcdata

The element corresponding to pcdata.

html

```java
public final
Element
html
```

The element corresponding to html.

---

#### html

public final

Element

html

The element corresponding to html.

meta

```java
public final
Element
meta
```

The element corresponding to meta.

---

#### meta

public final

Element

meta

The element corresponding to meta.

base

```java
public final
Element
base
```

The element corresponding to base.

---

#### base

public final

Element

base

The element corresponding to base.

isindex

```java
public final
Element
isindex
```

The element corresponding to isindex.

---

#### isindex

public final

Element

isindex

The element corresponding to isindex.

head

```java
public final
Element
head
```

The element corresponding to head.

---

#### head

public final

Element

head

The element corresponding to head.

body

```java
public final
Element
body
```

The element corresponding to body.

---

#### body

public final

Element

body

The element corresponding to body.

applet

```java
public final
Element
applet
```

The element corresponding to applet.

---

#### applet

public final

Element

applet

The element corresponding to applet.

param

```java
public final
Element
param
```

The element corresponding to param.

---

#### param

public final

Element

param

The element corresponding to param.

p

```java
public final
Element
p
```

The element corresponding to p.

---

#### p

public final

Element

p

The element corresponding to p.

title

```java
public final
Element
title
```

The element corresponding to title.

---

#### title

public final

Element

title

The element corresponding to title.

FILE_VERSION

```java
public static final int FILE_VERSION
```

The version of a file

**See Also:** Constant Field Values

---

#### FILE_VERSION

public static final int FILE_VERSION

The version of a file

Constructor Detail

- DTD

```java
protected DTD​(
String
name)
```

Creates a new DTD with the specified name.

**Parameters:** name

- the name, as a

String

of the new DTD

---

#### Constructor Detail

DTD

```java
protected DTD​(
String
name)
```

Creates a new DTD with the specified name.

**Parameters:** name

- the name, as a

String

of the new DTD

---

#### DTD

protected DTD​(

String

name)

Creates a new DTD with the specified name.

Method Detail

- getName

```java
public
String
getName()
```

Gets the name of the DTD.

**Returns:** the name of the DTD

- getEntity

```java
public
Entity
getEntity​(
String
name)
```

Gets an entity by name.

**Parameters:** name

- the entity name
**Returns:** the

Entity

corresponding to the

name

String

- getEntity

```java
public
Entity
getEntity​(int ch)
```

Gets a character entity.

**Parameters:** ch

- the character
**Returns:** the

Entity

corresponding to the

ch

character

- getElement

```java
public
Element
getElement​(
String
name)
```

Gets an element by name. A new element is
created if the element doesn't exist.

**Parameters:** name

- the requested

String
**Returns:** the

Element

corresponding to

name

, which may be newly created

- getElement

```java
public
Element
getElement​(int index)
```

Gets an element by index.

**Parameters:** index

- the requested index
**Returns:** the

Element

corresponding to

index

- defineEntity

```java
public
Entity
defineEntity​(
String
name,
int type,
char[] data)
```

Defines an entity. If the

Entity

specified
by

name

,

type

, and

data

exists, it is returned; otherwise a new

Entity

is created and is returned.

**Parameters:** name

- the name of the

Entity

as a

String
**Parameters:** type

- the type of the

Entity
**Parameters:** data

- the

Entity

's data
**Returns:** the

Entity

requested or a new

Entity

if not found

- defineElement

```java
public
Element
defineElement​(
String
name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel
content,

BitSet
exclusions,

BitSet
inclusions,

AttributeList
atts)
```

Returns the

Element

which matches the
specified parameters. If one doesn't exist, a new
one is created and returned.

**Parameters:** name

- the name of the

Element
**Parameters:** type

- the type of the

Element
**Parameters:** omitStart

-

true

if start should be omitted
**Parameters:** omitEnd

-

true

if end should be omitted
**Parameters:** content

- the

ContentModel
**Parameters:** exclusions

- the set of elements that must not occur inside the element
**Parameters:** inclusions

- the set of elements that can occur inside the element
**Parameters:** atts

- the

AttributeList

specifying the

Element
**Returns:** the

Element

specified

- defineAttributes

```java
public void defineAttributes​(
String
name,

AttributeList
atts)
```

Defines attributes for an

Element

.

**Parameters:** name

- the name of the

Element
**Parameters:** atts

- the

AttributeList

specifying the

Element

- defEntity

```java
public
Entity
defEntity​(
String
name,
int type,
int ch)
```

Creates and returns a character

Entity

.

**Parameters:** name

- the entity's name
**Parameters:** type

- the entity's type
**Parameters:** ch

- the entity's value (character)
**Returns:** the new character

Entity

- defEntity

```java
protected
Entity
defEntity​(
String
name,
int type,

String
str)
```

Creates and returns an

Entity

.

**Parameters:** name

- the entity's name
**Parameters:** type

- the entity's type
**Parameters:** str

- the entity's data section
**Returns:** the new

Entity

- defElement

```java
protected
Element
defElement​(
String
name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel
content,

String
[] exclusions,

String
[] inclusions,

AttributeList
atts)
```

Creates and returns an

Element

.

**Parameters:** name

- the element's name
**Parameters:** type

- the element's type
**Parameters:** omitStart

-

true

if the element needs no starting tag
**Parameters:** omitEnd

-

true

if the element needs no closing tag
**Parameters:** content

- the element's content
**Parameters:** exclusions

- the elements that must be excluded from the content of the element
**Parameters:** inclusions

- the elements that can be included as the content of the element
**Parameters:** atts

- the attributes of the element
**Returns:** the new

Element

- defAttributeList

```java
protected
AttributeList
defAttributeList​(
String
name,
int type,
int modifier,

String
value,

String
values,

AttributeList
atts)
```

Creates and returns an

AttributeList

responding to a new attribute.

**Parameters:** name

- the attribute's name
**Parameters:** type

- the attribute's type
**Parameters:** modifier

- the attribute's modifier
**Parameters:** value

- the default value of the attribute
**Parameters:** values

- the allowed values for the attribute (multiple values could be separated by '|')
**Parameters:** atts

- the previous attribute of the element; to be placed to

AttributeList.next

,
creating a linked list
**Returns:** the new

AttributeList

- defContentModel

```java
protected
ContentModel
defContentModel​(int type,

Object
obj,

ContentModel
next)
```

Creates and returns a new content model.

**Parameters:** type

- the type of the new content model
**Parameters:** obj

- the content of the content model
**Parameters:** next

- pointer to the next content model
**Returns:** the new

ContentModel

- toString

```java
public
String
toString()
```

Returns a string representation of this DTD.

**Overrides:** toString

in class

Object
**Returns:** the string representation of this DTD

- putDTDHash

```java
public static void putDTDHash​(
String
name,

DTD
dtd)
```

Put a name and appropriate DTD to hashtable.

**Parameters:** name

- the name of the DTD
**Parameters:** dtd

- the DTD

- getDTD

```java
public static
DTD
getDTD​(
String
name)
throws
IOException
```

Returns a DTD with the specified

name

. If
a DTD with that name doesn't exist, one is created
and returned. Any uppercase characters in the name
are converted to lowercase.

**Parameters:** name

- the name of the DTD
**Returns:** the DTD which corresponds to

name
**Throws:** IOException

- if an I/O error occurs

- read

```java
public void read​(
DataInputStream
in)
throws
IOException
```

Recreates a DTD from an archived format.

**Parameters:** in

- the

DataInputStream

to read from
**Throws:** IOException

- if an I/O error occurs

---

#### Method Detail

getName

```java
public
String
getName()
```

Gets the name of the DTD.

**Returns:** the name of the DTD

---

#### getName

public

String

getName()

Gets the name of the DTD.

getEntity

```java
public
Entity
getEntity​(
String
name)
```

Gets an entity by name.

**Parameters:** name

- the entity name
**Returns:** the

Entity

corresponding to the

name

String

---

#### getEntity

public

Entity

getEntity​(

String

name)

Gets an entity by name.

getEntity

```java
public
Entity
getEntity​(int ch)
```

Gets a character entity.

**Parameters:** ch

- the character
**Returns:** the

Entity

corresponding to the

ch

character

---

#### getEntity

public

Entity

getEntity​(int ch)

Gets a character entity.

getElement

```java
public
Element
getElement​(
String
name)
```

Gets an element by name. A new element is
created if the element doesn't exist.

**Parameters:** name

- the requested

String
**Returns:** the

Element

corresponding to

name

, which may be newly created

---

#### getElement

public

Element

getElement​(

String

name)

Gets an element by name. A new element is
created if the element doesn't exist.

getElement

```java
public
Element
getElement​(int index)
```

Gets an element by index.

**Parameters:** index

- the requested index
**Returns:** the

Element

corresponding to

index

---

#### getElement

public

Element

getElement​(int index)

Gets an element by index.

defineEntity

```java
public
Entity
defineEntity​(
String
name,
int type,
char[] data)
```

Defines an entity. If the

Entity

specified
by

name

,

type

, and

data

exists, it is returned; otherwise a new

Entity

is created and is returned.

**Parameters:** name

- the name of the

Entity

as a

String
**Parameters:** type

- the type of the

Entity
**Parameters:** data

- the

Entity

's data
**Returns:** the

Entity

requested or a new

Entity

if not found

---

#### defineEntity

public

Entity

defineEntity​(

String

name,
int type,
char[] data)

Defines an entity. If the

Entity

specified
by

name

,

type

, and

data

exists, it is returned; otherwise a new

Entity

is created and is returned.

defineElement

```java
public
Element
defineElement​(
String
name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel
content,

BitSet
exclusions,

BitSet
inclusions,

AttributeList
atts)
```

Returns the

Element

which matches the
specified parameters. If one doesn't exist, a new
one is created and returned.

**Parameters:** name

- the name of the

Element
**Parameters:** type

- the type of the

Element
**Parameters:** omitStart

-

true

if start should be omitted
**Parameters:** omitEnd

-

true

if end should be omitted
**Parameters:** content

- the

ContentModel
**Parameters:** exclusions

- the set of elements that must not occur inside the element
**Parameters:** inclusions

- the set of elements that can occur inside the element
**Parameters:** atts

- the

AttributeList

specifying the

Element
**Returns:** the

Element

specified

---

#### defineElement

public

Element

defineElement​(

String

name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel

content,

BitSet

exclusions,

BitSet

inclusions,

AttributeList

atts)

Returns the

Element

which matches the
specified parameters. If one doesn't exist, a new
one is created and returned.

defineAttributes

```java
public void defineAttributes​(
String
name,

AttributeList
atts)
```

Defines attributes for an

Element

.

**Parameters:** name

- the name of the

Element
**Parameters:** atts

- the

AttributeList

specifying the

Element

---

#### defineAttributes

public void defineAttributes​(

String

name,

AttributeList

atts)

Defines attributes for an

Element

.

defEntity

```java
public
Entity
defEntity​(
String
name,
int type,
int ch)
```

Creates and returns a character

Entity

.

**Parameters:** name

- the entity's name
**Parameters:** type

- the entity's type
**Parameters:** ch

- the entity's value (character)
**Returns:** the new character

Entity

---

#### defEntity

public

Entity

defEntity​(

String

name,
int type,
int ch)

Creates and returns a character

Entity

.

defEntity

```java
protected
Entity
defEntity​(
String
name,
int type,

String
str)
```

Creates and returns an

Entity

.

**Parameters:** name

- the entity's name
**Parameters:** type

- the entity's type
**Parameters:** str

- the entity's data section
**Returns:** the new

Entity

---

#### defEntity

protected

Entity

defEntity​(

String

name,
int type,

String

str)

Creates and returns an

Entity

.

defElement

```java
protected
Element
defElement​(
String
name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel
content,

String
[] exclusions,

String
[] inclusions,

AttributeList
atts)
```

Creates and returns an

Element

.

**Parameters:** name

- the element's name
**Parameters:** type

- the element's type
**Parameters:** omitStart

-

true

if the element needs no starting tag
**Parameters:** omitEnd

-

true

if the element needs no closing tag
**Parameters:** content

- the element's content
**Parameters:** exclusions

- the elements that must be excluded from the content of the element
**Parameters:** inclusions

- the elements that can be included as the content of the element
**Parameters:** atts

- the attributes of the element
**Returns:** the new

Element

---

#### defElement

protected

Element

defElement​(

String

name,
int type,
boolean omitStart,
boolean omitEnd,

ContentModel

content,

String

[] exclusions,

String

[] inclusions,

AttributeList

atts)

Creates and returns an

Element

.

defAttributeList

```java
protected
AttributeList
defAttributeList​(
String
name,
int type,
int modifier,

String
value,

String
values,

AttributeList
atts)
```

Creates and returns an

AttributeList

responding to a new attribute.

**Parameters:** name

- the attribute's name
**Parameters:** type

- the attribute's type
**Parameters:** modifier

- the attribute's modifier
**Parameters:** value

- the default value of the attribute
**Parameters:** values

- the allowed values for the attribute (multiple values could be separated by '|')
**Parameters:** atts

- the previous attribute of the element; to be placed to

AttributeList.next

,
creating a linked list
**Returns:** the new

AttributeList

---

#### defAttributeList

protected

AttributeList

defAttributeList​(

String

name,
int type,
int modifier,

String

value,

String

values,

AttributeList

atts)

Creates and returns an

AttributeList

responding to a new attribute.

defContentModel

```java
protected
ContentModel
defContentModel​(int type,

Object
obj,

ContentModel
next)
```

Creates and returns a new content model.

**Parameters:** type

- the type of the new content model
**Parameters:** obj

- the content of the content model
**Parameters:** next

- pointer to the next content model
**Returns:** the new

ContentModel

---

#### defContentModel

protected

ContentModel

defContentModel​(int type,

Object

obj,

ContentModel

next)

Creates and returns a new content model.

toString

```java
public
String
toString()
```

Returns a string representation of this DTD.

**Overrides:** toString

in class

Object
**Returns:** the string representation of this DTD

---

#### toString

public

String

toString()

Returns a string representation of this DTD.

putDTDHash

```java
public static void putDTDHash​(
String
name,

DTD
dtd)
```

Put a name and appropriate DTD to hashtable.

**Parameters:** name

- the name of the DTD
**Parameters:** dtd

- the DTD

---

#### putDTDHash

public static void putDTDHash​(

String

name,

DTD

dtd)

Put a name and appropriate DTD to hashtable.

getDTD

```java
public static
DTD
getDTD​(
String
name)
throws
IOException
```

Returns a DTD with the specified

name

. If
a DTD with that name doesn't exist, one is created
and returned. Any uppercase characters in the name
are converted to lowercase.

**Parameters:** name

- the name of the DTD
**Returns:** the DTD which corresponds to

name
**Throws:** IOException

- if an I/O error occurs

---

#### getDTD

public static

DTD

getDTD​(

String

name)
throws

IOException

Returns a DTD with the specified

name

. If
a DTD with that name doesn't exist, one is created
and returned. Any uppercase characters in the name
are converted to lowercase.

read

```java
public void read​(
DataInputStream
in)
throws
IOException
```

Recreates a DTD from an archived format.

**Parameters:** in

- the

DataInputStream

to read from
**Throws:** IOException

- if an I/O error occurs

---

#### read

public void read​(

DataInputStream

in)
throws

IOException

Recreates a DTD from an archived format.

---

