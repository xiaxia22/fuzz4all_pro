# Enum LambdaExpressionTree.BodyKind

**Source:** `jdk.compiler\com\sun\source\tree\LambdaExpressionTree.BodyKind.html`

### Class Description

```java
public static enum
LambdaExpressionTree.BodyKind

extends
Enum
<
LambdaExpressionTree.BodyKind
>
```

Lambda expressions come in two forms:

- expression lambdas, whose body is an expression, and

statement lambdas, whose body is a block

**All Implemented Interfaces:** Serializable

,

Comparable

<

LambdaExpressionTree.BodyKind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
LambdaExpressionTree.BodyKind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LambdaExpressionTree.BodyKind c : LambdaExpressionTree.BodyKind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
LambdaExpressionTree.BodyKind
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

### Additional Sections

#### Enum LambdaExpressionTree.BodyKind

java.lang.Object

- java.lang.Enum

<

LambdaExpressionTree.BodyKind

>
- - com.sun.source.tree.LambdaExpressionTree.BodyKind

java.lang.Enum

<

LambdaExpressionTree.BodyKind

>

- com.sun.source.tree.LambdaExpressionTree.BodyKind

com.sun.source.tree.LambdaExpressionTree.BodyKind

**All Implemented Interfaces:** Serializable

,

Comparable

<

LambdaExpressionTree.BodyKind

>

**Enclosing interface:** LambdaExpressionTree

```java
public static enum
LambdaExpressionTree.BodyKind

extends
Enum
<
LambdaExpressionTree.BodyKind
>
```

Lambda expressions come in two forms:

- expression lambdas, whose body is an expression, and

statement lambdas, whose body is a block

public static enum

LambdaExpressionTree.BodyKind

extends

Enum

<

LambdaExpressionTree.BodyKind

>

Lambda expressions come in two forms:

- expression lambdas, whose body is an expression, and

statement lambdas, whose body is a block

expression lambdas, whose body is an expression, and

statement lambdas, whose body is a block

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

EXPRESSION

enum constant for expression lambdas

STATEMENT

enum constant for statement lambdas

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

LambdaExpressionTree.BodyKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

LambdaExpressionTree.BodyKind

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

EXPRESSION

enum constant for expression lambdas

STATEMENT

enum constant for statement lambdas

---

#### Enum Constant Summary

enum constant for expression lambdas

enum constant for statement lambdas

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

LambdaExpressionTree.BodyKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

LambdaExpressionTree.BodyKind

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

- EXPRESSION

```java
public static final
LambdaExpressionTree.BodyKind
EXPRESSION
```

enum constant for expression lambdas

- STATEMENT

```java
public static final
LambdaExpressionTree.BodyKind
STATEMENT
```

enum constant for statement lambdas

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
LambdaExpressionTree.BodyKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LambdaExpressionTree.BodyKind c : LambdaExpressionTree.BodyKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
LambdaExpressionTree.BodyKind
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

Enum Constant Detail

- EXPRESSION

```java
public static final
LambdaExpressionTree.BodyKind
EXPRESSION
```

enum constant for expression lambdas

- STATEMENT

```java
public static final
LambdaExpressionTree.BodyKind
STATEMENT
```

enum constant for statement lambdas

---

#### Enum Constant Detail

EXPRESSION

```java
public static final
LambdaExpressionTree.BodyKind
EXPRESSION
```

enum constant for expression lambdas

---

#### EXPRESSION

public static final

LambdaExpressionTree.BodyKind

EXPRESSION

enum constant for expression lambdas

STATEMENT

```java
public static final
LambdaExpressionTree.BodyKind
STATEMENT
```

enum constant for statement lambdas

---

#### STATEMENT

public static final

LambdaExpressionTree.BodyKind

STATEMENT

enum constant for statement lambdas

Method Detail

- values

```java
public static
LambdaExpressionTree.BodyKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LambdaExpressionTree.BodyKind c : LambdaExpressionTree.BodyKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
LambdaExpressionTree.BodyKind
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

#### Method Detail

values

```java
public static
LambdaExpressionTree.BodyKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LambdaExpressionTree.BodyKind c : LambdaExpressionTree.BodyKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

LambdaExpressionTree.BodyKind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (LambdaExpressionTree.BodyKind c : LambdaExpressionTree.BodyKind.values())
System.out.println(c);
```

for (LambdaExpressionTree.BodyKind c : LambdaExpressionTree.BodyKind.values())
System.out.println(c);

valueOf

```java
public static
LambdaExpressionTree.BodyKind
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

LambdaExpressionTree.BodyKind

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

