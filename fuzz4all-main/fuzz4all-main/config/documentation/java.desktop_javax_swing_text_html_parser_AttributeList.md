# Class AttributeList

**Source:** `java.desktop\javax\swing\text\html\parser\AttributeList.html`

### Class Description

```java
public final class
AttributeList

extends
Object

implements
DTDConstants
,
Serializable
```

This class defines the attributes of an SGML element
as described in a DTD using the ATTLIST construct.
An AttributeList can be obtained from the Element
class using the getAttributes() method.

It is actually an element in a linked list. Use the
getNext() method repeatedly to enumerate all the attributes
of an element.

**All Implemented Interfaces:** Serializable

,

DTDConstants

---

### Field Details

#### public
String
name

The attribute name

---

#### public int type

The attribute type

---

#### public
Vector
<?> values

The possible attribute values

---

#### public int modifier

The attribute modifier

---

#### public
String
value

The default attribute value

---

#### public
AttributeList
next

The next attribute in the list

---

### Constructor Details

#### public AttributeList​(
String
name)

Create an attribute list element.

**Parameters:**
- name

- the attribute name

---

#### public AttributeList​(
String
name,
int type,
int modifier,

String
value,

Vector
<?> values,

AttributeList
next)

Create an attribute list element.

**Parameters:**
- name

- the attribute name
- type

- the attribute type
- modifier

- the attribute modifier
- value

- the default attribute value
- values

- the possible attribute values
- next

- the next attribute in the list

---

### Method Details

#### public
String
getName()

**Returns:**
- attribute name

---

#### public int getType()

**Returns:**
- attribute type

**See Also:**
- DTDConstants

---

#### public int getModifier()

**Returns:**
- attribute modifier

**See Also:**
- DTDConstants

---

#### public
Enumeration
<?> getValues()

**Returns:**
- possible attribute values

---

#### public
String
getValue()

**Returns:**
- default attribute value

---

#### public
AttributeList
getNext()

**Returns:**
- the next attribute in the list

---

#### public
String
toString()

Description copied from class:

Object

**Overrides:**
- toString

in class

Object

**Returns:**
- string representation

---

#### public static int name2type​(
String
nm)

Converts an attribute name to the type

**Parameters:**
- nm

- an attribute name

**Returns:**
- the type

---

#### public static
String
type2name​(int tp)

Converts a type to the attribute name

**Parameters:**
- tp

- a type

**Returns:**
- the attribute name

---

### Additional Sections

#### Class AttributeList

java.lang.Object

- javax.swing.text.html.parser.AttributeList

javax.swing.text.html.parser.AttributeList

**All Implemented Interfaces:** Serializable

,

DTDConstants

```java
public final class
AttributeList

extends
Object

implements
DTDConstants
,
Serializable
```

This class defines the attributes of an SGML element
as described in a DTD using the ATTLIST construct.
An AttributeList can be obtained from the Element
class using the getAttributes() method.

It is actually an element in a linked list. Use the
getNext() method repeatedly to enumerate all the attributes
of an element.

**See Also:** Element

,

Serialized Form

public final class

AttributeList

extends

Object

implements

DTDConstants

,

Serializable

This class defines the attributes of an SGML element
as described in a DTD using the ATTLIST construct.
An AttributeList can be obtained from the Element
class using the getAttributes() method.

It is actually an element in a linked list. Use the
getNext() method repeatedly to enumerate all the attributes
of an element.

It is actually an element in a linked list. Use the
getNext() method repeatedly to enumerate all the attributes
of an element.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

int

modifier

The attribute modifier

String

name

The attribute name

AttributeList

next

The next attribute in the list

int

type

The attribute type

String

value

The default attribute value

Vector

<?>

values

The possible attribute values

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

Constructor

Description

AttributeList

​(

String

name)

Create an attribute list element.

AttributeList

​(

String

name,
int type,
int modifier,

String

value,

Vector

<?> values,

AttributeList

next)

Create an attribute list element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getModifier

()

String

getName

()

AttributeList

getNext

()

int

getType

()

String

getValue

()

Enumeration

<?>

getValues

()

static int

name2type

​(

String

nm)

Converts an attribute name to the type

String

toString

()

Returns a string representation of the object.

static

String

type2name

​(int tp)

Converts a type to the attribute name

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

int

modifier

The attribute modifier

String

name

The attribute name

AttributeList

next

The next attribute in the list

int

type

The attribute type

String

value

The default attribute value

Vector

<?>

values

The possible attribute values

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

The attribute modifier

The attribute name

The next attribute in the list

The attribute type

The default attribute value

The possible attribute values

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

Constructor

Description

AttributeList

​(

String

name)

Create an attribute list element.

AttributeList

​(

String

name,
int type,
int modifier,

String

value,

Vector

<?> values,

AttributeList

next)

Create an attribute list element.

---

#### Constructor Summary

Create an attribute list element.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getModifier

()

String

getName

()

AttributeList

getNext

()

int

getType

()

String

getValue

()

Enumeration

<?>

getValues

()

static int

name2type

​(

String

nm)

Converts an attribute name to the type

String

toString

()

Returns a string representation of the object.

static

String

type2name

​(int tp)

Converts a type to the attribute name

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

Converts an attribute name to the type

Returns a string representation of the object.

Converts a type to the attribute name

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

The attribute name

- type

```java
public int type
```

The attribute type

- values

```java
public
Vector
<?> values
```

The possible attribute values

- modifier

```java
public int modifier
```

The attribute modifier

- value

```java
public
String
value
```

The default attribute value

- next

```java
public
AttributeList
next
```

The next attribute in the list

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AttributeList

```java
public AttributeList​(
String
name)
```

Create an attribute list element.

**Parameters:** name

- the attribute name

- AttributeList

```java
public AttributeList​(
String
name,
int type,
int modifier,

String
value,

Vector
<?> values,

AttributeList
next)
```

Create an attribute list element.

**Parameters:** name

- the attribute name
**Parameters:** type

- the attribute type
**Parameters:** modifier

- the attribute modifier
**Parameters:** value

- the default attribute value
**Parameters:** values

- the possible attribute values
**Parameters:** next

- the next attribute in the list

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

**Returns:** attribute name

- getType

```java
public int getType()
```

**Returns:** attribute type
**See Also:** DTDConstants

- getModifier

```java
public int getModifier()
```

**Returns:** attribute modifier
**See Also:** DTDConstants

- getValues

```java
public
Enumeration
<?> getValues()
```

**Returns:** possible attribute values

- getValue

```java
public
String
getValue()
```

**Returns:** default attribute value

- getNext

```java
public
AttributeList
getNext()
```

**Returns:** the next attribute in the list

- toString

```java
public
String
toString()
```

Description copied from class:

Object

Returns a string representation of the object. In general, the

toString

method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

**Overrides:** toString

in class

Object
**Returns:** string representation

- name2type

```java
public static int name2type​(
String
nm)
```

Converts an attribute name to the type

**Parameters:** nm

- an attribute name
**Returns:** the type

- type2name

```java
public static
String
type2name​(int tp)
```

Converts a type to the attribute name

**Parameters:** tp

- a type
**Returns:** the attribute name

Field Detail

- name

```java
public
String
name
```

The attribute name

- type

```java
public int type
```

The attribute type

- values

```java
public
Vector
<?> values
```

The possible attribute values

- modifier

```java
public int modifier
```

The attribute modifier

- value

```java
public
String
value
```

The default attribute value

- next

```java
public
AttributeList
next
```

The next attribute in the list

---

#### Field Detail

name

```java
public
String
name
```

The attribute name

---

#### name

public

String

name

The attribute name

type

```java
public int type
```

The attribute type

---

#### type

public int type

The attribute type

values

```java
public
Vector
<?> values
```

The possible attribute values

---

#### values

public

Vector

<?> values

The possible attribute values

modifier

```java
public int modifier
```

The attribute modifier

---

#### modifier

public int modifier

The attribute modifier

value

```java
public
String
value
```

The default attribute value

---

#### value

public

String

value

The default attribute value

next

```java
public
AttributeList
next
```

The next attribute in the list

---

#### next

public

AttributeList

next

The next attribute in the list

Constructor Detail

- AttributeList

```java
public AttributeList​(
String
name)
```

Create an attribute list element.

**Parameters:** name

- the attribute name

- AttributeList

```java
public AttributeList​(
String
name,
int type,
int modifier,

String
value,

Vector
<?> values,

AttributeList
next)
```

Create an attribute list element.

**Parameters:** name

- the attribute name
**Parameters:** type

- the attribute type
**Parameters:** modifier

- the attribute modifier
**Parameters:** value

- the default attribute value
**Parameters:** values

- the possible attribute values
**Parameters:** next

- the next attribute in the list

---

#### Constructor Detail

AttributeList

```java
public AttributeList​(
String
name)
```

Create an attribute list element.

**Parameters:** name

- the attribute name

---

#### AttributeList

public AttributeList​(

String

name)

Create an attribute list element.

AttributeList

```java
public AttributeList​(
String
name,
int type,
int modifier,

String
value,

Vector
<?> values,

AttributeList
next)
```

Create an attribute list element.

**Parameters:** name

- the attribute name
**Parameters:** type

- the attribute type
**Parameters:** modifier

- the attribute modifier
**Parameters:** value

- the default attribute value
**Parameters:** values

- the possible attribute values
**Parameters:** next

- the next attribute in the list

---

#### AttributeList

public AttributeList​(

String

name,
int type,
int modifier,

String

value,

Vector

<?> values,

AttributeList

next)

Create an attribute list element.

Method Detail

- getName

```java
public
String
getName()
```

**Returns:** attribute name

- getType

```java
public int getType()
```

**Returns:** attribute type
**See Also:** DTDConstants

- getModifier

```java
public int getModifier()
```

**Returns:** attribute modifier
**See Also:** DTDConstants

- getValues

```java
public
Enumeration
<?> getValues()
```

**Returns:** possible attribute values

- getValue

```java
public
String
getValue()
```

**Returns:** default attribute value

- getNext

```java
public
AttributeList
getNext()
```

**Returns:** the next attribute in the list

- toString

```java
public
String
toString()
```

Description copied from class:

Object

Returns a string representation of the object. In general, the

toString

method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

**Overrides:** toString

in class

Object
**Returns:** string representation

- name2type

```java
public static int name2type​(
String
nm)
```

Converts an attribute name to the type

**Parameters:** nm

- an attribute name
**Returns:** the type

- type2name

```java
public static
String
type2name​(int tp)
```

Converts a type to the attribute name

**Parameters:** tp

- a type
**Returns:** the attribute name

---

#### Method Detail

getName

```java
public
String
getName()
```

**Returns:** attribute name

---

#### getName

public

String

getName()

getType

```java
public int getType()
```

**Returns:** attribute type
**See Also:** DTDConstants

---

#### getType

public int getType()

getModifier

```java
public int getModifier()
```

**Returns:** attribute modifier
**See Also:** DTDConstants

---

#### getModifier

public int getModifier()

getValues

```java
public
Enumeration
<?> getValues()
```

**Returns:** possible attribute values

---

#### getValues

public

Enumeration

<?> getValues()

getValue

```java
public
String
getValue()
```

**Returns:** default attribute value

---

#### getValue

public

String

getValue()

getNext

```java
public
AttributeList
getNext()
```

**Returns:** the next attribute in the list

---

#### getNext

public

AttributeList

getNext()

toString

```java
public
String
toString()
```

Description copied from class:

Object

Returns a string representation of the object. In general, the

toString

method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

**Overrides:** toString

in class

Object
**Returns:** string representation

---

#### toString

public

String

toString()

Description copied from class:

Object

Returns a string representation of the object. In general, the

toString

method returns a string that
"textually represents" this object. The result should
be a concise but informative representation that is easy for a
person to read.
It is recommended that all subclasses override this method.

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

The

toString

method for class

Object

returns a string consisting of the name of the class of which the
object is an instance, the at-sign character `

@

', and
the unsigned hexadecimal representation of the hash code of the
object. In other words, this method returns a string equal to the
value of:

```java
getClass().getName() + '@' + Integer.toHexString(hashCode())
```

getClass().getName() + '@' + Integer.toHexString(hashCode())

name2type

```java
public static int name2type​(
String
nm)
```

Converts an attribute name to the type

**Parameters:** nm

- an attribute name
**Returns:** the type

---

#### name2type

public static int name2type​(

String

nm)

Converts an attribute name to the type

type2name

```java
public static
String
type2name​(int tp)
```

Converts a type to the attribute name

**Parameters:** tp

- a type
**Returns:** the attribute name

---

#### type2name

public static

String

type2name​(int tp)

Converts a type to the attribute name

---

