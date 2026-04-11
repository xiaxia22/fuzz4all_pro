# Class ContentModel

**Source:** `java.desktop\javax\swing\text\html\parser\ContentModel.html`

### Class Description

```java
public final class
ContentModel

extends
Object

implements
Serializable
```

A representation of a content model. A content model is
basically a restricted BNF expression. It is restricted in
the sense that it must be deterministic. This means that you
don't have to represent it as a finite state automaton.

See Annex H on page 556 of the SGML handbook for more information.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public int type

Type. Either '*', '?', '+', ',', '|', '&'.

---

#### public
Object
content

The content. Either an Element or a ContentModel.

---

#### public
ContentModel
next

The next content model (in a ',', '|' or '&' expression).

---

### Constructor Details

#### public ContentModel()

Creates

ContentModel

---

#### public ContentModel​(
Element
content)

Create a content model for an element.

**Parameters:**
- content

- the element

---

#### public ContentModel​(int type,

ContentModel
content)

Create a content model of a particular type.

**Parameters:**
- type

- the type
- content

- the content

---

#### public ContentModel​(int type,

Object
content,

ContentModel
next)

Create a content model of a particular type.

**Parameters:**
- type

- the type
- content

- the content
- next

- the next content model

---

### Method Details

#### public boolean empty()

Return true if the content model could
match an empty input stream.

**Returns:**
- true

if the content model could
match an empty input stream

---

#### public void getElements​(
Vector
<
Element
> elemVec)

Update elemVec with the list of elements that are
part of the this contentModel.

**Parameters:**
- elemVec

- the list of elements

---

#### public boolean first​(
Object
token)

Return true if the token could potentially be the
first token in the input stream.

**Parameters:**
- token

- the token

**Returns:**
- true

if the token could potentially be the first token
in the input stream

---

#### public
Element
first()

Return the element that must be next.

**Returns:**
- the element that must be next

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
- the string representation of this

ContentModel

---

### Additional Sections

#### Class ContentModel

java.lang.Object

- javax.swing.text.html.parser.ContentModel

javax.swing.text.html.parser.ContentModel

**All Implemented Interfaces:** Serializable

```java
public final class
ContentModel

extends
Object

implements
Serializable
```

A representation of a content model. A content model is
basically a restricted BNF expression. It is restricted in
the sense that it must be deterministic. This means that you
don't have to represent it as a finite state automaton.

See Annex H on page 556 of the SGML handbook for more information.

**See Also:** Serialized Form

public final class

ContentModel

extends

Object

implements

Serializable

A representation of a content model. A content model is
basically a restricted BNF expression. It is restricted in
the sense that it must be deterministic. This means that you
don't have to represent it as a finite state automaton.

See Annex H on page 556 of the SGML handbook for more information.

See Annex H on page 556 of the SGML handbook for more information.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

Object

content

The content.

ContentModel

next

The next content model (in a ',', '|' or '&' expression).

int

type

Type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ContentModel

()

Creates

ContentModel

ContentModel

​(int type,

Object

content,

ContentModel

next)

Create a content model of a particular type.

ContentModel

​(int type,

ContentModel

content)

Create a content model of a particular type.

ContentModel

​(

Element

content)

Create a content model for an element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

empty

()

Return true if the content model could
match an empty input stream.

Element

first

()

Return the element that must be next.

boolean

first

​(

Object

token)

Return true if the token could potentially be the
first token in the input stream.

void

getElements

​(

Vector

<

Element

> elemVec)

Update elemVec with the list of elements that are
part of the this contentModel.

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

Object

content

The content.

ContentModel

next

The next content model (in a ',', '|' or '&' expression).

int

type

Type.

---

#### Field Summary

The content.

The next content model (in a ',', '|' or '&' expression).

Type.

Constructor Summary

Constructors

Constructor

Description

ContentModel

()

Creates

ContentModel

ContentModel

​(int type,

Object

content,

ContentModel

next)

Create a content model of a particular type.

ContentModel

​(int type,

ContentModel

content)

Create a content model of a particular type.

ContentModel

​(

Element

content)

Create a content model for an element.

---

#### Constructor Summary

Creates

ContentModel

Create a content model of a particular type.

Create a content model for an element.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

empty

()

Return true if the content model could
match an empty input stream.

Element

first

()

Return the element that must be next.

boolean

first

​(

Object

token)

Return true if the token could potentially be the
first token in the input stream.

void

getElements

​(

Vector

<

Element

> elemVec)

Update elemVec with the list of elements that are
part of the this contentModel.

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

Return true if the content model could
match an empty input stream.

Return the element that must be next.

Return true if the token could potentially be the
first token in the input stream.

Update elemVec with the list of elements that are
part of the this contentModel.

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

- type

```java
public int type
```

Type. Either '*', '?', '+', ',', '|', '&'.

- content

```java
public
Object
content
```

The content. Either an Element or a ContentModel.

- next

```java
public
ContentModel
next
```

The next content model (in a ',', '|' or '&' expression).

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ContentModel

```java
public ContentModel()
```

Creates

ContentModel

- ContentModel

```java
public ContentModel​(
Element
content)
```

Create a content model for an element.

**Parameters:** content

- the element

- ContentModel

```java
public ContentModel​(int type,

ContentModel
content)
```

Create a content model of a particular type.

**Parameters:** type

- the type
**Parameters:** content

- the content

- ContentModel

```java
public ContentModel​(int type,

Object
content,

ContentModel
next)
```

Create a content model of a particular type.

**Parameters:** type

- the type
**Parameters:** content

- the content
**Parameters:** next

- the next content model

============ METHOD DETAIL ==========

- Method Detail

- empty

```java
public boolean empty()
```

Return true if the content model could
match an empty input stream.

**Returns:** true

if the content model could
match an empty input stream

- getElements

```java
public void getElements​(
Vector
<
Element
> elemVec)
```

Update elemVec with the list of elements that are
part of the this contentModel.

**Parameters:** elemVec

- the list of elements

- first

```java
public boolean first​(
Object
token)
```

Return true if the token could potentially be the
first token in the input stream.

**Parameters:** token

- the token
**Returns:** true

if the token could potentially be the first token
in the input stream

- first

```java
public
Element
first()
```

Return the element that must be next.

**Returns:** the element that must be next

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
**Returns:** the string representation of this

ContentModel

Field Detail

- type

```java
public int type
```

Type. Either '*', '?', '+', ',', '|', '&'.

- content

```java
public
Object
content
```

The content. Either an Element or a ContentModel.

- next

```java
public
ContentModel
next
```

The next content model (in a ',', '|' or '&' expression).

---

#### Field Detail

type

```java
public int type
```

Type. Either '*', '?', '+', ',', '|', '&'.

---

#### type

public int type

Type. Either '*', '?', '+', ',', '|', '&'.

content

```java
public
Object
content
```

The content. Either an Element or a ContentModel.

---

#### content

public

Object

content

The content. Either an Element or a ContentModel.

next

```java
public
ContentModel
next
```

The next content model (in a ',', '|' or '&' expression).

---

#### next

public

ContentModel

next

The next content model (in a ',', '|' or '&' expression).

Constructor Detail

- ContentModel

```java
public ContentModel()
```

Creates

ContentModel

- ContentModel

```java
public ContentModel​(
Element
content)
```

Create a content model for an element.

**Parameters:** content

- the element

- ContentModel

```java
public ContentModel​(int type,

ContentModel
content)
```

Create a content model of a particular type.

**Parameters:** type

- the type
**Parameters:** content

- the content

- ContentModel

```java
public ContentModel​(int type,

Object
content,

ContentModel
next)
```

Create a content model of a particular type.

**Parameters:** type

- the type
**Parameters:** content

- the content
**Parameters:** next

- the next content model

---

#### Constructor Detail

ContentModel

```java
public ContentModel()
```

Creates

ContentModel

---

#### ContentModel

public ContentModel()

Creates

ContentModel

ContentModel

```java
public ContentModel​(
Element
content)
```

Create a content model for an element.

**Parameters:** content

- the element

---

#### ContentModel

public ContentModel​(

Element

content)

Create a content model for an element.

ContentModel

```java
public ContentModel​(int type,

ContentModel
content)
```

Create a content model of a particular type.

**Parameters:** type

- the type
**Parameters:** content

- the content

---

#### ContentModel

public ContentModel​(int type,

ContentModel

content)

Create a content model of a particular type.

ContentModel

```java
public ContentModel​(int type,

Object
content,

ContentModel
next)
```

Create a content model of a particular type.

**Parameters:** type

- the type
**Parameters:** content

- the content
**Parameters:** next

- the next content model

---

#### ContentModel

public ContentModel​(int type,

Object

content,

ContentModel

next)

Create a content model of a particular type.

Method Detail

- empty

```java
public boolean empty()
```

Return true if the content model could
match an empty input stream.

**Returns:** true

if the content model could
match an empty input stream

- getElements

```java
public void getElements​(
Vector
<
Element
> elemVec)
```

Update elemVec with the list of elements that are
part of the this contentModel.

**Parameters:** elemVec

- the list of elements

- first

```java
public boolean first​(
Object
token)
```

Return true if the token could potentially be the
first token in the input stream.

**Parameters:** token

- the token
**Returns:** true

if the token could potentially be the first token
in the input stream

- first

```java
public
Element
first()
```

Return the element that must be next.

**Returns:** the element that must be next

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
**Returns:** the string representation of this

ContentModel

---

#### Method Detail

empty

```java
public boolean empty()
```

Return true if the content model could
match an empty input stream.

**Returns:** true

if the content model could
match an empty input stream

---

#### empty

public boolean empty()

Return true if the content model could
match an empty input stream.

getElements

```java
public void getElements​(
Vector
<
Element
> elemVec)
```

Update elemVec with the list of elements that are
part of the this contentModel.

**Parameters:** elemVec

- the list of elements

---

#### getElements

public void getElements​(

Vector

<

Element

> elemVec)

Update elemVec with the list of elements that are
part of the this contentModel.

first

```java
public boolean first​(
Object
token)
```

Return true if the token could potentially be the
first token in the input stream.

**Parameters:** token

- the token
**Returns:** true

if the token could potentially be the first token
in the input stream

---

#### first

public boolean first​(

Object

token)

Return true if the token could potentially be the
first token in the input stream.

first

```java
public
Element
first()
```

Return the element that must be next.

**Returns:** the element that must be next

---

#### first

public

Element

first()

Return the element that must be next.

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
**Returns:** the string representation of this

ContentModel

---

#### toString

public

String

toString()

Convert to a string.

---

