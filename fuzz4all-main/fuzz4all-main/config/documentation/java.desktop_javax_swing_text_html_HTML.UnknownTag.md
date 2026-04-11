# Class HTML.UnknownTag

**Source:** `java.desktop\javax\swing\text\html\HTML.UnknownTag.html`

### Class Description

```java
public static class
HTML.UnknownTag

extends
HTML.Tag

implements
Serializable
```

Class represents unknown HTML tag.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnknownTag​(
String
id)

Creates a new

UnknownTag

with the specified

id

.

**Parameters:**
- id

- the id of the new tag

---

### Method Details

#### public int hashCode()

Returns the hash code which corresponds to the string
for this tag.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
obj)

Compares this object to the specified object.
The result is

true

if and only if the argument is not

null

and is an

UnknownTag

object
with the same name.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to compare this tag with

**Returns:**
- true

if the objects are equal;

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

### Additional Sections

#### Class HTML.UnknownTag

java.lang.Object

- javax.swing.text.html.HTML.Tag
- - javax.swing.text.html.HTML.UnknownTag

javax.swing.text.html.HTML.Tag

- javax.swing.text.html.HTML.UnknownTag

javax.swing.text.html.HTML.UnknownTag

**All Implemented Interfaces:** Serializable

**Enclosing class:** HTML

```java
public static class
HTML.UnknownTag

extends
HTML.Tag

implements
Serializable
```

Class represents unknown HTML tag.

**See Also:** Serialized Form

public static class

HTML.UnknownTag

extends

HTML.Tag

implements

Serializable

Class represents unknown HTML tag.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.text.html.

HTML.Tag

A

,

ADDRESS

,

APPLET

,

AREA

,

B

,

BASE

,

BASEFONT

,

BIG

,

BLOCKQUOTE

,

BODY

,

BR

,

CAPTION

,

CENTER

,

CITE

,

CODE

,

COMMENT

,

CONTENT

,

DD

,

DFN

,

DIR

,

DIV

,

DL

,

DT

,

EM

,

FONT

,

FORM

,

FRAME

,

FRAMESET

,

H1

,

H2

,

H3

,

H4

,

H5

,

H6

,

HEAD

,

HR

,

HTML

,

I

,

IMG

,

IMPLIED

,

INPUT

,

ISINDEX

,

KBD

,

LI

,

LINK

,

MAP

,

MENU

,

META

,

NOFRAMES

,

OBJECT

,

OL

,

OPTION

,

P

,

PARAM

,

PRE

,

S

,

SAMP

,

SCRIPT

,

SELECT

,

SMALL

,

SPAN

,

STRIKE

,

STRONG

,

STYLE

,

SUB

,

SUP

,

TABLE

,

TD

,

TEXTAREA

,

TH

,

TITLE

,

TR

,

TT

,

U

,

UL

,

VAR

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnknownTag

​(

String

id)

Creates a new

UnknownTag

with the specified

id

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares this object to the specified object.

int

hashCode

()

Returns the hash code which corresponds to the string
for this tag.

- Methods declared in class javax.swing.text.html.

HTML.Tag

breaksFlow

,

isBlock

,

isPreformatted

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- Fields declared in class javax.swing.text.html.

HTML.Tag

A

,

ADDRESS

,

APPLET

,

AREA

,

B

,

BASE

,

BASEFONT

,

BIG

,

BLOCKQUOTE

,

BODY

,

BR

,

CAPTION

,

CENTER

,

CITE

,

CODE

,

COMMENT

,

CONTENT

,

DD

,

DFN

,

DIR

,

DIV

,

DL

,

DT

,

EM

,

FONT

,

FORM

,

FRAME

,

FRAMESET

,

H1

,

H2

,

H3

,

H4

,

H5

,

H6

,

HEAD

,

HR

,

HTML

,

I

,

IMG

,

IMPLIED

,

INPUT

,

ISINDEX

,

KBD

,

LI

,

LINK

,

MAP

,

MENU

,

META

,

NOFRAMES

,

OBJECT

,

OL

,

OPTION

,

P

,

PARAM

,

PRE

,

S

,

SAMP

,

SCRIPT

,

SELECT

,

SMALL

,

SPAN

,

STRIKE

,

STRONG

,

STYLE

,

SUB

,

SUP

,

TABLE

,

TD

,

TEXTAREA

,

TH

,

TITLE

,

TR

,

TT

,

U

,

UL

,

VAR

---

#### Field Summary

Fields declared in class javax.swing.text.html.

HTML.Tag

A

,

ADDRESS

,

APPLET

,

AREA

,

B

,

BASE

,

BASEFONT

,

BIG

,

BLOCKQUOTE

,

BODY

,

BR

,

CAPTION

,

CENTER

,

CITE

,

CODE

,

COMMENT

,

CONTENT

,

DD

,

DFN

,

DIR

,

DIV

,

DL

,

DT

,

EM

,

FONT

,

FORM

,

FRAME

,

FRAMESET

,

H1

,

H2

,

H3

,

H4

,

H5

,

H6

,

HEAD

,

HR

,

HTML

,

I

,

IMG

,

IMPLIED

,

INPUT

,

ISINDEX

,

KBD

,

LI

,

LINK

,

MAP

,

MENU

,

META

,

NOFRAMES

,

OBJECT

,

OL

,

OPTION

,

P

,

PARAM

,

PRE

,

S

,

SAMP

,

SCRIPT

,

SELECT

,

SMALL

,

SPAN

,

STRIKE

,

STRONG

,

STYLE

,

SUB

,

SUP

,

TABLE

,

TD

,

TEXTAREA

,

TH

,

TITLE

,

TR

,

TT

,

U

,

UL

,

VAR

---

#### Fields declared in class javax.swing.text.html. HTML.Tag

Constructor Summary

Constructors

Constructor

Description

UnknownTag

​(

String

id)

Creates a new

UnknownTag

with the specified

id

.

---

#### Constructor Summary

Creates a new

UnknownTag

with the specified

id

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares this object to the specified object.

int

hashCode

()

Returns the hash code which corresponds to the string
for this tag.

- Methods declared in class javax.swing.text.html.

HTML.Tag

breaksFlow

,

isBlock

,

isPreformatted

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Compares this object to the specified object.

Returns the hash code which corresponds to the string
for this tag.

Methods declared in class javax.swing.text.html.

HTML.Tag

breaksFlow

,

isBlock

,

isPreformatted

,

toString

---

#### Methods declared in class javax.swing.text.html. HTML.Tag

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- UnknownTag

```java
public UnknownTag​(
String
id)
```

Creates a new

UnknownTag

with the specified

id

.

**Parameters:** id

- the id of the new tag

============ METHOD DETAIL ==========

- Method Detail

- hashCode

```java
public int hashCode()
```

Returns the hash code which corresponds to the string
for this tag.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this object to the specified object.
The result is

true

if and only if the argument is not

null

and is an

UnknownTag

object
with the same name.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare this tag with
**Returns:** true

if the objects are equal;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- UnknownTag

```java
public UnknownTag​(
String
id)
```

Creates a new

UnknownTag

with the specified

id

.

**Parameters:** id

- the id of the new tag

---

#### Constructor Detail

UnknownTag

```java
public UnknownTag​(
String
id)
```

Creates a new

UnknownTag

with the specified

id

.

**Parameters:** id

- the id of the new tag

---

#### UnknownTag

public UnknownTag​(

String

id)

Creates a new

UnknownTag

with the specified

id

.

Method Detail

- hashCode

```java
public int hashCode()
```

Returns the hash code which corresponds to the string
for this tag.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this object to the specified object.
The result is

true

if and only if the argument is not

null

and is an

UnknownTag

object
with the same name.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare this tag with
**Returns:** true

if the objects are equal;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

hashCode

```java
public int hashCode()
```

Returns the hash code which corresponds to the string
for this tag.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code which corresponds to the string
for this tag.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this object to the specified object.
The result is

true

if and only if the argument is not

null

and is an

UnknownTag

object
with the same name.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare this tag with
**Returns:** true

if the objects are equal;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this object to the specified object.
The result is

true

if and only if the argument is not

null

and is an

UnknownTag

object
with the same name.

---

