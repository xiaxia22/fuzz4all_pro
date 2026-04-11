# Class NumberFormat.Field

**Source:** `java.base\java\text\NumberFormat.Field.html`

### Class Description

```java
public static class
NumberFormat.Field

extends
Format.Field
```

Defines constants that are used as attribute keys in the

AttributedCharacterIterator

returned
from

NumberFormat.formatToCharacterIterator

and as
field identifiers in

FieldPosition

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
NumberFormat.Field
INTEGER

Constant identifying the integer field.

---

#### public static final
NumberFormat.Field
FRACTION

Constant identifying the fraction field.

---

#### public static final
NumberFormat.Field
EXPONENT

Constant identifying the exponent field.

---

#### public static final
NumberFormat.Field
DECIMAL_SEPARATOR

Constant identifying the decimal separator field.

---

#### public static final
NumberFormat.Field
SIGN

Constant identifying the sign field.

---

#### public static final
NumberFormat.Field
GROUPING_SEPARATOR

Constant identifying the grouping separator field.

---

#### public static final
NumberFormat.Field
EXPONENT_SYMBOL

Constant identifying the exponent symbol field.

---

#### public static final
NumberFormat.Field
PERCENT

Constant identifying the percent field.

---

#### public static final
NumberFormat.Field
PERMILLE

Constant identifying the permille field.

---

#### public static final
NumberFormat.Field
CURRENCY

Constant identifying the currency field.

---

#### public static final
NumberFormat.Field
EXPONENT_SIGN

Constant identifying the exponent sign field.

---

### Constructor Details

#### protected Field​(
String
name)

Creates a Field instance with the specified
name.

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
- resolved NumberFormat.Field constant

**Throws:**
- InvalidObjectException

- if the constant could not be resolved.

---

### Additional Sections

#### Class NumberFormat.Field

java.lang.Object

- java.text.AttributedCharacterIterator.Attribute
- - java.text.Format.Field
- - java.text.NumberFormat.Field

java.text.AttributedCharacterIterator.Attribute

- java.text.Format.Field
- - java.text.NumberFormat.Field

java.text.Format.Field

- java.text.NumberFormat.Field

java.text.NumberFormat.Field

**All Implemented Interfaces:** Serializable

**Enclosing class:** NumberFormat

```java
public static class
NumberFormat.Field

extends
Format.Field
```

Defines constants that are used as attribute keys in the

AttributedCharacterIterator

returned
from

NumberFormat.formatToCharacterIterator

and as
field identifiers in

FieldPosition

.

**Since:** 1.4
**See Also:** Serialized Form

public static class

NumberFormat.Field

extends

Format.Field

Defines constants that are used as attribute keys in the

AttributedCharacterIterator

returned
from

NumberFormat.formatToCharacterIterator

and as
field identifiers in

FieldPosition

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

NumberFormat.Field

CURRENCY

Constant identifying the currency field.

static

NumberFormat.Field

DECIMAL_SEPARATOR

Constant identifying the decimal separator field.

static

NumberFormat.Field

EXPONENT

Constant identifying the exponent field.

static

NumberFormat.Field

EXPONENT_SIGN

Constant identifying the exponent sign field.

static

NumberFormat.Field

EXPONENT_SYMBOL

Constant identifying the exponent symbol field.

static

NumberFormat.Field

FRACTION

Constant identifying the fraction field.

static

NumberFormat.Field

GROUPING_SEPARATOR

Constant identifying the grouping separator field.

static

NumberFormat.Field

INTEGER

Constant identifying the integer field.

static

NumberFormat.Field

PERCENT

Constant identifying the percent field.

static

NumberFormat.Field

PERMILLE

Constant identifying the permille field.

static

NumberFormat.Field

SIGN

Constant identifying the sign field.

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

Creates a Field instance with the specified
name.

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

NumberFormat.Field

CURRENCY

Constant identifying the currency field.

static

NumberFormat.Field

DECIMAL_SEPARATOR

Constant identifying the decimal separator field.

static

NumberFormat.Field

EXPONENT

Constant identifying the exponent field.

static

NumberFormat.Field

EXPONENT_SIGN

Constant identifying the exponent sign field.

static

NumberFormat.Field

EXPONENT_SYMBOL

Constant identifying the exponent symbol field.

static

NumberFormat.Field

FRACTION

Constant identifying the fraction field.

static

NumberFormat.Field

GROUPING_SEPARATOR

Constant identifying the grouping separator field.

static

NumberFormat.Field

INTEGER

Constant identifying the integer field.

static

NumberFormat.Field

PERCENT

Constant identifying the percent field.

static

NumberFormat.Field

PERMILLE

Constant identifying the permille field.

static

NumberFormat.Field

SIGN

Constant identifying the sign field.

- Fields declared in class java.text.

AttributedCharacterIterator.Attribute

INPUT_METHOD_SEGMENT

,

LANGUAGE

,

READING

---

#### Field Summary

Constant identifying the currency field.

Constant identifying the decimal separator field.

Constant identifying the exponent field.

Constant identifying the exponent sign field.

Constant identifying the exponent symbol field.

Constant identifying the fraction field.

Constant identifying the grouping separator field.

Constant identifying the integer field.

Constant identifying the percent field.

Constant identifying the permille field.

Constant identifying the sign field.

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

Creates a Field instance with the specified
name.

---

#### Constructor Summary

Creates a Field instance with the specified
name.

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

- INTEGER

```java
public static final
NumberFormat.Field
INTEGER
```

Constant identifying the integer field.

- FRACTION

```java
public static final
NumberFormat.Field
FRACTION
```

Constant identifying the fraction field.

- EXPONENT

```java
public static final
NumberFormat.Field
EXPONENT
```

Constant identifying the exponent field.

- DECIMAL_SEPARATOR

```java
public static final
NumberFormat.Field
DECIMAL_SEPARATOR
```

Constant identifying the decimal separator field.

- SIGN

```java
public static final
NumberFormat.Field
SIGN
```

Constant identifying the sign field.

- GROUPING_SEPARATOR

```java
public static final
NumberFormat.Field
GROUPING_SEPARATOR
```

Constant identifying the grouping separator field.

- EXPONENT_SYMBOL

```java
public static final
NumberFormat.Field
EXPONENT_SYMBOL
```

Constant identifying the exponent symbol field.

- PERCENT

```java
public static final
NumberFormat.Field
PERCENT
```

Constant identifying the percent field.

- PERMILLE

```java
public static final
NumberFormat.Field
PERMILLE
```

Constant identifying the permille field.

- CURRENCY

```java
public static final
NumberFormat.Field
CURRENCY
```

Constant identifying the currency field.

- EXPONENT_SIGN

```java
public static final
NumberFormat.Field
EXPONENT_SIGN
```

Constant identifying the exponent sign field.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Field

```java
protected Field​(
String
name)
```

Creates a Field instance with the specified
name.

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
**Returns:** resolved NumberFormat.Field constant
**Throws:** InvalidObjectException

- if the constant could not be resolved.

Field Detail

- INTEGER

```java
public static final
NumberFormat.Field
INTEGER
```

Constant identifying the integer field.

- FRACTION

```java
public static final
NumberFormat.Field
FRACTION
```

Constant identifying the fraction field.

- EXPONENT

```java
public static final
NumberFormat.Field
EXPONENT
```

Constant identifying the exponent field.

- DECIMAL_SEPARATOR

```java
public static final
NumberFormat.Field
DECIMAL_SEPARATOR
```

Constant identifying the decimal separator field.

- SIGN

```java
public static final
NumberFormat.Field
SIGN
```

Constant identifying the sign field.

- GROUPING_SEPARATOR

```java
public static final
NumberFormat.Field
GROUPING_SEPARATOR
```

Constant identifying the grouping separator field.

- EXPONENT_SYMBOL

```java
public static final
NumberFormat.Field
EXPONENT_SYMBOL
```

Constant identifying the exponent symbol field.

- PERCENT

```java
public static final
NumberFormat.Field
PERCENT
```

Constant identifying the percent field.

- PERMILLE

```java
public static final
NumberFormat.Field
PERMILLE
```

Constant identifying the permille field.

- CURRENCY

```java
public static final
NumberFormat.Field
CURRENCY
```

Constant identifying the currency field.

- EXPONENT_SIGN

```java
public static final
NumberFormat.Field
EXPONENT_SIGN
```

Constant identifying the exponent sign field.

---

#### Field Detail

INTEGER

```java
public static final
NumberFormat.Field
INTEGER
```

Constant identifying the integer field.

---

#### INTEGER

public static final

NumberFormat.Field

INTEGER

Constant identifying the integer field.

FRACTION

```java
public static final
NumberFormat.Field
FRACTION
```

Constant identifying the fraction field.

---

#### FRACTION

public static final

NumberFormat.Field

FRACTION

Constant identifying the fraction field.

EXPONENT

```java
public static final
NumberFormat.Field
EXPONENT
```

Constant identifying the exponent field.

---

#### EXPONENT

public static final

NumberFormat.Field

EXPONENT

Constant identifying the exponent field.

DECIMAL_SEPARATOR

```java
public static final
NumberFormat.Field
DECIMAL_SEPARATOR
```

Constant identifying the decimal separator field.

---

#### DECIMAL_SEPARATOR

public static final

NumberFormat.Field

DECIMAL_SEPARATOR

Constant identifying the decimal separator field.

SIGN

```java
public static final
NumberFormat.Field
SIGN
```

Constant identifying the sign field.

---

#### SIGN

public static final

NumberFormat.Field

SIGN

Constant identifying the sign field.

GROUPING_SEPARATOR

```java
public static final
NumberFormat.Field
GROUPING_SEPARATOR
```

Constant identifying the grouping separator field.

---

#### GROUPING_SEPARATOR

public static final

NumberFormat.Field

GROUPING_SEPARATOR

Constant identifying the grouping separator field.

EXPONENT_SYMBOL

```java
public static final
NumberFormat.Field
EXPONENT_SYMBOL
```

Constant identifying the exponent symbol field.

---

#### EXPONENT_SYMBOL

public static final

NumberFormat.Field

EXPONENT_SYMBOL

Constant identifying the exponent symbol field.

PERCENT

```java
public static final
NumberFormat.Field
PERCENT
```

Constant identifying the percent field.

---

#### PERCENT

public static final

NumberFormat.Field

PERCENT

Constant identifying the percent field.

PERMILLE

```java
public static final
NumberFormat.Field
PERMILLE
```

Constant identifying the permille field.

---

#### PERMILLE

public static final

NumberFormat.Field

PERMILLE

Constant identifying the permille field.

CURRENCY

```java
public static final
NumberFormat.Field
CURRENCY
```

Constant identifying the currency field.

---

#### CURRENCY

public static final

NumberFormat.Field

CURRENCY

Constant identifying the currency field.

EXPONENT_SIGN

```java
public static final
NumberFormat.Field
EXPONENT_SIGN
```

Constant identifying the exponent sign field.

---

#### EXPONENT_SIGN

public static final

NumberFormat.Field

EXPONENT_SIGN

Constant identifying the exponent sign field.

Constructor Detail

- Field

```java
protected Field​(
String
name)
```

Creates a Field instance with the specified
name.

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

Creates a Field instance with the specified
name.

**Parameters:** name

- Name of the attribute

---

#### Field

protected Field​(

String

name)

Creates a Field instance with the specified
name.

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
**Returns:** resolved NumberFormat.Field constant
**Throws:** InvalidObjectException

- if the constant could not be resolved.

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
**Returns:** resolved NumberFormat.Field constant
**Throws:** InvalidObjectException

- if the constant could not be resolved.

---

#### readResolve

protected

Object

readResolve()
throws

InvalidObjectException

Resolves instances being deserialized to the predefined constants.

---

