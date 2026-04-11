# Enum NestingKind

**Source:** `java.compiler\javax\lang\model\element\NestingKind.html`

### Class Description

```java
public enum
NestingKind

extends
Enum
<
NestingKind
>
```

The

nesting kind

of a type element.
Type elements come in four varieties:
top-level, member, local, and anonymous.

Nesting kind

is a non-standard term used here to denote this
classification.

Note that it is possible additional nesting kinds will be added
in future versions of the platform.

Example:

The classes below are annotated with their nesting kind.

```java
import java.lang.annotation.*;
import static java.lang.annotation.RetentionPolicy.*;
import javax.lang.model.element.*;
import static javax.lang.model.element.NestingKind.*;

@Nesting(TOP_LEVEL)
public class NestingExamples {
@Nesting(MEMBER)
static class MemberClass1{}

@Nesting(MEMBER)
class MemberClass2{}

public static void main(String... argv) {
@Nesting(LOCAL)
class LocalClass{};

Class<?>[] classes = {
NestingExamples.class,
MemberClass1.class,
MemberClass2.class,
LocalClass.class
};

for(Class<?> clazz : classes) {
System.out.format("%s is %s%n",
clazz.getName(),
clazz.getAnnotation(Nesting.class).value());
}
}
}

@Retention(RUNTIME)
@interface Nesting {
NestingKind value();
}
```

**All Implemented Interfaces:** Serializable

,

Comparable

<

NestingKind

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
NestingKind
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (NestingKind c : NestingKind.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
NestingKind
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

#### public boolean isNested()

Does this constant correspond to a nested type element?
A

nested

type element is any that is not top-level.
More specifically, an

inner

type element is any nested type element that
is not

static

.

**Returns:**
- whether or not the constant is nested

**See The Java™ Language Specification :**
- 14.3 Inner Classes and Enclosing Instances

---

### Additional Sections

#### Enum NestingKind

java.lang.Object

- java.lang.Enum

<

NestingKind

>
- - javax.lang.model.element.NestingKind

java.lang.Enum

<

NestingKind

>

- javax.lang.model.element.NestingKind

javax.lang.model.element.NestingKind

**All Implemented Interfaces:** Serializable

,

Comparable

<

NestingKind

>

```java
public enum
NestingKind

extends
Enum
<
NestingKind
>
```

The

nesting kind

of a type element.
Type elements come in four varieties:
top-level, member, local, and anonymous.

Nesting kind

is a non-standard term used here to denote this
classification.

Note that it is possible additional nesting kinds will be added
in future versions of the platform.

Example:

The classes below are annotated with their nesting kind.

```java
import java.lang.annotation.*;
import static java.lang.annotation.RetentionPolicy.*;
import javax.lang.model.element.*;
import static javax.lang.model.element.NestingKind.*;

@Nesting(TOP_LEVEL)
public class NestingExamples {
@Nesting(MEMBER)
static class MemberClass1{}

@Nesting(MEMBER)
class MemberClass2{}

public static void main(String... argv) {
@Nesting(LOCAL)
class LocalClass{};

Class<?>[] classes = {
NestingExamples.class,
MemberClass1.class,
MemberClass2.class,
LocalClass.class
};

for(Class<?> clazz : classes) {
System.out.format("%s is %s%n",
clazz.getName(),
clazz.getAnnotation(Nesting.class).value());
}
}
}

@Retention(RUNTIME)
@interface Nesting {
NestingKind value();
}
```

**Since:** 1.6

public enum

NestingKind

extends

Enum

<

NestingKind

>

The

nesting kind

of a type element.
Type elements come in four varieties:
top-level, member, local, and anonymous.

Nesting kind

is a non-standard term used here to denote this
classification.

Note that it is possible additional nesting kinds will be added
in future versions of the platform.

Example:

The classes below are annotated with their nesting kind.

```java
import java.lang.annotation.*;
import static java.lang.annotation.RetentionPolicy.*;
import javax.lang.model.element.*;
import static javax.lang.model.element.NestingKind.*;

@Nesting(TOP_LEVEL)
public class NestingExamples {
@Nesting(MEMBER)
static class MemberClass1{}

@Nesting(MEMBER)
class MemberClass2{}

public static void main(String... argv) {
@Nesting(LOCAL)
class LocalClass{};

Class<?>[] classes = {
NestingExamples.class,
MemberClass1.class,
MemberClass2.class,
LocalClass.class
};

for(Class<?> clazz : classes) {
System.out.format("%s is %s%n",
clazz.getName(),
clazz.getAnnotation(Nesting.class).value());
}
}
}

@Retention(RUNTIME)
@interface Nesting {
NestingKind value();
}
```

Note that it is possible additional nesting kinds will be added
in future versions of the platform.

Example:

The classes below are annotated with their nesting kind.

```java
import java.lang.annotation.*;
import static java.lang.annotation.RetentionPolicy.*;
import javax.lang.model.element.*;
import static javax.lang.model.element.NestingKind.*;

@Nesting(TOP_LEVEL)
public class NestingExamples {
@Nesting(MEMBER)
static class MemberClass1{}

@Nesting(MEMBER)
class MemberClass2{}

public static void main(String... argv) {
@Nesting(LOCAL)
class LocalClass{};

Class<?>[] classes = {
NestingExamples.class,
MemberClass1.class,
MemberClass2.class,
LocalClass.class
};

for(Class<?> clazz : classes) {
System.out.format("%s is %s%n",
clazz.getName(),
clazz.getAnnotation(Nesting.class).value());
}
}
}

@Retention(RUNTIME)
@interface Nesting {
NestingKind value();
}
```

Example:

The classes below are annotated with their nesting kind.

```java
import java.lang.annotation.*;
import static java.lang.annotation.RetentionPolicy.*;
import javax.lang.model.element.*;
import static javax.lang.model.element.NestingKind.*;

@Nesting(TOP_LEVEL)
public class NestingExamples {
@Nesting(MEMBER)
static class MemberClass1{}

@Nesting(MEMBER)
class MemberClass2{}

public static void main(String... argv) {
@Nesting(LOCAL)
class LocalClass{};

Class<?>[] classes = {
NestingExamples.class,
MemberClass1.class,
MemberClass2.class,
LocalClass.class
};

for(Class<?> clazz : classes) {
System.out.format("%s is %s%n",
clazz.getName(),
clazz.getAnnotation(Nesting.class).value());
}
}
}

@Retention(RUNTIME)
@interface Nesting {
NestingKind value();
}
```

import java.lang.annotation.*;
import static java.lang.annotation.RetentionPolicy.*;
import javax.lang.model.element.*;
import static javax.lang.model.element.NestingKind.*;

@Nesting(TOP_LEVEL)
public class NestingExamples {
@Nesting(MEMBER)
static class MemberClass1{}

@Nesting(MEMBER)
class MemberClass2{}

public static void main(String... argv) {
@Nesting(LOCAL)
class LocalClass{};

Class<?>[] classes = {
NestingExamples.class,
MemberClass1.class,
MemberClass2.class,
LocalClass.class
};

for(Class<?> clazz : classes) {
System.out.format("%s is %s%n",
clazz.getName(),
clazz.getAnnotation(Nesting.class).value());
}
}
}

@Retention(RUNTIME)
@interface Nesting {
NestingKind value();
}

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ANONYMOUS

A type without a name.

LOCAL

A named type declared within a construct other than a type.

MEMBER

A type that is a named member of another type.

TOP_LEVEL

A top-level type, not contained within another type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isNested

()

Does this constant correspond to a nested type element?

static

NestingKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

NestingKind

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

ANONYMOUS

A type without a name.

LOCAL

A named type declared within a construct other than a type.

MEMBER

A type that is a named member of another type.

TOP_LEVEL

A top-level type, not contained within another type.

---

#### Enum Constant Summary

A type without a name.

A named type declared within a construct other than a type.

A type that is a named member of another type.

A top-level type, not contained within another type.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

isNested

()

Does this constant correspond to a nested type element?

static

NestingKind

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

NestingKind

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

Does this constant correspond to a nested type element?

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

- TOP_LEVEL

```java
public static final
NestingKind
TOP_LEVEL
```

A top-level type, not contained within another type.

- MEMBER

```java
public static final
NestingKind
MEMBER
```

A type that is a named member of another type.

**See The Java™ Language Specification :** 8.5 Member Type Declarations

- LOCAL

```java
public static final
NestingKind
LOCAL
```

A named type declared within a construct other than a type.

**See The Java™ Language Specification :** 14.3 Local Class Declarations

- ANONYMOUS

```java
public static final
NestingKind
ANONYMOUS
```

A type without a name.

**See The Java™ Language Specification :** 15.9.5 Anonymous Class Declarations

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
NestingKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (NestingKind c : NestingKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
NestingKind
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

- isNested

```java
public boolean isNested()
```

Does this constant correspond to a nested type element?
A

nested

type element is any that is not top-level.
More specifically, an

inner

type element is any nested type element that
is not

static

.

**Returns:** whether or not the constant is nested
**See The Java™ Language Specification :** 14.3 Inner Classes and Enclosing Instances

Enum Constant Detail

- TOP_LEVEL

```java
public static final
NestingKind
TOP_LEVEL
```

A top-level type, not contained within another type.

- MEMBER

```java
public static final
NestingKind
MEMBER
```

A type that is a named member of another type.

**See The Java™ Language Specification :** 8.5 Member Type Declarations

- LOCAL

```java
public static final
NestingKind
LOCAL
```

A named type declared within a construct other than a type.

**See The Java™ Language Specification :** 14.3 Local Class Declarations

- ANONYMOUS

```java
public static final
NestingKind
ANONYMOUS
```

A type without a name.

**See The Java™ Language Specification :** 15.9.5 Anonymous Class Declarations

---

#### Enum Constant Detail

TOP_LEVEL

```java
public static final
NestingKind
TOP_LEVEL
```

A top-level type, not contained within another type.

---

#### TOP_LEVEL

public static final

NestingKind

TOP_LEVEL

A top-level type, not contained within another type.

MEMBER

```java
public static final
NestingKind
MEMBER
```

A type that is a named member of another type.

**See The Java™ Language Specification :** 8.5 Member Type Declarations

---

#### MEMBER

public static final

NestingKind

MEMBER

A type that is a named member of another type.

LOCAL

```java
public static final
NestingKind
LOCAL
```

A named type declared within a construct other than a type.

**See The Java™ Language Specification :** 14.3 Local Class Declarations

---

#### LOCAL

public static final

NestingKind

LOCAL

A named type declared within a construct other than a type.

ANONYMOUS

```java
public static final
NestingKind
ANONYMOUS
```

A type without a name.

**See The Java™ Language Specification :** 15.9.5 Anonymous Class Declarations

---

#### ANONYMOUS

public static final

NestingKind

ANONYMOUS

A type without a name.

Method Detail

- values

```java
public static
NestingKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (NestingKind c : NestingKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
NestingKind
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

- isNested

```java
public boolean isNested()
```

Does this constant correspond to a nested type element?
A

nested

type element is any that is not top-level.
More specifically, an

inner

type element is any nested type element that
is not

static

.

**Returns:** whether or not the constant is nested
**See The Java™ Language Specification :** 14.3 Inner Classes and Enclosing Instances

---

#### Method Detail

values

```java
public static
NestingKind
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (NestingKind c : NestingKind.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

NestingKind

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (NestingKind c : NestingKind.values())
System.out.println(c);
```

for (NestingKind c : NestingKind.values())
System.out.println(c);

valueOf

```java
public static
NestingKind
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

NestingKind

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

isNested

```java
public boolean isNested()
```

Does this constant correspond to a nested type element?
A

nested

type element is any that is not top-level.
More specifically, an

inner

type element is any nested type element that
is not

static

.

**Returns:** whether or not the constant is nested
**See The Java™ Language Specification :** 14.3 Inner Classes and Enclosing Instances

---

#### isNested

public boolean isNested()

Does this constant correspond to a nested type element?
A

nested

type element is any that is not top-level.
More specifically, an

inner

type element is any nested type element that
is not

static

.

---

