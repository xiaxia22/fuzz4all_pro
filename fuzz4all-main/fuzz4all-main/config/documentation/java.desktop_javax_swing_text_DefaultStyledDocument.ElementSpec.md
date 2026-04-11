# Class DefaultStyledDocument.ElementSpec

**Source:** `java.desktop\javax\swing\text\DefaultStyledDocument.ElementSpec.html`

### Class Description

```java
public static class
DefaultStyledDocument.ElementSpec

extends
Object
```

Specification for building elements.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**Enclosing class:** DefaultStyledDocument

---

### Field Details

#### public static final short StartTagType

A possible value for getType. This specifies
that this record type is a start tag and
represents markup that specifies the start
of an element.

**See Also:**
- Constant Field Values

---

#### public static final short EndTagType

A possible value for getType. This specifies
that this record type is a end tag and
represents markup that specifies the end
of an element.

**See Also:**
- Constant Field Values

---

#### public static final short ContentType

A possible value for getType. This specifies
that this record type represents content.

**See Also:**
- Constant Field Values

---

#### public static final short JoinPreviousDirection

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to what precedes it.

**See Also:**
- Constant Field Values

---

#### public static final short JoinNextDirection

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to what follows it.

**See Also:**
- Constant Field Values

---

#### public static final short OriginateDirection

A possible value for getDirection. This specifies
that the data associated with this record should
be used to originate a new element. This would be
the normal value.

**See Also:**
- Constant Field Values

---

#### public static final short JoinFractureDirection

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to the fractured element.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ElementSpec​(
AttributeSet
a,
short type)

Constructor useful for markup when the markup will not
be stored in the document.

**Parameters:**
- a

- the attributes for the element
- type

- the type of the element (StartTagType, EndTagType,
ContentType)

---

#### public ElementSpec​(
AttributeSet
a,
short type,
int len)

Constructor for parsing inside the document when
the data has already been added, but len information
is needed.

**Parameters:**
- a

- the attributes for the element
- type

- the type of the element (StartTagType, EndTagType,
ContentType)
- len

- the length >= 0

---

#### public ElementSpec​(
AttributeSet
a,
short type,
char[] txt,
int offs,
int len)

Constructor for creating a spec externally for batch
input of content and markup into the document.

**Parameters:**
- a

- the attributes for the element
- type

- the type of the element (StartTagType, EndTagType,
ContentType)
- txt

- the text for the element
- offs

- the offset into the text >= 0
- len

- the length of the text >= 0

---

### Method Details

#### public void setType​(short type)

Sets the element type.

**Parameters:**
- type

- the type of the element (StartTagType, EndTagType,
ContentType)

---

#### public short getType()

Gets the element type.

**Returns:**
- the type of the element (StartTagType, EndTagType,
ContentType)

---

#### public void setDirection​(short direction)

Sets the direction.

**Parameters:**
- direction

- the direction (JoinPreviousDirection,
JoinNextDirection)

---

#### public short getDirection()

Gets the direction.

**Returns:**
- the direction (JoinPreviousDirection, JoinNextDirection)

---

#### public
AttributeSet
getAttributes()

Gets the element attributes.

**Returns:**
- the attribute set

---

#### public char[] getArray()

Gets the array of characters.

**Returns:**
- the array

---

#### public int getOffset()

Gets the starting offset.

**Returns:**
- the offset >= 0

---

#### public int getLength()

Gets the length.

**Returns:**
- the length >= 0

---

#### public
String
toString()

Converts the element to a string.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string

---

### Additional Sections

#### Class DefaultStyledDocument.ElementSpec

java.lang.Object

- javax.swing.text.DefaultStyledDocument.ElementSpec

javax.swing.text.DefaultStyledDocument.ElementSpec

**Enclosing class:** DefaultStyledDocument

```java
public static class
DefaultStyledDocument.ElementSpec

extends
Object
```

Specification for building elements.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

public static class

DefaultStyledDocument.ElementSpec

extends

Object

Specification for building elements.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static short

ContentType

A possible value for getType.

static short

EndTagType

A possible value for getType.

static short

JoinFractureDirection

A possible value for getDirection.

static short

JoinNextDirection

A possible value for getDirection.

static short

JoinPreviousDirection

A possible value for getDirection.

static short

OriginateDirection

A possible value for getDirection.

static short

StartTagType

A possible value for getType.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ElementSpec

​(

AttributeSet

a,
short type)

Constructor useful for markup when the markup will not
be stored in the document.

ElementSpec

​(

AttributeSet

a,
short type,
char[] txt,
int offs,
int len)

Constructor for creating a spec externally for batch
input of content and markup into the document.

ElementSpec

​(

AttributeSet

a,
short type,
int len)

Constructor for parsing inside the document when
the data has already been added, but len information
is needed.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

char[]

getArray

()

Gets the array of characters.

AttributeSet

getAttributes

()

Gets the element attributes.

short

getDirection

()

Gets the direction.

int

getLength

()

Gets the length.

int

getOffset

()

Gets the starting offset.

short

getType

()

Gets the element type.

void

setDirection

​(short direction)

Sets the direction.

void

setType

​(short type)

Sets the element type.

String

toString

()

Converts the element to a string.

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

static short

ContentType

A possible value for getType.

static short

EndTagType

A possible value for getType.

static short

JoinFractureDirection

A possible value for getDirection.

static short

JoinNextDirection

A possible value for getDirection.

static short

JoinPreviousDirection

A possible value for getDirection.

static short

OriginateDirection

A possible value for getDirection.

static short

StartTagType

A possible value for getType.

---

#### Field Summary

A possible value for getType.

A possible value for getDirection.

Constructor Summary

Constructors

Constructor

Description

ElementSpec

​(

AttributeSet

a,
short type)

Constructor useful for markup when the markup will not
be stored in the document.

ElementSpec

​(

AttributeSet

a,
short type,
char[] txt,
int offs,
int len)

Constructor for creating a spec externally for batch
input of content and markup into the document.

ElementSpec

​(

AttributeSet

a,
short type,
int len)

Constructor for parsing inside the document when
the data has already been added, but len information
is needed.

---

#### Constructor Summary

Constructor useful for markup when the markup will not
be stored in the document.

Constructor for creating a spec externally for batch
input of content and markup into the document.

Constructor for parsing inside the document when
the data has already been added, but len information
is needed.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

char[]

getArray

()

Gets the array of characters.

AttributeSet

getAttributes

()

Gets the element attributes.

short

getDirection

()

Gets the direction.

int

getLength

()

Gets the length.

int

getOffset

()

Gets the starting offset.

short

getType

()

Gets the element type.

void

setDirection

​(short direction)

Sets the direction.

void

setType

​(short type)

Sets the element type.

String

toString

()

Converts the element to a string.

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

Gets the array of characters.

Gets the element attributes.

Gets the direction.

Gets the length.

Gets the starting offset.

Gets the element type.

Sets the direction.

Sets the element type.

Converts the element to a string.

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

- StartTagType

```java
public static final short StartTagType
```

A possible value for getType. This specifies
that this record type is a start tag and
represents markup that specifies the start
of an element.

**See Also:** Constant Field Values

- EndTagType

```java
public static final short EndTagType
```

A possible value for getType. This specifies
that this record type is a end tag and
represents markup that specifies the end
of an element.

**See Also:** Constant Field Values

- ContentType

```java
public static final short ContentType
```

A possible value for getType. This specifies
that this record type represents content.

**See Also:** Constant Field Values

- JoinPreviousDirection

```java
public static final short JoinPreviousDirection
```

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to what precedes it.

**See Also:** Constant Field Values

- JoinNextDirection

```java
public static final short JoinNextDirection
```

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to what follows it.

**See Also:** Constant Field Values

- OriginateDirection

```java
public static final short OriginateDirection
```

A possible value for getDirection. This specifies
that the data associated with this record should
be used to originate a new element. This would be
the normal value.

**See Also:** Constant Field Values

- JoinFractureDirection

```java
public static final short JoinFractureDirection
```

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to the fractured element.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ElementSpec

```java
public ElementSpec​(
AttributeSet
a,
short type)
```

Constructor useful for markup when the markup will not
be stored in the document.

**Parameters:** a

- the attributes for the element
**Parameters:** type

- the type of the element (StartTagType, EndTagType,
ContentType)

- ElementSpec

```java
public ElementSpec​(
AttributeSet
a,
short type,
int len)
```

Constructor for parsing inside the document when
the data has already been added, but len information
is needed.

**Parameters:** a

- the attributes for the element
**Parameters:** type

- the type of the element (StartTagType, EndTagType,
ContentType)
**Parameters:** len

- the length >= 0

- ElementSpec

```java
public ElementSpec​(
AttributeSet
a,
short type,
char[] txt,
int offs,
int len)
```

Constructor for creating a spec externally for batch
input of content and markup into the document.

**Parameters:** a

- the attributes for the element
**Parameters:** type

- the type of the element (StartTagType, EndTagType,
ContentType)
**Parameters:** txt

- the text for the element
**Parameters:** offs

- the offset into the text >= 0
**Parameters:** len

- the length of the text >= 0

============ METHOD DETAIL ==========

- Method Detail

- setType

```java
public void setType​(short type)
```

Sets the element type.

**Parameters:** type

- the type of the element (StartTagType, EndTagType,
ContentType)

- getType

```java
public short getType()
```

Gets the element type.

**Returns:** the type of the element (StartTagType, EndTagType,
ContentType)

- setDirection

```java
public void setDirection​(short direction)
```

Sets the direction.

**Parameters:** direction

- the direction (JoinPreviousDirection,
JoinNextDirection)

- getDirection

```java
public short getDirection()
```

Gets the direction.

**Returns:** the direction (JoinPreviousDirection, JoinNextDirection)

- getAttributes

```java
public
AttributeSet
getAttributes()
```

Gets the element attributes.

**Returns:** the attribute set

- getArray

```java
public char[] getArray()
```

Gets the array of characters.

**Returns:** the array

- getOffset

```java
public int getOffset()
```

Gets the starting offset.

**Returns:** the offset >= 0

- getLength

```java
public int getLength()
```

Gets the length.

**Returns:** the length >= 0

- toString

```java
public
String
toString()
```

Converts the element to a string.

**Overrides:** toString

in class

Object
**Returns:** the string

Field Detail

- StartTagType

```java
public static final short StartTagType
```

A possible value for getType. This specifies
that this record type is a start tag and
represents markup that specifies the start
of an element.

**See Also:** Constant Field Values

- EndTagType

```java
public static final short EndTagType
```

A possible value for getType. This specifies
that this record type is a end tag and
represents markup that specifies the end
of an element.

**See Also:** Constant Field Values

- ContentType

```java
public static final short ContentType
```

A possible value for getType. This specifies
that this record type represents content.

**See Also:** Constant Field Values

- JoinPreviousDirection

```java
public static final short JoinPreviousDirection
```

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to what precedes it.

**See Also:** Constant Field Values

- JoinNextDirection

```java
public static final short JoinNextDirection
```

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to what follows it.

**See Also:** Constant Field Values

- OriginateDirection

```java
public static final short OriginateDirection
```

A possible value for getDirection. This specifies
that the data associated with this record should
be used to originate a new element. This would be
the normal value.

**See Also:** Constant Field Values

- JoinFractureDirection

```java
public static final short JoinFractureDirection
```

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to the fractured element.

**See Also:** Constant Field Values

---

#### Field Detail

StartTagType

```java
public static final short StartTagType
```

A possible value for getType. This specifies
that this record type is a start tag and
represents markup that specifies the start
of an element.

**See Also:** Constant Field Values

---

#### StartTagType

public static final short StartTagType

A possible value for getType. This specifies
that this record type is a start tag and
represents markup that specifies the start
of an element.

EndTagType

```java
public static final short EndTagType
```

A possible value for getType. This specifies
that this record type is a end tag and
represents markup that specifies the end
of an element.

**See Also:** Constant Field Values

---

#### EndTagType

public static final short EndTagType

A possible value for getType. This specifies
that this record type is a end tag and
represents markup that specifies the end
of an element.

ContentType

```java
public static final short ContentType
```

A possible value for getType. This specifies
that this record type represents content.

**See Also:** Constant Field Values

---

#### ContentType

public static final short ContentType

A possible value for getType. This specifies
that this record type represents content.

JoinPreviousDirection

```java
public static final short JoinPreviousDirection
```

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to what precedes it.

**See Also:** Constant Field Values

---

#### JoinPreviousDirection

public static final short JoinPreviousDirection

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to what precedes it.

JoinNextDirection

```java
public static final short JoinNextDirection
```

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to what follows it.

**See Also:** Constant Field Values

---

#### JoinNextDirection

public static final short JoinNextDirection

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to what follows it.

OriginateDirection

```java
public static final short OriginateDirection
```

A possible value for getDirection. This specifies
that the data associated with this record should
be used to originate a new element. This would be
the normal value.

**See Also:** Constant Field Values

---

#### OriginateDirection

public static final short OriginateDirection

A possible value for getDirection. This specifies
that the data associated with this record should
be used to originate a new element. This would be
the normal value.

JoinFractureDirection

```java
public static final short JoinFractureDirection
```

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to the fractured element.

**See Also:** Constant Field Values

---

#### JoinFractureDirection

public static final short JoinFractureDirection

A possible value for getDirection. This specifies
that the data associated with this record should
be joined to the fractured element.

Constructor Detail

- ElementSpec

```java
public ElementSpec​(
AttributeSet
a,
short type)
```

Constructor useful for markup when the markup will not
be stored in the document.

**Parameters:** a

- the attributes for the element
**Parameters:** type

- the type of the element (StartTagType, EndTagType,
ContentType)

- ElementSpec

```java
public ElementSpec​(
AttributeSet
a,
short type,
int len)
```

Constructor for parsing inside the document when
the data has already been added, but len information
is needed.

**Parameters:** a

- the attributes for the element
**Parameters:** type

- the type of the element (StartTagType, EndTagType,
ContentType)
**Parameters:** len

- the length >= 0

- ElementSpec

```java
public ElementSpec​(
AttributeSet
a,
short type,
char[] txt,
int offs,
int len)
```

Constructor for creating a spec externally for batch
input of content and markup into the document.

**Parameters:** a

- the attributes for the element
**Parameters:** type

- the type of the element (StartTagType, EndTagType,
ContentType)
**Parameters:** txt

- the text for the element
**Parameters:** offs

- the offset into the text >= 0
**Parameters:** len

- the length of the text >= 0

---

#### Constructor Detail

ElementSpec

```java
public ElementSpec​(
AttributeSet
a,
short type)
```

Constructor useful for markup when the markup will not
be stored in the document.

**Parameters:** a

- the attributes for the element
**Parameters:** type

- the type of the element (StartTagType, EndTagType,
ContentType)

---

#### ElementSpec

public ElementSpec​(

AttributeSet

a,
short type)

Constructor useful for markup when the markup will not
be stored in the document.

ElementSpec

```java
public ElementSpec​(
AttributeSet
a,
short type,
int len)
```

Constructor for parsing inside the document when
the data has already been added, but len information
is needed.

**Parameters:** a

- the attributes for the element
**Parameters:** type

- the type of the element (StartTagType, EndTagType,
ContentType)
**Parameters:** len

- the length >= 0

---

#### ElementSpec

public ElementSpec​(

AttributeSet

a,
short type,
int len)

Constructor for parsing inside the document when
the data has already been added, but len information
is needed.

ElementSpec

```java
public ElementSpec​(
AttributeSet
a,
short type,
char[] txt,
int offs,
int len)
```

Constructor for creating a spec externally for batch
input of content and markup into the document.

**Parameters:** a

- the attributes for the element
**Parameters:** type

- the type of the element (StartTagType, EndTagType,
ContentType)
**Parameters:** txt

- the text for the element
**Parameters:** offs

- the offset into the text >= 0
**Parameters:** len

- the length of the text >= 0

---

#### ElementSpec

public ElementSpec​(

AttributeSet

a,
short type,
char[] txt,
int offs,
int len)

Constructor for creating a spec externally for batch
input of content and markup into the document.

Method Detail

- setType

```java
public void setType​(short type)
```

Sets the element type.

**Parameters:** type

- the type of the element (StartTagType, EndTagType,
ContentType)

- getType

```java
public short getType()
```

Gets the element type.

**Returns:** the type of the element (StartTagType, EndTagType,
ContentType)

- setDirection

```java
public void setDirection​(short direction)
```

Sets the direction.

**Parameters:** direction

- the direction (JoinPreviousDirection,
JoinNextDirection)

- getDirection

```java
public short getDirection()
```

Gets the direction.

**Returns:** the direction (JoinPreviousDirection, JoinNextDirection)

- getAttributes

```java
public
AttributeSet
getAttributes()
```

Gets the element attributes.

**Returns:** the attribute set

- getArray

```java
public char[] getArray()
```

Gets the array of characters.

**Returns:** the array

- getOffset

```java
public int getOffset()
```

Gets the starting offset.

**Returns:** the offset >= 0

- getLength

```java
public int getLength()
```

Gets the length.

**Returns:** the length >= 0

- toString

```java
public
String
toString()
```

Converts the element to a string.

**Overrides:** toString

in class

Object
**Returns:** the string

---

#### Method Detail

setType

```java
public void setType​(short type)
```

Sets the element type.

**Parameters:** type

- the type of the element (StartTagType, EndTagType,
ContentType)

---

#### setType

public void setType​(short type)

Sets the element type.

getType

```java
public short getType()
```

Gets the element type.

**Returns:** the type of the element (StartTagType, EndTagType,
ContentType)

---

#### getType

public short getType()

Gets the element type.

setDirection

```java
public void setDirection​(short direction)
```

Sets the direction.

**Parameters:** direction

- the direction (JoinPreviousDirection,
JoinNextDirection)

---

#### setDirection

public void setDirection​(short direction)

Sets the direction.

getDirection

```java
public short getDirection()
```

Gets the direction.

**Returns:** the direction (JoinPreviousDirection, JoinNextDirection)

---

#### getDirection

public short getDirection()

Gets the direction.

getAttributes

```java
public
AttributeSet
getAttributes()
```

Gets the element attributes.

**Returns:** the attribute set

---

#### getAttributes

public

AttributeSet

getAttributes()

Gets the element attributes.

getArray

```java
public char[] getArray()
```

Gets the array of characters.

**Returns:** the array

---

#### getArray

public char[] getArray()

Gets the array of characters.

getOffset

```java
public int getOffset()
```

Gets the starting offset.

**Returns:** the offset >= 0

---

#### getOffset

public int getOffset()

Gets the starting offset.

getLength

```java
public int getLength()
```

Gets the length.

**Returns:** the length >= 0

---

#### getLength

public int getLength()

Gets the length.

toString

```java
public
String
toString()
```

Converts the element to a string.

**Overrides:** toString

in class

Object
**Returns:** the string

---

#### toString

public

String

toString()

Converts the element to a string.

---

