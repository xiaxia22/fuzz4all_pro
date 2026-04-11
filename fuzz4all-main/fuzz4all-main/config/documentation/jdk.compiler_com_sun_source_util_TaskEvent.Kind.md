# Enum TaskEvent.Kind

**Source:** `jdk.compiler\com\sun\source\util\TaskEvent.Kind.html`

### Class Description

```java
public static enum
TaskEvent.Kind

extends
Enum
<
TaskEvent.Kind
>
```

Kind of task event.

**All Implemented Interfaces:** Serializable

,

Comparable

<

TaskEvent.Kind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
TaskEvent.Kind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TaskEvent.Kind c : TaskEvent.Kind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
TaskEvent.Kind
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

#### Enum TaskEvent.Kind

java.lang.Object

- java.lang.Enum

<

TaskEvent.Kind

>
- - com.sun.source.util.TaskEvent.Kind

java.lang.Enum

<

TaskEvent.Kind

>

- com.sun.source.util.TaskEvent.Kind

com.sun.source.util.TaskEvent.Kind

**All Implemented Interfaces:** Serializable

,

Comparable

<

TaskEvent.Kind

>

**Enclosing class:** TaskEvent

```java
public static enum
TaskEvent.Kind

extends
Enum
<
TaskEvent.Kind
>
```

Kind of task event.

**Since:** 1.6

public static enum

TaskEvent.Kind

extends

Enum

<

TaskEvent.Kind

>

Kind of task event.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ANALYZE

For events relating to elements being analyzed for errors.

ANNOTATION_PROCESSING

For events relating to overall annotation processing.

ANNOTATION_PROCESSING_ROUND

For events relating to an individual annotation processing round.

COMPILATION

Sent before parsing first source file, and after writing the last output file.

ENTER

For events relating to elements being entered.

GENERATE

For events relating to class files being generated.

PARSE

For events related to the parsing of a file.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

TaskEvent.Kind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

TaskEvent.Kind

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

ANALYZE

For events relating to elements being analyzed for errors.

ANNOTATION_PROCESSING

For events relating to overall annotation processing.

ANNOTATION_PROCESSING_ROUND

For events relating to an individual annotation processing round.

COMPILATION

Sent before parsing first source file, and after writing the last output file.

ENTER

For events relating to elements being entered.

GENERATE

For events relating to class files being generated.

PARSE

For events related to the parsing of a file.

---

#### Enum Constant Summary

For events relating to elements being analyzed for errors.

For events relating to overall annotation processing.

For events relating to an individual annotation processing round.

Sent before parsing first source file, and after writing the last output file.

For events relating to elements being entered.

For events relating to class files being generated.

For events related to the parsing of a file.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

TaskEvent.Kind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

TaskEvent.Kind

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

- PARSE

```java
public static final
TaskEvent.Kind
PARSE
```

For events related to the parsing of a file.

- ENTER

```java
public static final
TaskEvent.Kind
ENTER
```

For events relating to elements being entered.

- ANALYZE

```java
public static final
TaskEvent.Kind
ANALYZE
```

For events relating to elements being analyzed for errors.

- GENERATE

```java
public static final
TaskEvent.Kind
GENERATE
```

For events relating to class files being generated.

- ANNOTATION_PROCESSING

```java
public static final
TaskEvent.Kind
ANNOTATION_PROCESSING
```

For events relating to overall annotation processing.

- ANNOTATION_PROCESSING_ROUND

```java
public static final
TaskEvent.Kind
ANNOTATION_PROCESSING_ROUND
```

For events relating to an individual annotation processing round.

- COMPILATION

```java
public static final
TaskEvent.Kind
COMPILATION
```

Sent before parsing first source file, and after writing the last output file.
This event is not sent when using

JavacTask.parse()

,

JavacTask.analyze()

or

JavacTask.generate()

.

**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
TaskEvent.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TaskEvent.Kind c : TaskEvent.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
TaskEvent.Kind
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

- PARSE

```java
public static final
TaskEvent.Kind
PARSE
```

For events related to the parsing of a file.

- ENTER

```java
public static final
TaskEvent.Kind
ENTER
```

For events relating to elements being entered.

- ANALYZE

```java
public static final
TaskEvent.Kind
ANALYZE
```

For events relating to elements being analyzed for errors.

- GENERATE

```java
public static final
TaskEvent.Kind
GENERATE
```

For events relating to class files being generated.

- ANNOTATION_PROCESSING

```java
public static final
TaskEvent.Kind
ANNOTATION_PROCESSING
```

For events relating to overall annotation processing.

- ANNOTATION_PROCESSING_ROUND

```java
public static final
TaskEvent.Kind
ANNOTATION_PROCESSING_ROUND
```

For events relating to an individual annotation processing round.

- COMPILATION

```java
public static final
TaskEvent.Kind
COMPILATION
```

Sent before parsing first source file, and after writing the last output file.
This event is not sent when using

JavacTask.parse()

,

JavacTask.analyze()

or

JavacTask.generate()

.

**Since:** 9

---

#### Enum Constant Detail

PARSE

```java
public static final
TaskEvent.Kind
PARSE
```

For events related to the parsing of a file.

---

#### PARSE

public static final

TaskEvent.Kind

PARSE

For events related to the parsing of a file.

ENTER

```java
public static final
TaskEvent.Kind
ENTER
```

For events relating to elements being entered.

---

#### ENTER

public static final

TaskEvent.Kind

ENTER

For events relating to elements being entered.

ANALYZE

```java
public static final
TaskEvent.Kind
ANALYZE
```

For events relating to elements being analyzed for errors.

---

#### ANALYZE

public static final

TaskEvent.Kind

ANALYZE

For events relating to elements being analyzed for errors.

GENERATE

```java
public static final
TaskEvent.Kind
GENERATE
```

For events relating to class files being generated.

---

#### GENERATE

public static final

TaskEvent.Kind

GENERATE

For events relating to class files being generated.

ANNOTATION_PROCESSING

```java
public static final
TaskEvent.Kind
ANNOTATION_PROCESSING
```

For events relating to overall annotation processing.

---

#### ANNOTATION_PROCESSING

public static final

TaskEvent.Kind

ANNOTATION_PROCESSING

For events relating to overall annotation processing.

ANNOTATION_PROCESSING_ROUND

```java
public static final
TaskEvent.Kind
ANNOTATION_PROCESSING_ROUND
```

For events relating to an individual annotation processing round.

---

#### ANNOTATION_PROCESSING_ROUND

public static final

TaskEvent.Kind

ANNOTATION_PROCESSING_ROUND

For events relating to an individual annotation processing round.

COMPILATION

```java
public static final
TaskEvent.Kind
COMPILATION
```

Sent before parsing first source file, and after writing the last output file.
This event is not sent when using

JavacTask.parse()

,

JavacTask.analyze()

or

JavacTask.generate()

.

**Since:** 9

---

#### COMPILATION

public static final

TaskEvent.Kind

COMPILATION

Sent before parsing first source file, and after writing the last output file.
This event is not sent when using

JavacTask.parse()

,

JavacTask.analyze()

or

JavacTask.generate()

.

Method Detail

- values

```java
public static
TaskEvent.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TaskEvent.Kind c : TaskEvent.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
TaskEvent.Kind
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
TaskEvent.Kind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TaskEvent.Kind c : TaskEvent.Kind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

TaskEvent.Kind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (TaskEvent.Kind c : TaskEvent.Kind.values())
System.out.println(c);
```

for (TaskEvent.Kind c : TaskEvent.Kind.values())
System.out.println(c);

valueOf

```java
public static
TaskEvent.Kind
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

TaskEvent.Kind

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

