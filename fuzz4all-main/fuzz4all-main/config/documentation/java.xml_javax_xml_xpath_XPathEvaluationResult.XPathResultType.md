# Enum XPathEvaluationResult.XPathResultType

**Source:** `java.xml\javax\xml\xpath\XPathEvaluationResult.XPathResultType.html`

### Class Description

```java
public static enum
XPathEvaluationResult.XPathResultType

extends
Enum
<
XPathEvaluationResult.XPathResultType
>
```

XPathResultType represents possible return types of an XPath evaluation.
Provided as an enum type, it allows the use of switch statement. At the
same time, a mapping is provided between the original QName types in

XPathConstants

and class types used in the generic methods.

**All Implemented Interfaces:** Serializable

,

Comparable

<

XPathEvaluationResult.XPathResultType

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
XPathEvaluationResult.XPathResultType
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (XPathEvaluationResult.XPathResultType c : XPathEvaluationResult.XPathResultType.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
XPathEvaluationResult.XPathResultType
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

#### public static
QName
getQNameType​(
Class
<?> clsType)

Returns the QName type as specified in

XPathConstants

that
corresponds to the specified class type.

**Parameters:**
- clsType

- a class type that the enum type supports

**Returns:**
- the QName type that matches with the specified class type,
null if there is no match

---

### Additional Sections

#### Enum XPathEvaluationResult.XPathResultType

java.lang.Object

- java.lang.Enum

<

XPathEvaluationResult.XPathResultType

>
- - javax.xml.xpath.XPathEvaluationResult.XPathResultType

java.lang.Enum

<

XPathEvaluationResult.XPathResultType

>

- javax.xml.xpath.XPathEvaluationResult.XPathResultType

javax.xml.xpath.XPathEvaluationResult.XPathResultType

**All Implemented Interfaces:** Serializable

,

Comparable

<

XPathEvaluationResult.XPathResultType

>

**Enclosing interface:** XPathEvaluationResult

<

T

>

```java
public static enum
XPathEvaluationResult.XPathResultType

extends
Enum
<
XPathEvaluationResult.XPathResultType
>
```

XPathResultType represents possible return types of an XPath evaluation.
Provided as an enum type, it allows the use of switch statement. At the
same time, a mapping is provided between the original QName types in

XPathConstants

and class types used in the generic methods.

public static enum

XPathEvaluationResult.XPathResultType

extends

Enum

<

XPathEvaluationResult.XPathResultType

>

XPathResultType represents possible return types of an XPath evaluation.
Provided as an enum type, it allows the use of switch statement. At the
same time, a mapping is provided between the original QName types in

XPathConstants

and class types used in the generic methods.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ANY

Any type that represents any of the 5 other types listed below.

BOOLEAN

The XPath 1.0 boolean data type.

NODE

The XPath 1.0 NodeSet data type.

NODESET

The XPath 1.0 NodeSet data type.

NUMBER

The XPath 1.0 Number data type.

STRING

The XPath 1.0 String data type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

QName

getQNameType

​(

Class

<?> clsType)

Returns the QName type as specified in

XPathConstants

that
corresponds to the specified class type.

static

XPathEvaluationResult.XPathResultType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

XPathEvaluationResult.XPathResultType

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

ANY

Any type that represents any of the 5 other types listed below.

BOOLEAN

The XPath 1.0 boolean data type.

NODE

The XPath 1.0 NodeSet data type.

NODESET

The XPath 1.0 NodeSet data type.

NUMBER

The XPath 1.0 Number data type.

STRING

The XPath 1.0 String data type.

---

#### Enum Constant Summary

Any type that represents any of the 5 other types listed below.

The XPath 1.0 boolean data type.

The XPath 1.0 NodeSet data type.

The XPath 1.0 Number data type.

The XPath 1.0 String data type.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

QName

getQNameType

​(

Class

<?> clsType)

Returns the QName type as specified in

XPathConstants

that
corresponds to the specified class type.

static

XPathEvaluationResult.XPathResultType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

XPathEvaluationResult.XPathResultType

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Returns the QName type as specified in

XPathConstants

that
corresponds to the specified class type.

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- ANY

```java
public static final
XPathEvaluationResult.XPathResultType
ANY
```

Any type that represents any of the 5 other types listed below.
Maps to

XPathEvaluationResult

.

- BOOLEAN

```java
public static final
XPathEvaluationResult.XPathResultType
BOOLEAN
```

The XPath 1.0 boolean data type. Maps to Java

Boolean

.

- NUMBER

```java
public static final
XPathEvaluationResult.XPathResultType
NUMBER
```

The XPath 1.0 Number data type. Maps to Java

Number

. Of the
subtypes of Number, only Double, Integer and Long are required.

- STRING

```java
public static final
XPathEvaluationResult.XPathResultType
STRING
```

The XPath 1.0 String data type. Maps to Java

String

.

- NODESET

```java
public static final
XPathEvaluationResult.XPathResultType
NODESET
```

The XPath 1.0 NodeSet data type. Maps to

NodeList

.

- NODE

```java
public static final
XPathEvaluationResult.XPathResultType
NODE
```

The XPath 1.0 NodeSet data type. Maps to

Node

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
XPathEvaluationResult.XPathResultType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (XPathEvaluationResult.XPathResultType c : XPathEvaluationResult.XPathResultType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
XPathEvaluationResult.XPathResultType
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- getQNameType

```java
public static
QName
getQNameType​(
Class
<?> clsType)
```

Returns the QName type as specified in

XPathConstants

that
corresponds to the specified class type.

**Parameters:** clsType

- a class type that the enum type supports
**Returns:** the QName type that matches with the specified class type,
null if there is no match

Enum Constant Detail

- ANY

```java
public static final
XPathEvaluationResult.XPathResultType
ANY
```

Any type that represents any of the 5 other types listed below.
Maps to

XPathEvaluationResult

.

- BOOLEAN

```java
public static final
XPathEvaluationResult.XPathResultType
BOOLEAN
```

The XPath 1.0 boolean data type. Maps to Java

Boolean

.

- NUMBER

```java
public static final
XPathEvaluationResult.XPathResultType
NUMBER
```

The XPath 1.0 Number data type. Maps to Java

Number

. Of the
subtypes of Number, only Double, Integer and Long are required.

- STRING

```java
public static final
XPathEvaluationResult.XPathResultType
STRING
```

The XPath 1.0 String data type. Maps to Java

String

.

- NODESET

```java
public static final
XPathEvaluationResult.XPathResultType
NODESET
```

The XPath 1.0 NodeSet data type. Maps to

NodeList

.

- NODE

```java
public static final
XPathEvaluationResult.XPathResultType
NODE
```

The XPath 1.0 NodeSet data type. Maps to

Node

.

---

#### Enum Constant Detail

ANY

```java
public static final
XPathEvaluationResult.XPathResultType
ANY
```

Any type that represents any of the 5 other types listed below.
Maps to

XPathEvaluationResult

.

---

#### ANY

public static final

XPathEvaluationResult.XPathResultType

ANY

Any type that represents any of the 5 other types listed below.
Maps to

XPathEvaluationResult

.

BOOLEAN

```java
public static final
XPathEvaluationResult.XPathResultType
BOOLEAN
```

The XPath 1.0 boolean data type. Maps to Java

Boolean

.

---

#### BOOLEAN

public static final

XPathEvaluationResult.XPathResultType

BOOLEAN

The XPath 1.0 boolean data type. Maps to Java

Boolean

.

NUMBER

```java
public static final
XPathEvaluationResult.XPathResultType
NUMBER
```

The XPath 1.0 Number data type. Maps to Java

Number

. Of the
subtypes of Number, only Double, Integer and Long are required.

---

#### NUMBER

public static final

XPathEvaluationResult.XPathResultType

NUMBER

The XPath 1.0 Number data type. Maps to Java

Number

. Of the
subtypes of Number, only Double, Integer and Long are required.

STRING

```java
public static final
XPathEvaluationResult.XPathResultType
STRING
```

The XPath 1.0 String data type. Maps to Java

String

.

---

#### STRING

public static final

XPathEvaluationResult.XPathResultType

STRING

The XPath 1.0 String data type. Maps to Java

String

.

NODESET

```java
public static final
XPathEvaluationResult.XPathResultType
NODESET
```

The XPath 1.0 NodeSet data type. Maps to

NodeList

.

---

#### NODESET

public static final

XPathEvaluationResult.XPathResultType

NODESET

The XPath 1.0 NodeSet data type. Maps to

NodeList

.

NODE

```java
public static final
XPathEvaluationResult.XPathResultType
NODE
```

The XPath 1.0 NodeSet data type. Maps to

Node

.

---

#### NODE

public static final

XPathEvaluationResult.XPathResultType

NODE

The XPath 1.0 NodeSet data type. Maps to

Node

.

Method Detail

- values

```java
public static
XPathEvaluationResult.XPathResultType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (XPathEvaluationResult.XPathResultType c : XPathEvaluationResult.XPathResultType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
XPathEvaluationResult.XPathResultType
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- getQNameType

```java
public static
QName
getQNameType​(
Class
<?> clsType)
```

Returns the QName type as specified in

XPathConstants

that
corresponds to the specified class type.

**Parameters:** clsType

- a class type that the enum type supports
**Returns:** the QName type that matches with the specified class type,
null if there is no match

---

#### Method Detail

values

```java
public static
XPathEvaluationResult.XPathResultType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (XPathEvaluationResult.XPathResultType c : XPathEvaluationResult.XPathResultType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

XPathEvaluationResult.XPathResultType

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (XPathEvaluationResult.XPathResultType c : XPathEvaluationResult.XPathResultType.values())
System.out.println(c);
```

for (XPathEvaluationResult.XPathResultType c : XPathEvaluationResult.XPathResultType.values())
System.out.println(c);

valueOf

```java
public static
XPathEvaluationResult.XPathResultType
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

XPathEvaluationResult.XPathResultType

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

getQNameType

```java
public static
QName
getQNameType​(
Class
<?> clsType)
```

Returns the QName type as specified in

XPathConstants

that
corresponds to the specified class type.

**Parameters:** clsType

- a class type that the enum type supports
**Returns:** the QName type that matches with the specified class type,
null if there is no match

---

#### getQNameType

public static

QName

getQNameType​(

Class

<?> clsType)

Returns the QName type as specified in

XPathConstants

that
corresponds to the specified class type.

---

