# Class MessageFormat.Field

**Source:** `java.base\java\text\MessageFormat.Field.html`

### Class Description

```java
public static class
MessageFormat.Field

extends
Format.Field
```

Defines constants that are used as attribute keys in the

AttributedCharacterIterator

returned
from

MessageFormat.formatToCharacterIterator

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
MessageFormat.Field
ARGUMENT

Constant identifying a portion of a message that was generated
from an argument passed into

formatToCharacterIterator

.
The value associated with the key will be an

Integer

indicating the index in the

arguments

array of the
argument from which the text was generated.

---

### Constructor Details

#### protected Field​(
String
name)

Creates a Field with the specified name.

**Parameters:**
- name

- Name of the attribute

---

### Method Details

#### protected
Object
readResolve()
throws
InvalidObjectException

Resolves instances being deserialized to the predefined constants.

**Overrides:**
- readResolve

in class

AttributedCharacterIterator.Attribute

**Returns:**
- resolved MessageFormat.Field constant

**Throws:**
- InvalidObjectException

- if the constant could not be
resolved.

---

### Additional Sections

#### Class MessageFormat.Field

java.lang.Object

- java.text.AttributedCharacterIterator.Attribute
- - java.text.Format.Field
- - java.text.MessageFormat.Field

java.text.AttributedCharacterIterator.Attribute

- java.text.Format.Field
- - java.text.MessageFormat.Field

java.text.Format.Field

- java.text.MessageFormat.Field

java.text.MessageFormat.Field

**All Implemented Interfaces:** Serializable

**Enclosing class:** MessageFormat

```java
public static class
MessageFormat.Field

extends
Format.Field
```

Defines constants that are used as attribute keys in the

AttributedCharacterIterator

returned
from

MessageFormat.formatToCharacterIterator

.

**Since:** 1.4
**See Also:** Serialized Form

public static class

MessageFormat.Field

extends

Format.Field

Defines constants that are used as attribute keys in the

AttributedCharacterIterator

returned
from

MessageFormat.formatToCharacterIterator

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

MessageFormat.Field

ARGUMENT

Constant identifying a portion of a message that was generated
from an argument passed into

formatToCharacterIterator

.

- Fields declared in class java.text.

AttributedCharacterIterator.Attribute

INPUT_METHOD_SEGMENT

,

LANGUAGE

,

READING

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Field

​(

String

name)

Creates a Field with the specified name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Object

readResolve

()

Resolves instances being deserialized to the predefined constants.

- Methods declared in class java.text.

AttributedCharacterIterator.Attribute

equals

,

getName

,

hashCode

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

Fields

Modifier and Type

Field

Description

static

MessageFormat.Field

ARGUMENT

Constant identifying a portion of a message that was generated
from an argument passed into

formatToCharacterIterator

.

- Fields declared in class java.text.

AttributedCharacterIterator.Attribute

INPUT_METHOD_SEGMENT

,

LANGUAGE

,

READING

---

#### Field Summary

Constant identifying a portion of a message that was generated
from an argument passed into

formatToCharacterIterator

.

Fields declared in class java.text.

AttributedCharacterIterator.Attribute

INPUT_METHOD_SEGMENT

,

LANGUAGE

,

READING

---

#### Fields declared in class java.text. AttributedCharacterIterator.Attribute

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Field

​(

String

name)

Creates a Field with the specified name.

---

#### Constructor Summary

Creates a Field with the specified name.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Object

readResolve

()

Resolves instances being deserialized to the predefined constants.

- Methods declared in class java.text.

AttributedCharacterIterator.Attribute

equals

,

getName

,

hashCode

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

Resolves instances being deserialized to the predefined constants.

Methods declared in class java.text.

AttributedCharacterIterator.Attribute

equals

,

getName

,

hashCode

,

toString

---

#### Methods declared in class java.text. AttributedCharacterIterator.Attribute

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

- ARGUMENT

```java
public static final
MessageFormat.Field
ARGUMENT
```

Constant identifying a portion of a message that was generated
from an argument passed into

formatToCharacterIterator

.
The value associated with the key will be an

Integer

indicating the index in the

arguments

array of the
argument from which the text was generated.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Field

```java
protected Field​(
String
name)
```

Creates a Field with the specified name.

**Parameters:** name

- Name of the attribute

============ METHOD DETAIL ==========

- Method Detail

- readResolve

```java
protected
Object
readResolve()
throws
InvalidObjectException
```

Resolves instances being deserialized to the predefined constants.

**Overrides:** readResolve

in class

AttributedCharacterIterator.Attribute
**Returns:** resolved MessageFormat.Field constant
**Throws:** InvalidObjectException

- if the constant could not be
resolved.

Field Detail

- ARGUMENT

```java
public static final
MessageFormat.Field
ARGUMENT
```

Constant identifying a portion of a message that was generated
from an argument passed into

formatToCharacterIterator

.
The value associated with the key will be an

Integer

indicating the index in the

arguments

array of the
argument from which the text was generated.

---

#### Field Detail

ARGUMENT

```java
public static final
MessageFormat.Field
ARGUMENT
```

Constant identifying a portion of a message that was generated
from an argument passed into

formatToCharacterIterator

.
The value associated with the key will be an

Integer

indicating the index in the

arguments

array of the
argument from which the text was generated.

---

#### ARGUMENT

public static final

MessageFormat.Field

ARGUMENT

Constant identifying a portion of a message that was generated
from an argument passed into

formatToCharacterIterator

.
The value associated with the key will be an

Integer

indicating the index in the

arguments

array of the
argument from which the text was generated.

Constructor Detail

- Field

```java
protected Field​(
String
name)
```

Creates a Field with the specified name.

**Parameters:** name

- Name of the attribute

---

#### Constructor Detail

Field

```java
protected Field​(
String
name)
```

Creates a Field with the specified name.

**Parameters:** name

- Name of the attribute

---

#### Field

protected Field​(

String

name)

Creates a Field with the specified name.

Method Detail

- readResolve

```java
protected
Object
readResolve()
throws
InvalidObjectException
```

Resolves instances being deserialized to the predefined constants.

**Overrides:** readResolve

in class

AttributedCharacterIterator.Attribute
**Returns:** resolved MessageFormat.Field constant
**Throws:** InvalidObjectException

- if the constant could not be
resolved.

---

#### Method Detail

readResolve

```java
protected
Object
readResolve()
throws
InvalidObjectException
```

Resolves instances being deserialized to the predefined constants.

**Overrides:** readResolve

in class

AttributedCharacterIterator.Attribute
**Returns:** resolved MessageFormat.Field constant
**Throws:** InvalidObjectException

- if the constant could not be
resolved.

---

#### readResolve

protected

Object

readResolve()
throws

InvalidObjectException

Resolves instances being deserialized to the predefined constants.

---

