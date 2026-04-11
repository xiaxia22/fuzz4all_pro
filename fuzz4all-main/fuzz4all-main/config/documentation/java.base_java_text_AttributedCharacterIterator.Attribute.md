# Class AttributedCharacterIterator.Attribute

**Source:** `java.base\java\text\AttributedCharacterIterator.Attribute.html`

### Class Description

```java
public static class
AttributedCharacterIterator.Attribute

extends
Object

implements
Serializable
```

Defines attribute keys that are used to identify text attributes. These
keys are used in

AttributedCharacterIterator

and

AttributedString

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
AttributedCharacterIterator.Attribute
LANGUAGE

Attribute key for the language of some text.

Values are instances of

Locale

.

**See Also:**
- Locale

---

#### public static final
AttributedCharacterIterator.Attribute
READING

Attribute key for the reading of some text. In languages where the written form
and the pronunciation of a word are only loosely related (such as Japanese),
it is often necessary to store the reading (pronunciation) along with the
written form.

Values are instances of

Annotation

holding instances of

String

.

**See Also:**
- Annotation

,

String

---

#### public static final
AttributedCharacterIterator.Attribute
INPUT_METHOD_SEGMENT

Attribute key for input method segments. Input methods often break
up text into segments, which usually correspond to words.

Values are instances of

Annotation

holding a

null

reference.

**See Also:**
- Annotation

---

### Constructor Details

#### protected Attribute​(
String
name)

Constructs an

Attribute

with the given name.

**Parameters:**
- name

- the name of

Attribute

---

### Method Details

#### public final boolean equals​(
Object
obj)

Compares two objects for equality. This version only returns true
for

x.equals(y)

if

x

and

y

refer
to the same object, and guarantees this for all subclasses.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Returns a hash code value for the object. This version is identical to
the one in

Object

, but is also final.

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

#### public
String
toString()

Returns a string representation of the object. This version returns the
concatenation of class name,

"("

, a name identifying the attribute
and

")"

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

#### protected
String
getName()

Returns the name of the attribute.

**Returns:**
- the name of

Attribute

---

#### protected
Object
readResolve()
throws
InvalidObjectException

Resolves instances being deserialized to the predefined constants.

**Returns:**
- the resolved

Attribute

object

**Throws:**
- InvalidObjectException

- if the object to resolve is not
an instance of

Attribute

---

### Additional Sections

#### Class AttributedCharacterIterator.Attribute

java.lang.Object

- java.text.AttributedCharacterIterator.Attribute

java.text.AttributedCharacterIterator.Attribute

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** Format.Field

,

TextAttribute

**Enclosing interface:** AttributedCharacterIterator

```java
public static class
AttributedCharacterIterator.Attribute

extends
Object

implements
Serializable
```

Defines attribute keys that are used to identify text attributes. These
keys are used in

AttributedCharacterIterator

and

AttributedString

.

**Since:** 1.2
**See Also:** AttributedCharacterIterator

,

AttributedString

,

Serialized Form

public static class

AttributedCharacterIterator.Attribute

extends

Object

implements

Serializable

Defines attribute keys that are used to identify text attributes. These
keys are used in

AttributedCharacterIterator

and

AttributedString

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

AttributedCharacterIterator.Attribute

INPUT_METHOD_SEGMENT

Attribute key for input method segments.

static

AttributedCharacterIterator.Attribute

LANGUAGE

Attribute key for the language of some text.

static

AttributedCharacterIterator.Attribute

READING

Attribute key for the reading of some text.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Attribute

​(

String

name)

Constructs an

Attribute

with the given name.

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

Compares two objects for equality.

protected

String

getName

()

Returns the name of the attribute.

int

hashCode

()

Returns a hash code value for the object.

protected

Object

readResolve

()

Resolves instances being deserialized to the predefined constants.

String

toString

()

Returns a string representation of the object.

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

Fields

Modifier and Type

Field

Description

static

AttributedCharacterIterator.Attribute

INPUT_METHOD_SEGMENT

Attribute key for input method segments.

static

AttributedCharacterIterator.Attribute

LANGUAGE

Attribute key for the language of some text.

static

AttributedCharacterIterator.Attribute

READING

Attribute key for the reading of some text.

---

#### Field Summary

Attribute key for input method segments.

Attribute key for the language of some text.

Attribute key for the reading of some text.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Attribute

​(

String

name)

Constructs an

Attribute

with the given name.

---

#### Constructor Summary

Constructs an

Attribute

with the given name.

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

Compares two objects for equality.

protected

String

getName

()

Returns the name of the attribute.

int

hashCode

()

Returns a hash code value for the object.

protected

Object

readResolve

()

Resolves instances being deserialized to the predefined constants.

String

toString

()

Returns a string representation of the object.

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

Compares two objects for equality.

Returns the name of the attribute.

Returns a hash code value for the object.

Resolves instances being deserialized to the predefined constants.

Returns a string representation of the object.

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

============ FIELD DETAIL ===========

- Field Detail

- LANGUAGE

```java
public static final
AttributedCharacterIterator.Attribute
LANGUAGE
```

Attribute key for the language of some text.

Values are instances of

Locale

.

**See Also:** Locale

- READING

```java
public static final
AttributedCharacterIterator.Attribute
READING
```

Attribute key for the reading of some text. In languages where the written form
and the pronunciation of a word are only loosely related (such as Japanese),
it is often necessary to store the reading (pronunciation) along with the
written form.

Values are instances of

Annotation

holding instances of

String

.

**See Also:** Annotation

,

String

- INPUT_METHOD_SEGMENT

```java
public static final
AttributedCharacterIterator.Attribute
INPUT_METHOD_SEGMENT
```

Attribute key for input method segments. Input methods often break
up text into segments, which usually correspond to words.

Values are instances of

Annotation

holding a

null

reference.

**See Also:** Annotation

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Attribute

```java
protected Attribute​(
String
name)
```

Constructs an

Attribute

with the given name.

**Parameters:** name

- the name of

Attribute

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Compares two objects for equality. This version only returns true
for

x.equals(y)

if

x

and

y

refer
to the same object, and guarantees this for all subclasses.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for the object. This version is identical to
the one in

Object

, but is also final.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of the object. This version returns the
concatenation of class name,

"("

, a name identifying the attribute
and

")"

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- getName

```java
protected
String
getName()
```

Returns the name of the attribute.

**Returns:** the name of

Attribute

- readResolve

```java
protected
Object
readResolve()
throws
InvalidObjectException
```

Resolves instances being deserialized to the predefined constants.

**Returns:** the resolved

Attribute

object
**Throws:** InvalidObjectException

- if the object to resolve is not
an instance of

Attribute

Field Detail

- LANGUAGE

```java
public static final
AttributedCharacterIterator.Attribute
LANGUAGE
```

Attribute key for the language of some text.

Values are instances of

Locale

.

**See Also:** Locale

- READING

```java
public static final
AttributedCharacterIterator.Attribute
READING
```

Attribute key for the reading of some text. In languages where the written form
and the pronunciation of a word are only loosely related (such as Japanese),
it is often necessary to store the reading (pronunciation) along with the
written form.

Values are instances of

Annotation

holding instances of

String

.

**See Also:** Annotation

,

String

- INPUT_METHOD_SEGMENT

```java
public static final
AttributedCharacterIterator.Attribute
INPUT_METHOD_SEGMENT
```

Attribute key for input method segments. Input methods often break
up text into segments, which usually correspond to words.

Values are instances of

Annotation

holding a

null

reference.

**See Also:** Annotation

---

#### Field Detail

LANGUAGE

```java
public static final
AttributedCharacterIterator.Attribute
LANGUAGE
```

Attribute key for the language of some text.

Values are instances of

Locale

.

**See Also:** Locale

---

#### LANGUAGE

public static final

AttributedCharacterIterator.Attribute

LANGUAGE

Attribute key for the language of some text.

Values are instances of

Locale

.

Values are instances of

Locale

.

READING

```java
public static final
AttributedCharacterIterator.Attribute
READING
```

Attribute key for the reading of some text. In languages where the written form
and the pronunciation of a word are only loosely related (such as Japanese),
it is often necessary to store the reading (pronunciation) along with the
written form.

Values are instances of

Annotation

holding instances of

String

.

**See Also:** Annotation

,

String

---

#### READING

public static final

AttributedCharacterIterator.Attribute

READING

Attribute key for the reading of some text. In languages where the written form
and the pronunciation of a word are only loosely related (such as Japanese),
it is often necessary to store the reading (pronunciation) along with the
written form.

Values are instances of

Annotation

holding instances of

String

.

Values are instances of

Annotation

holding instances of

String

.

INPUT_METHOD_SEGMENT

```java
public static final
AttributedCharacterIterator.Attribute
INPUT_METHOD_SEGMENT
```

Attribute key for input method segments. Input methods often break
up text into segments, which usually correspond to words.

Values are instances of

Annotation

holding a

null

reference.

**See Also:** Annotation

---

#### INPUT_METHOD_SEGMENT

public static final

AttributedCharacterIterator.Attribute

INPUT_METHOD_SEGMENT

Attribute key for input method segments. Input methods often break
up text into segments, which usually correspond to words.

Values are instances of

Annotation

holding a

null

reference.

Values are instances of

Annotation

holding a

null

reference.

Constructor Detail

- Attribute

```java
protected Attribute​(
String
name)
```

Constructs an

Attribute

with the given name.

**Parameters:** name

- the name of

Attribute

---

#### Constructor Detail

Attribute

```java
protected Attribute​(
String
name)
```

Constructs an

Attribute

with the given name.

**Parameters:** name

- the name of

Attribute

---

#### Attribute

protected Attribute​(

String

name)

Constructs an

Attribute

with the given name.

Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Compares two objects for equality. This version only returns true
for

x.equals(y)

if

x

and

y

refer
to the same object, and guarantees this for all subclasses.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for the object. This version is identical to
the one in

Object

, but is also final.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of the object. This version returns the
concatenation of class name,

"("

, a name identifying the attribute
and

")"

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- getName

```java
protected
String
getName()
```

Returns the name of the attribute.

**Returns:** the name of

Attribute

- readResolve

```java
protected
Object
readResolve()
throws
InvalidObjectException
```

Resolves instances being deserialized to the predefined constants.

**Returns:** the resolved

Attribute

object
**Throws:** InvalidObjectException

- if the object to resolve is not
an instance of

Attribute

---

#### Method Detail

equals

```java
public final boolean equals​(
Object
obj)
```

Compares two objects for equality. This version only returns true
for

x.equals(y)

if

x

and

y

refer
to the same object, and guarantees this for all subclasses.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public final boolean equals​(

Object

obj)

Compares two objects for equality. This version only returns true
for

x.equals(y)

if

x

and

y

refer
to the same object, and guarantees this for all subclasses.

hashCode

```java
public final int hashCode()
```

Returns a hash code value for the object. This version is identical to
the one in

Object

, but is also final.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Returns a hash code value for the object. This version is identical to
the one in

Object

, but is also final.

toString

```java
public
String
toString()
```

Returns a string representation of the object. This version returns the
concatenation of class name,

"("

, a name identifying the attribute
and

")"

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string representation of the object. This version returns the
concatenation of class name,

"("

, a name identifying the attribute
and

")"

.

getName

```java
protected
String
getName()
```

Returns the name of the attribute.

**Returns:** the name of

Attribute

---

#### getName

protected

String

getName()

Returns the name of the attribute.

readResolve

```java
protected
Object
readResolve()
throws
InvalidObjectException
```

Resolves instances being deserialized to the predefined constants.

**Returns:** the resolved

Attribute

object
**Throws:** InvalidObjectException

- if the object to resolve is not
an instance of

Attribute

---

#### readResolve

protected

Object

readResolve()
throws

InvalidObjectException

Resolves instances being deserialized to the predefined constants.

---

