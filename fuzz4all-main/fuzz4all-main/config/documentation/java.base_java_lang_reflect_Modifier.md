# Class Modifier

**Source:** `java.base\java\lang\reflect\Modifier.html`

### Class Description

```java
public class
Modifier

extends
Object
```

The Modifier class provides

static

methods and
constants to decode class and member access modifiers. The sets of
modifiers are represented as integers with distinct bit positions
representing different modifiers. The values for the constants
representing the modifiers are taken from the tables in sections 4.1, 4.4, 4.5, and 4.7 of

The Java™ Virtual Machine Specification

.

**Since:** 1.1
**See Also:** Class.getModifiers()

,

Member.getModifiers()

---

### Field Details

#### public static final int PUBLIC

The

int

value representing the

public

modifier.

**See Also:**
- Constant Field Values

---

#### public static final int PRIVATE

The

int

value representing the

private

modifier.

**See Also:**
- Constant Field Values

---

#### public static final int PROTECTED

The

int

value representing the

protected

modifier.

**See Also:**
- Constant Field Values

---

#### public static final int STATIC

The

int

value representing the

static

modifier.

**See Also:**
- Constant Field Values

---

#### public static final int FINAL

The

int

value representing the

final

modifier.

**See Also:**
- Constant Field Values

---

#### public static final int SYNCHRONIZED

The

int

value representing the

synchronized

modifier.

**See Also:**
- Constant Field Values

---

#### public static final int VOLATILE

The

int

value representing the

volatile

modifier.

**See Also:**
- Constant Field Values

---

#### public static final int TRANSIENT

The

int

value representing the

transient

modifier.

**See Also:**
- Constant Field Values

---

#### public static final int NATIVE

The

int

value representing the

native

modifier.

**See Also:**
- Constant Field Values

---

#### public static final int INTERFACE

The

int

value representing the

interface

modifier.

**See Also:**
- Constant Field Values

---

#### public static final int ABSTRACT

The

int

value representing the

abstract

modifier.

**See Also:**
- Constant Field Values

---

#### public static final int STRICT

The

int

value representing the

strictfp

modifier.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public Modifier()

*No description found.*

---

### Method Details

#### public static boolean isPublic​(int mod)

Return

true

if the integer argument includes the

public

modifier,

false

otherwise.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- true

if

mod

includes the

public

modifier;

false

otherwise.

---

#### public static boolean isPrivate​(int mod)

Return

true

if the integer argument includes the

private

modifier,

false

otherwise.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- true

if

mod

includes the

private

modifier;

false

otherwise.

---

#### public static boolean isProtected​(int mod)

Return

true

if the integer argument includes the

protected

modifier,

false

otherwise.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- true

if

mod

includes the

protected

modifier;

false

otherwise.

---

#### public static boolean isStatic​(int mod)

Return

true

if the integer argument includes the

static

modifier,

false

otherwise.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- true

if

mod

includes the

static

modifier;

false

otherwise.

---

#### public static boolean isFinal​(int mod)

Return

true

if the integer argument includes the

final

modifier,

false

otherwise.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- true

if

mod

includes the

final

modifier;

false

otherwise.

---

#### public static boolean isSynchronized​(int mod)

Return

true

if the integer argument includes the

synchronized

modifier,

false

otherwise.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- true

if

mod

includes the

synchronized

modifier;

false

otherwise.

---

#### public static boolean isVolatile​(int mod)

Return

true

if the integer argument includes the

volatile

modifier,

false

otherwise.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- true

if

mod

includes the

volatile

modifier;

false

otherwise.

---

#### public static boolean isTransient​(int mod)

Return

true

if the integer argument includes the

transient

modifier,

false

otherwise.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- true

if

mod

includes the

transient

modifier;

false

otherwise.

---

#### public static boolean isNative​(int mod)

Return

true

if the integer argument includes the

native

modifier,

false

otherwise.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- true

if

mod

includes the

native

modifier;

false

otherwise.

---

#### public static boolean isInterface​(int mod)

Return

true

if the integer argument includes the

interface

modifier,

false

otherwise.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- true

if

mod

includes the

interface

modifier;

false

otherwise.

---

#### public static boolean isAbstract​(int mod)

Return

true

if the integer argument includes the

abstract

modifier,

false

otherwise.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- true

if

mod

includes the

abstract

modifier;

false

otherwise.

---

#### public static boolean isStrict​(int mod)

Return

true

if the integer argument includes the

strictfp

modifier,

false

otherwise.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- true

if

mod

includes the

strictfp

modifier;

false

otherwise.

---

#### public static
String
toString​(int mod)

Return a string describing the access modifier flags in
the specified modifier. For example:

```java
public final synchronized strictfp
```

The modifier names are returned in an order consistent with the
suggested modifier orderings given in sections 8.1.1, 8.3.1, 8.4.3, 8.8.3, and 9.1.1 of

The Java™ Language Specification

.
The full modifier ordering used by this method is:

public protected private abstract static final transient
volatile synchronized native strictfp
interface

The

interface

modifier discussed in this class is
not a true modifier in the Java language and it appears after
all other modifiers listed by this method. This method may
return a string of modifiers that are not valid modifiers of a
Java entity; in other words, no checking is done on the
possible validity of the combination of modifiers represented
by the input.

Note that to perform such checking for a known kind of entity,
such as a constructor or method, first AND the argument of

toString

with the appropriate mask from a method like

constructorModifiers()

or

methodModifiers()

.

**Parameters:**
- mod

- a set of modifiers

**Returns:**
- a string representation of the set of modifiers
represented by

mod

---

#### public static int classModifiers()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a class.

**Returns:**
- an

int

value OR-ing together the source language
modifiers that can be applied to a class.

**Since:**
- 1.7

**See The Java™ Language Specification :**
- 8.1.1 Class Modifiers

---

#### public static int interfaceModifiers()

Return an

int

value OR-ing together the source language
modifiers that can be applied to an interface.

**Returns:**
- an

int

value OR-ing together the source language
modifiers that can be applied to an interface.

**Since:**
- 1.7

**See The Java™ Language Specification :**
- 9.1.1 Interface Modifiers

---

#### public static int constructorModifiers()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a constructor.

**Returns:**
- an

int

value OR-ing together the source language
modifiers that can be applied to a constructor.

**Since:**
- 1.7

**See The Java™ Language Specification :**
- 8.8.3 Constructor Modifiers

---

#### public static int methodModifiers()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a method.

**Returns:**
- an

int

value OR-ing together the source language
modifiers that can be applied to a method.

**Since:**
- 1.7

**See The Java™ Language Specification :**
- 8.4.3 Method Modifiers

---

#### public static int fieldModifiers()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a field.

**Returns:**
- an

int

value OR-ing together the source language
modifiers that can be applied to a field.

**Since:**
- 1.7

**See The Java™ Language Specification :**
- 8.3.1 Field Modifiers

---

#### public static int parameterModifiers()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a parameter.

**Returns:**
- an

int

value OR-ing together the source language
modifiers that can be applied to a parameter.

**Since:**
- 1.8

**See The Java™ Language Specification :**
- 8.4.1 Formal Parameters

---

### Additional Sections

#### Class Modifier

java.lang.Object

- java.lang.reflect.Modifier

java.lang.reflect.Modifier

```java
public class
Modifier

extends
Object
```

The Modifier class provides

static

methods and
constants to decode class and member access modifiers. The sets of
modifiers are represented as integers with distinct bit positions
representing different modifiers. The values for the constants
representing the modifiers are taken from the tables in sections 4.1, 4.4, 4.5, and 4.7 of

The Java™ Virtual Machine Specification

.

**Since:** 1.1
**See Also:** Class.getModifiers()

,

Member.getModifiers()

public class

Modifier

extends

Object

The Modifier class provides

static

methods and
constants to decode class and member access modifiers. The sets of
modifiers are represented as integers with distinct bit positions
representing different modifiers. The values for the constants
representing the modifiers are taken from the tables in sections 4.1, 4.4, 4.5, and 4.7 of

The Java™ Virtual Machine Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ABSTRACT

The

int

value representing the

abstract

modifier.

static int

FINAL

The

int

value representing the

final

modifier.

static int

INTERFACE

The

int

value representing the

interface

modifier.

static int

NATIVE

The

int

value representing the

native

modifier.

static int

PRIVATE

The

int

value representing the

private

modifier.

static int

PROTECTED

The

int

value representing the

protected

modifier.

static int

PUBLIC

The

int

value representing the

public

modifier.

static int

STATIC

The

int

value representing the

static

modifier.

static int

STRICT

The

int

value representing the

strictfp

modifier.

static int

SYNCHRONIZED

The

int

value representing the

synchronized

modifier.

static int

TRANSIENT

The

int

value representing the

transient

modifier.

static int

VOLATILE

The

int

value representing the

volatile

modifier.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Modifier

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static int

classModifiers

()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a class.

static int

constructorModifiers

()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a constructor.

static int

fieldModifiers

()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a field.

static int

interfaceModifiers

()

Return an

int

value OR-ing together the source language
modifiers that can be applied to an interface.

static boolean

isAbstract

​(int mod)

Return

true

if the integer argument includes the

abstract

modifier,

false

otherwise.

static boolean

isFinal

​(int mod)

Return

true

if the integer argument includes the

final

modifier,

false

otherwise.

static boolean

isInterface

​(int mod)

Return

true

if the integer argument includes the

interface

modifier,

false

otherwise.

static boolean

isNative

​(int mod)

Return

true

if the integer argument includes the

native

modifier,

false

otherwise.

static boolean

isPrivate

​(int mod)

Return

true

if the integer argument includes the

private

modifier,

false

otherwise.

static boolean

isProtected

​(int mod)

Return

true

if the integer argument includes the

protected

modifier,

false

otherwise.

static boolean

isPublic

​(int mod)

Return

true

if the integer argument includes the

public

modifier,

false

otherwise.

static boolean

isStatic

​(int mod)

Return

true

if the integer argument includes the

static

modifier,

false

otherwise.

static boolean

isStrict

​(int mod)

Return

true

if the integer argument includes the

strictfp

modifier,

false

otherwise.

static boolean

isSynchronized

​(int mod)

Return

true

if the integer argument includes the

synchronized

modifier,

false

otherwise.

static boolean

isTransient

​(int mod)

Return

true

if the integer argument includes the

transient

modifier,

false

otherwise.

static boolean

isVolatile

​(int mod)

Return

true

if the integer argument includes the

volatile

modifier,

false

otherwise.

static int

methodModifiers

()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a method.

static int

parameterModifiers

()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a parameter.

static

String

toString

​(int mod)

Return a string describing the access modifier flags in
the specified modifier.

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

toString

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

static int

ABSTRACT

The

int

value representing the

abstract

modifier.

static int

FINAL

The

int

value representing the

final

modifier.

static int

INTERFACE

The

int

value representing the

interface

modifier.

static int

NATIVE

The

int

value representing the

native

modifier.

static int

PRIVATE

The

int

value representing the

private

modifier.

static int

PROTECTED

The

int

value representing the

protected

modifier.

static int

PUBLIC

The

int

value representing the

public

modifier.

static int

STATIC

The

int

value representing the

static

modifier.

static int

STRICT

The

int

value representing the

strictfp

modifier.

static int

SYNCHRONIZED

The

int

value representing the

synchronized

modifier.

static int

TRANSIENT

The

int

value representing the

transient

modifier.

static int

VOLATILE

The

int

value representing the

volatile

modifier.

---

#### Field Summary

The

int

value representing the

abstract

modifier.

The

int

value representing the

final

modifier.

The

int

value representing the

interface

modifier.

The

int

value representing the

native

modifier.

The

int

value representing the

private

modifier.

The

int

value representing the

protected

modifier.

The

int

value representing the

public

modifier.

The

int

value representing the

static

modifier.

The

int

value representing the

strictfp

modifier.

The

int

value representing the

synchronized

modifier.

The

int

value representing the

transient

modifier.

The

int

value representing the

volatile

modifier.

Constructor Summary

Constructors

Constructor

Description

Modifier

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static int

classModifiers

()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a class.

static int

constructorModifiers

()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a constructor.

static int

fieldModifiers

()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a field.

static int

interfaceModifiers

()

Return an

int

value OR-ing together the source language
modifiers that can be applied to an interface.

static boolean

isAbstract

​(int mod)

Return

true

if the integer argument includes the

abstract

modifier,

false

otherwise.

static boolean

isFinal

​(int mod)

Return

true

if the integer argument includes the

final

modifier,

false

otherwise.

static boolean

isInterface

​(int mod)

Return

true

if the integer argument includes the

interface

modifier,

false

otherwise.

static boolean

isNative

​(int mod)

Return

true

if the integer argument includes the

native

modifier,

false

otherwise.

static boolean

isPrivate

​(int mod)

Return

true

if the integer argument includes the

private

modifier,

false

otherwise.

static boolean

isProtected

​(int mod)

Return

true

if the integer argument includes the

protected

modifier,

false

otherwise.

static boolean

isPublic

​(int mod)

Return

true

if the integer argument includes the

public

modifier,

false

otherwise.

static boolean

isStatic

​(int mod)

Return

true

if the integer argument includes the

static

modifier,

false

otherwise.

static boolean

isStrict

​(int mod)

Return

true

if the integer argument includes the

strictfp

modifier,

false

otherwise.

static boolean

isSynchronized

​(int mod)

Return

true

if the integer argument includes the

synchronized

modifier,

false

otherwise.

static boolean

isTransient

​(int mod)

Return

true

if the integer argument includes the

transient

modifier,

false

otherwise.

static boolean

isVolatile

​(int mod)

Return

true

if the integer argument includes the

volatile

modifier,

false

otherwise.

static int

methodModifiers

()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a method.

static int

parameterModifiers

()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a parameter.

static

String

toString

​(int mod)

Return a string describing the access modifier flags in
the specified modifier.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Return an

int

value OR-ing together the source language
modifiers that can be applied to a class.

Return an

int

value OR-ing together the source language
modifiers that can be applied to a constructor.

Return an

int

value OR-ing together the source language
modifiers that can be applied to a field.

Return an

int

value OR-ing together the source language
modifiers that can be applied to an interface.

Return

true

if the integer argument includes the

abstract

modifier,

false

otherwise.

Return

true

if the integer argument includes the

final

modifier,

false

otherwise.

Return

true

if the integer argument includes the

interface

modifier,

false

otherwise.

Return

true

if the integer argument includes the

native

modifier,

false

otherwise.

Return

true

if the integer argument includes the

private

modifier,

false

otherwise.

Return

true

if the integer argument includes the

protected

modifier,

false

otherwise.

Return

true

if the integer argument includes the

public

modifier,

false

otherwise.

Return

true

if the integer argument includes the

static

modifier,

false

otherwise.

Return

true

if the integer argument includes the

strictfp

modifier,

false

otherwise.

Return

true

if the integer argument includes the

synchronized

modifier,

false

otherwise.

Return

true

if the integer argument includes the

transient

modifier,

false

otherwise.

Return

true

if the integer argument includes the

volatile

modifier,

false

otherwise.

Return an

int

value OR-ing together the source language
modifiers that can be applied to a method.

Return an

int

value OR-ing together the source language
modifiers that can be applied to a parameter.

Return a string describing the access modifier flags in
the specified modifier.

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

toString

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

- PUBLIC

```java
public static final int PUBLIC
```

The

int

value representing the

public

modifier.

**See Also:** Constant Field Values

- PRIVATE

```java
public static final int PRIVATE
```

The

int

value representing the

private

modifier.

**See Also:** Constant Field Values

- PROTECTED

```java
public static final int PROTECTED
```

The

int

value representing the

protected

modifier.

**See Also:** Constant Field Values

- STATIC

```java
public static final int STATIC
```

The

int

value representing the

static

modifier.

**See Also:** Constant Field Values

- FINAL

```java
public static final int FINAL
```

The

int

value representing the

final

modifier.

**See Also:** Constant Field Values

- SYNCHRONIZED

```java
public static final int SYNCHRONIZED
```

The

int

value representing the

synchronized

modifier.

**See Also:** Constant Field Values

- VOLATILE

```java
public static final int VOLATILE
```

The

int

value representing the

volatile

modifier.

**See Also:** Constant Field Values

- TRANSIENT

```java
public static final int TRANSIENT
```

The

int

value representing the

transient

modifier.

**See Also:** Constant Field Values

- NATIVE

```java
public static final int NATIVE
```

The

int

value representing the

native

modifier.

**See Also:** Constant Field Values

- INTERFACE

```java
public static final int INTERFACE
```

The

int

value representing the

interface

modifier.

**See Also:** Constant Field Values

- ABSTRACT

```java
public static final int ABSTRACT
```

The

int

value representing the

abstract

modifier.

**See Also:** Constant Field Values

- STRICT

```java
public static final int STRICT
```

The

int

value representing the

strictfp

modifier.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Modifier

```java
public Modifier()
```

============ METHOD DETAIL ==========

- Method Detail

- isPublic

```java
public static boolean isPublic​(int mod)
```

Return

true

if the integer argument includes the

public

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

public

modifier;

false

otherwise.

- isPrivate

```java
public static boolean isPrivate​(int mod)
```

Return

true

if the integer argument includes the

private

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

private

modifier;

false

otherwise.

- isProtected

```java
public static boolean isProtected​(int mod)
```

Return

true

if the integer argument includes the

protected

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

protected

modifier;

false

otherwise.

- isStatic

```java
public static boolean isStatic​(int mod)
```

Return

true

if the integer argument includes the

static

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

static

modifier;

false

otherwise.

- isFinal

```java
public static boolean isFinal​(int mod)
```

Return

true

if the integer argument includes the

final

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

final

modifier;

false

otherwise.

- isSynchronized

```java
public static boolean isSynchronized​(int mod)
```

Return

true

if the integer argument includes the

synchronized

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

synchronized

modifier;

false

otherwise.

- isVolatile

```java
public static boolean isVolatile​(int mod)
```

Return

true

if the integer argument includes the

volatile

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

volatile

modifier;

false

otherwise.

- isTransient

```java
public static boolean isTransient​(int mod)
```

Return

true

if the integer argument includes the

transient

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

transient

modifier;

false

otherwise.

- isNative

```java
public static boolean isNative​(int mod)
```

Return

true

if the integer argument includes the

native

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

native

modifier;

false

otherwise.

- isInterface

```java
public static boolean isInterface​(int mod)
```

Return

true

if the integer argument includes the

interface

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

interface

modifier;

false

otherwise.

- isAbstract

```java
public static boolean isAbstract​(int mod)
```

Return

true

if the integer argument includes the

abstract

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

abstract

modifier;

false

otherwise.

- isStrict

```java
public static boolean isStrict​(int mod)
```

Return

true

if the integer argument includes the

strictfp

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

strictfp

modifier;

false

otherwise.

- toString

```java
public static
String
toString​(int mod)
```

Return a string describing the access modifier flags in
the specified modifier. For example:

```java
public final synchronized strictfp
```

The modifier names are returned in an order consistent with the
suggested modifier orderings given in sections 8.1.1, 8.3.1, 8.4.3, 8.8.3, and 9.1.1 of

The Java™ Language Specification

.
The full modifier ordering used by this method is:

public protected private abstract static final transient
volatile synchronized native strictfp
interface

The

interface

modifier discussed in this class is
not a true modifier in the Java language and it appears after
all other modifiers listed by this method. This method may
return a string of modifiers that are not valid modifiers of a
Java entity; in other words, no checking is done on the
possible validity of the combination of modifiers represented
by the input.

Note that to perform such checking for a known kind of entity,
such as a constructor or method, first AND the argument of

toString

with the appropriate mask from a method like

constructorModifiers()

or

methodModifiers()

.

**Parameters:** mod

- a set of modifiers
**Returns:** a string representation of the set of modifiers
represented by

mod

- classModifiers

```java
public static int classModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a class.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a class.
**Since:** 1.7
**See The Java™ Language Specification :** 8.1.1 Class Modifiers

- interfaceModifiers

```java
public static int interfaceModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to an interface.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to an interface.
**Since:** 1.7
**See The Java™ Language Specification :** 9.1.1 Interface Modifiers

- constructorModifiers

```java
public static int constructorModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a constructor.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a constructor.
**Since:** 1.7
**See The Java™ Language Specification :** 8.8.3 Constructor Modifiers

- methodModifiers

```java
public static int methodModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a method.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a method.
**Since:** 1.7
**See The Java™ Language Specification :** 8.4.3 Method Modifiers

- fieldModifiers

```java
public static int fieldModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a field.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a field.
**Since:** 1.7
**See The Java™ Language Specification :** 8.3.1 Field Modifiers

- parameterModifiers

```java
public static int parameterModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a parameter.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a parameter.
**Since:** 1.8
**See The Java™ Language Specification :** 8.4.1 Formal Parameters

Field Detail

- PUBLIC

```java
public static final int PUBLIC
```

The

int

value representing the

public

modifier.

**See Also:** Constant Field Values

- PRIVATE

```java
public static final int PRIVATE
```

The

int

value representing the

private

modifier.

**See Also:** Constant Field Values

- PROTECTED

```java
public static final int PROTECTED
```

The

int

value representing the

protected

modifier.

**See Also:** Constant Field Values

- STATIC

```java
public static final int STATIC
```

The

int

value representing the

static

modifier.

**See Also:** Constant Field Values

- FINAL

```java
public static final int FINAL
```

The

int

value representing the

final

modifier.

**See Also:** Constant Field Values

- SYNCHRONIZED

```java
public static final int SYNCHRONIZED
```

The

int

value representing the

synchronized

modifier.

**See Also:** Constant Field Values

- VOLATILE

```java
public static final int VOLATILE
```

The

int

value representing the

volatile

modifier.

**See Also:** Constant Field Values

- TRANSIENT

```java
public static final int TRANSIENT
```

The

int

value representing the

transient

modifier.

**See Also:** Constant Field Values

- NATIVE

```java
public static final int NATIVE
```

The

int

value representing the

native

modifier.

**See Also:** Constant Field Values

- INTERFACE

```java
public static final int INTERFACE
```

The

int

value representing the

interface

modifier.

**See Also:** Constant Field Values

- ABSTRACT

```java
public static final int ABSTRACT
```

The

int

value representing the

abstract

modifier.

**See Also:** Constant Field Values

- STRICT

```java
public static final int STRICT
```

The

int

value representing the

strictfp

modifier.

**See Also:** Constant Field Values

---

#### Field Detail

PUBLIC

```java
public static final int PUBLIC
```

The

int

value representing the

public

modifier.

**See Also:** Constant Field Values

---

#### PUBLIC

public static final int PUBLIC

The

int

value representing the

public

modifier.

PRIVATE

```java
public static final int PRIVATE
```

The

int

value representing the

private

modifier.

**See Also:** Constant Field Values

---

#### PRIVATE

public static final int PRIVATE

The

int

value representing the

private

modifier.

PROTECTED

```java
public static final int PROTECTED
```

The

int

value representing the

protected

modifier.

**See Also:** Constant Field Values

---

#### PROTECTED

public static final int PROTECTED

The

int

value representing the

protected

modifier.

STATIC

```java
public static final int STATIC
```

The

int

value representing the

static

modifier.

**See Also:** Constant Field Values

---

#### STATIC

public static final int STATIC

The

int

value representing the

static

modifier.

FINAL

```java
public static final int FINAL
```

The

int

value representing the

final

modifier.

**See Also:** Constant Field Values

---

#### FINAL

public static final int FINAL

The

int

value representing the

final

modifier.

SYNCHRONIZED

```java
public static final int SYNCHRONIZED
```

The

int

value representing the

synchronized

modifier.

**See Also:** Constant Field Values

---

#### SYNCHRONIZED

public static final int SYNCHRONIZED

The

int

value representing the

synchronized

modifier.

VOLATILE

```java
public static final int VOLATILE
```

The

int

value representing the

volatile

modifier.

**See Also:** Constant Field Values

---

#### VOLATILE

public static final int VOLATILE

The

int

value representing the

volatile

modifier.

TRANSIENT

```java
public static final int TRANSIENT
```

The

int

value representing the

transient

modifier.

**See Also:** Constant Field Values

---

#### TRANSIENT

public static final int TRANSIENT

The

int

value representing the

transient

modifier.

NATIVE

```java
public static final int NATIVE
```

The

int

value representing the

native

modifier.

**See Also:** Constant Field Values

---

#### NATIVE

public static final int NATIVE

The

int

value representing the

native

modifier.

INTERFACE

```java
public static final int INTERFACE
```

The

int

value representing the

interface

modifier.

**See Also:** Constant Field Values

---

#### INTERFACE

public static final int INTERFACE

The

int

value representing the

interface

modifier.

ABSTRACT

```java
public static final int ABSTRACT
```

The

int

value representing the

abstract

modifier.

**See Also:** Constant Field Values

---

#### ABSTRACT

public static final int ABSTRACT

The

int

value representing the

abstract

modifier.

STRICT

```java
public static final int STRICT
```

The

int

value representing the

strictfp

modifier.

**See Also:** Constant Field Values

---

#### STRICT

public static final int STRICT

The

int

value representing the

strictfp

modifier.

Constructor Detail

- Modifier

```java
public Modifier()
```

---

#### Constructor Detail

Modifier

```java
public Modifier()
```

---

#### Modifier

public Modifier()

Method Detail

- isPublic

```java
public static boolean isPublic​(int mod)
```

Return

true

if the integer argument includes the

public

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

public

modifier;

false

otherwise.

- isPrivate

```java
public static boolean isPrivate​(int mod)
```

Return

true

if the integer argument includes the

private

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

private

modifier;

false

otherwise.

- isProtected

```java
public static boolean isProtected​(int mod)
```

Return

true

if the integer argument includes the

protected

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

protected

modifier;

false

otherwise.

- isStatic

```java
public static boolean isStatic​(int mod)
```

Return

true

if the integer argument includes the

static

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

static

modifier;

false

otherwise.

- isFinal

```java
public static boolean isFinal​(int mod)
```

Return

true

if the integer argument includes the

final

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

final

modifier;

false

otherwise.

- isSynchronized

```java
public static boolean isSynchronized​(int mod)
```

Return

true

if the integer argument includes the

synchronized

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

synchronized

modifier;

false

otherwise.

- isVolatile

```java
public static boolean isVolatile​(int mod)
```

Return

true

if the integer argument includes the

volatile

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

volatile

modifier;

false

otherwise.

- isTransient

```java
public static boolean isTransient​(int mod)
```

Return

true

if the integer argument includes the

transient

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

transient

modifier;

false

otherwise.

- isNative

```java
public static boolean isNative​(int mod)
```

Return

true

if the integer argument includes the

native

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

native

modifier;

false

otherwise.

- isInterface

```java
public static boolean isInterface​(int mod)
```

Return

true

if the integer argument includes the

interface

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

interface

modifier;

false

otherwise.

- isAbstract

```java
public static boolean isAbstract​(int mod)
```

Return

true

if the integer argument includes the

abstract

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

abstract

modifier;

false

otherwise.

- isStrict

```java
public static boolean isStrict​(int mod)
```

Return

true

if the integer argument includes the

strictfp

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

strictfp

modifier;

false

otherwise.

- toString

```java
public static
String
toString​(int mod)
```

Return a string describing the access modifier flags in
the specified modifier. For example:

```java
public final synchronized strictfp
```

The modifier names are returned in an order consistent with the
suggested modifier orderings given in sections 8.1.1, 8.3.1, 8.4.3, 8.8.3, and 9.1.1 of

The Java™ Language Specification

.
The full modifier ordering used by this method is:

public protected private abstract static final transient
volatile synchronized native strictfp
interface

The

interface

modifier discussed in this class is
not a true modifier in the Java language and it appears after
all other modifiers listed by this method. This method may
return a string of modifiers that are not valid modifiers of a
Java entity; in other words, no checking is done on the
possible validity of the combination of modifiers represented
by the input.

Note that to perform such checking for a known kind of entity,
such as a constructor or method, first AND the argument of

toString

with the appropriate mask from a method like

constructorModifiers()

or

methodModifiers()

.

**Parameters:** mod

- a set of modifiers
**Returns:** a string representation of the set of modifiers
represented by

mod

- classModifiers

```java
public static int classModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a class.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a class.
**Since:** 1.7
**See The Java™ Language Specification :** 8.1.1 Class Modifiers

- interfaceModifiers

```java
public static int interfaceModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to an interface.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to an interface.
**Since:** 1.7
**See The Java™ Language Specification :** 9.1.1 Interface Modifiers

- constructorModifiers

```java
public static int constructorModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a constructor.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a constructor.
**Since:** 1.7
**See The Java™ Language Specification :** 8.8.3 Constructor Modifiers

- methodModifiers

```java
public static int methodModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a method.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a method.
**Since:** 1.7
**See The Java™ Language Specification :** 8.4.3 Method Modifiers

- fieldModifiers

```java
public static int fieldModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a field.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a field.
**Since:** 1.7
**See The Java™ Language Specification :** 8.3.1 Field Modifiers

- parameterModifiers

```java
public static int parameterModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a parameter.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a parameter.
**Since:** 1.8
**See The Java™ Language Specification :** 8.4.1 Formal Parameters

---

#### Method Detail

isPublic

```java
public static boolean isPublic​(int mod)
```

Return

true

if the integer argument includes the

public

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

public

modifier;

false

otherwise.

---

#### isPublic

public static boolean isPublic​(int mod)

Return

true

if the integer argument includes the

public

modifier,

false

otherwise.

isPrivate

```java
public static boolean isPrivate​(int mod)
```

Return

true

if the integer argument includes the

private

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

private

modifier;

false

otherwise.

---

#### isPrivate

public static boolean isPrivate​(int mod)

Return

true

if the integer argument includes the

private

modifier,

false

otherwise.

isProtected

```java
public static boolean isProtected​(int mod)
```

Return

true

if the integer argument includes the

protected

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

protected

modifier;

false

otherwise.

---

#### isProtected

public static boolean isProtected​(int mod)

Return

true

if the integer argument includes the

protected

modifier,

false

otherwise.

isStatic

```java
public static boolean isStatic​(int mod)
```

Return

true

if the integer argument includes the

static

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

static

modifier;

false

otherwise.

---

#### isStatic

public static boolean isStatic​(int mod)

Return

true

if the integer argument includes the

static

modifier,

false

otherwise.

isFinal

```java
public static boolean isFinal​(int mod)
```

Return

true

if the integer argument includes the

final

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

final

modifier;

false

otherwise.

---

#### isFinal

public static boolean isFinal​(int mod)

Return

true

if the integer argument includes the

final

modifier,

false

otherwise.

isSynchronized

```java
public static boolean isSynchronized​(int mod)
```

Return

true

if the integer argument includes the

synchronized

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

synchronized

modifier;

false

otherwise.

---

#### isSynchronized

public static boolean isSynchronized​(int mod)

Return

true

if the integer argument includes the

synchronized

modifier,

false

otherwise.

isVolatile

```java
public static boolean isVolatile​(int mod)
```

Return

true

if the integer argument includes the

volatile

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

volatile

modifier;

false

otherwise.

---

#### isVolatile

public static boolean isVolatile​(int mod)

Return

true

if the integer argument includes the

volatile

modifier,

false

otherwise.

isTransient

```java
public static boolean isTransient​(int mod)
```

Return

true

if the integer argument includes the

transient

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

transient

modifier;

false

otherwise.

---

#### isTransient

public static boolean isTransient​(int mod)

Return

true

if the integer argument includes the

transient

modifier,

false

otherwise.

isNative

```java
public static boolean isNative​(int mod)
```

Return

true

if the integer argument includes the

native

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

native

modifier;

false

otherwise.

---

#### isNative

public static boolean isNative​(int mod)

Return

true

if the integer argument includes the

native

modifier,

false

otherwise.

isInterface

```java
public static boolean isInterface​(int mod)
```

Return

true

if the integer argument includes the

interface

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

interface

modifier;

false

otherwise.

---

#### isInterface

public static boolean isInterface​(int mod)

Return

true

if the integer argument includes the

interface

modifier,

false

otherwise.

isAbstract

```java
public static boolean isAbstract​(int mod)
```

Return

true

if the integer argument includes the

abstract

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

abstract

modifier;

false

otherwise.

---

#### isAbstract

public static boolean isAbstract​(int mod)

Return

true

if the integer argument includes the

abstract

modifier,

false

otherwise.

isStrict

```java
public static boolean isStrict​(int mod)
```

Return

true

if the integer argument includes the

strictfp

modifier,

false

otherwise.

**Parameters:** mod

- a set of modifiers
**Returns:** true

if

mod

includes the

strictfp

modifier;

false

otherwise.

---

#### isStrict

public static boolean isStrict​(int mod)

Return

true

if the integer argument includes the

strictfp

modifier,

false

otherwise.

toString

```java
public static
String
toString​(int mod)
```

Return a string describing the access modifier flags in
the specified modifier. For example:

```java
public final synchronized strictfp
```

The modifier names are returned in an order consistent with the
suggested modifier orderings given in sections 8.1.1, 8.3.1, 8.4.3, 8.8.3, and 9.1.1 of

The Java™ Language Specification

.
The full modifier ordering used by this method is:

public protected private abstract static final transient
volatile synchronized native strictfp
interface

The

interface

modifier discussed in this class is
not a true modifier in the Java language and it appears after
all other modifiers listed by this method. This method may
return a string of modifiers that are not valid modifiers of a
Java entity; in other words, no checking is done on the
possible validity of the combination of modifiers represented
by the input.

Note that to perform such checking for a known kind of entity,
such as a constructor or method, first AND the argument of

toString

with the appropriate mask from a method like

constructorModifiers()

or

methodModifiers()

.

**Parameters:** mod

- a set of modifiers
**Returns:** a string representation of the set of modifiers
represented by

mod

---

#### toString

public static

String

toString​(int mod)

Return a string describing the access modifier flags in
the specified modifier. For example:

```java
public final synchronized strictfp
```

The modifier names are returned in an order consistent with the
suggested modifier orderings given in sections 8.1.1, 8.3.1, 8.4.3, 8.8.3, and 9.1.1 of

The Java™ Language Specification

.
The full modifier ordering used by this method is:

public protected private abstract static final transient
volatile synchronized native strictfp
interface

The

interface

modifier discussed in this class is
not a true modifier in the Java language and it appears after
all other modifiers listed by this method. This method may
return a string of modifiers that are not valid modifiers of a
Java entity; in other words, no checking is done on the
possible validity of the combination of modifiers represented
by the input.

Note that to perform such checking for a known kind of entity,
such as a constructor or method, first AND the argument of

toString

with the appropriate mask from a method like

constructorModifiers()

or

methodModifiers()

.

public final synchronized strictfp

classModifiers

```java
public static int classModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a class.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a class.
**Since:** 1.7
**See The Java™ Language Specification :** 8.1.1 Class Modifiers

---

#### classModifiers

public static int classModifiers()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a class.

interfaceModifiers

```java
public static int interfaceModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to an interface.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to an interface.
**Since:** 1.7
**See The Java™ Language Specification :** 9.1.1 Interface Modifiers

---

#### interfaceModifiers

public static int interfaceModifiers()

Return an

int

value OR-ing together the source language
modifiers that can be applied to an interface.

constructorModifiers

```java
public static int constructorModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a constructor.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a constructor.
**Since:** 1.7
**See The Java™ Language Specification :** 8.8.3 Constructor Modifiers

---

#### constructorModifiers

public static int constructorModifiers()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a constructor.

methodModifiers

```java
public static int methodModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a method.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a method.
**Since:** 1.7
**See The Java™ Language Specification :** 8.4.3 Method Modifiers

---

#### methodModifiers

public static int methodModifiers()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a method.

fieldModifiers

```java
public static int fieldModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a field.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a field.
**Since:** 1.7
**See The Java™ Language Specification :** 8.3.1 Field Modifiers

---

#### fieldModifiers

public static int fieldModifiers()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a field.

parameterModifiers

```java
public static int parameterModifiers()
```

Return an

int

value OR-ing together the source language
modifiers that can be applied to a parameter.

**Returns:** an

int

value OR-ing together the source language
modifiers that can be applied to a parameter.
**Since:** 1.8
**See The Java™ Language Specification :** 8.4.1 Formal Parameters

---

#### parameterModifiers

public static int parameterModifiers()

Return an

int

value OR-ing together the source language
modifiers that can be applied to a parameter.

---

