# Class Compiler

**Source:** `java.base\java\lang\Compiler.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public final class
Compiler

extends
Object
```

The

Compiler

class is provided to support Java-to-native-code
compilers and related services. By design, the

Compiler

class does
nothing; it serves as a placeholder for a JIT compiler implementation.
If no compiler is available, these methods do nothing.

**Since:** 1.0

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static boolean compileClass​(
Class
<?> clazz)

Compiles the specified class.

**Parameters:**
- clazz

- A class

**Returns:**
- true

if the compilation succeeded;

false

if the
compilation failed or no compiler is available

**Throws:**
- NullPointerException

- If

clazz

is

null

---

#### public static boolean compileClasses​(
String
string)

Compiles all classes whose name matches the specified string.

**Parameters:**
- string

- The name of the classes to compile

**Returns:**
- true

if the compilation succeeded;

false

if the
compilation failed or no compiler is available

**Throws:**
- NullPointerException

- If

string

is

null

---

#### public static
Object
command​(
Object
any)

Examines the argument type and its fields and perform some documented
operation. No specific operations are required.

**Parameters:**
- any

- An argument

**Returns:**
- A compiler-specific value, or

null

if no compiler is
available

**Throws:**
- NullPointerException

- If

any

is

null

---

#### public static void enable()

Cause the Compiler to resume operation.

---

#### public static void disable()

Cause the Compiler to cease operation.

---

### Additional Sections

#### Class Compiler

java.lang.Object

- java.lang.Compiler

java.lang.Compiler

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public final class
Compiler

extends
Object
```

Deprecated, for removal: This API element is subject to removal in a future version.

JIT compilers and their technologies vary too widely to
be controlled effectively by a standardized interface. As such, many
JIT compiler implementations ignore this interface, and are instead
controllable by implementation-specific mechanisms such as command-line
options. This class is subject to removal in a future version of Java SE.

The

Compiler

class is provided to support Java-to-native-code
compilers and related services. By design, the

Compiler

class does
nothing; it serves as a placeholder for a JIT compiler implementation.
If no compiler is available, these methods do nothing.

**Since:** 1.0

@Deprecated

(

since

="9",

forRemoval

=true)
public final class

Compiler

extends

Object

The

Compiler

class is provided to support Java-to-native-code
compilers and related services. By design, the

Compiler

class does
nothing; it serves as a placeholder for a JIT compiler implementation.
If no compiler is available, these methods do nothing.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Object

command

​(

Object

any)

Deprecated, for removal: This API element is subject to removal in a future version.

Examines the argument type and its fields and perform some documented
operation.

static boolean

compileClass

​(

Class

<?> clazz)

Deprecated, for removal: This API element is subject to removal in a future version.

Compiles the specified class.

static boolean

compileClasses

​(

String

string)

Deprecated, for removal: This API element is subject to removal in a future version.

Compiles all classes whose name matches the specified string.

static void

disable

()

Deprecated, for removal: This API element is subject to removal in a future version.

Cause the Compiler to cease operation.

static void

enable

()

Deprecated, for removal: This API element is subject to removal in a future version.

Cause the Compiler to resume operation.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

Object

command

​(

Object

any)

Deprecated, for removal: This API element is subject to removal in a future version.

Examines the argument type and its fields and perform some documented
operation.

static boolean

compileClass

​(

Class

<?> clazz)

Deprecated, for removal: This API element is subject to removal in a future version.

Compiles the specified class.

static boolean

compileClasses

​(

String

string)

Deprecated, for removal: This API element is subject to removal in a future version.

Compiles all classes whose name matches the specified string.

static void

disable

()

Deprecated, for removal: This API element is subject to removal in a future version.

Cause the Compiler to cease operation.

static void

enable

()

Deprecated, for removal: This API element is subject to removal in a future version.

Cause the Compiler to resume operation.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Examines the argument type and its fields and perform some documented
operation.

Compiles the specified class.

Compiles all classes whose name matches the specified string.

Cause the Compiler to cease operation.

Cause the Compiler to resume operation.

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

============ METHOD DETAIL ==========

- Method Detail

- compileClass

```java
public static boolean compileClass​(
Class
<?> clazz)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Compiles the specified class.

**Parameters:** clazz

- A class
**Returns:** true

if the compilation succeeded;

false

if the
compilation failed or no compiler is available
**Throws:** NullPointerException

- If

clazz

is

null

- compileClasses

```java
public static boolean compileClasses​(
String
string)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Compiles all classes whose name matches the specified string.

**Parameters:** string

- The name of the classes to compile
**Returns:** true

if the compilation succeeded;

false

if the
compilation failed or no compiler is available
**Throws:** NullPointerException

- If

string

is

null

- command

```java
public static
Object
command​(
Object
any)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Examines the argument type and its fields and perform some documented
operation. No specific operations are required.

**Parameters:** any

- An argument
**Returns:** A compiler-specific value, or

null

if no compiler is
available
**Throws:** NullPointerException

- If

any

is

null

- enable

```java
public static void enable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Cause the Compiler to resume operation.

- disable

```java
public static void disable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Cause the Compiler to cease operation.

Method Detail

- compileClass

```java
public static boolean compileClass​(
Class
<?> clazz)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Compiles the specified class.

**Parameters:** clazz

- A class
**Returns:** true

if the compilation succeeded;

false

if the
compilation failed or no compiler is available
**Throws:** NullPointerException

- If

clazz

is

null

- compileClasses

```java
public static boolean compileClasses​(
String
string)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Compiles all classes whose name matches the specified string.

**Parameters:** string

- The name of the classes to compile
**Returns:** true

if the compilation succeeded;

false

if the
compilation failed or no compiler is available
**Throws:** NullPointerException

- If

string

is

null

- command

```java
public static
Object
command​(
Object
any)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Examines the argument type and its fields and perform some documented
operation. No specific operations are required.

**Parameters:** any

- An argument
**Returns:** A compiler-specific value, or

null

if no compiler is
available
**Throws:** NullPointerException

- If

any

is

null

- enable

```java
public static void enable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Cause the Compiler to resume operation.

- disable

```java
public static void disable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Cause the Compiler to cease operation.

---

#### Method Detail

compileClass

```java
public static boolean compileClass​(
Class
<?> clazz)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Compiles the specified class.

**Parameters:** clazz

- A class
**Returns:** true

if the compilation succeeded;

false

if the
compilation failed or no compiler is available
**Throws:** NullPointerException

- If

clazz

is

null

---

#### compileClass

public static boolean compileClass​(

Class

<?> clazz)

Compiles the specified class.

compileClasses

```java
public static boolean compileClasses​(
String
string)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Compiles all classes whose name matches the specified string.

**Parameters:** string

- The name of the classes to compile
**Returns:** true

if the compilation succeeded;

false

if the
compilation failed or no compiler is available
**Throws:** NullPointerException

- If

string

is

null

---

#### compileClasses

public static boolean compileClasses​(

String

string)

Compiles all classes whose name matches the specified string.

command

```java
public static
Object
command​(
Object
any)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Examines the argument type and its fields and perform some documented
operation. No specific operations are required.

**Parameters:** any

- An argument
**Returns:** A compiler-specific value, or

null

if no compiler is
available
**Throws:** NullPointerException

- If

any

is

null

---

#### command

public static

Object

command​(

Object

any)

Examines the argument type and its fields and perform some documented
operation. No specific operations are required.

enable

```java
public static void enable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Cause the Compiler to resume operation.

---

#### enable

public static void enable()

Cause the Compiler to resume operation.

disable

```java
public static void disable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Cause the Compiler to cease operation.

---

#### disable

public static void disable()

Cause the Compiler to cease operation.

---

