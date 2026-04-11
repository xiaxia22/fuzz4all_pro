# Class ClassDefinition

**Source:** `java.instrument\java\lang\instrument\ClassDefinition.html`

### Class Description

```java
public final class
ClassDefinition

extends
Object
```

This class serves as a parameter block to the

Instrumentation.redefineClasses

method.
Serves to bind the

Class

that needs redefining together with the new class file bytes.

**Since:** 1.5
**See Also:** Instrumentation.redefineClasses(java.lang.instrument.ClassDefinition...)

---

### Field Details

*No entries found.*

### Constructor Details

#### public ClassDefinition​(
Class
<?> theClass,
byte[] theClassFile)

Creates a new

ClassDefinition

binding using the supplied
class and class file bytes. Does not copy the supplied buffer, just captures a reference to it.

**Parameters:**
- theClass

- the

Class

that needs redefining
- theClassFile

- the new class file bytes

**Throws:**
- NullPointerException

- if the supplied class or array is

null

.

---

### Method Details

#### public
Class
<?> getDefinitionClass()

Returns the class.

**Returns:**
- the

Class

object referred to.

---

#### public byte[] getDefinitionClassFile()

Returns the array of bytes that contains the new class file.

**Returns:**
- the class file bytes.

---

### Additional Sections

#### Class ClassDefinition

java.lang.Object

- java.lang.instrument.ClassDefinition

java.lang.instrument.ClassDefinition

```java
public final class
ClassDefinition

extends
Object
```

This class serves as a parameter block to the

Instrumentation.redefineClasses

method.
Serves to bind the

Class

that needs redefining together with the new class file bytes.

**Since:** 1.5
**See Also:** Instrumentation.redefineClasses(java.lang.instrument.ClassDefinition...)

public final class

ClassDefinition

extends

Object

This class serves as a parameter block to the

Instrumentation.redefineClasses

method.
Serves to bind the

Class

that needs redefining together with the new class file bytes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ClassDefinition

​(

Class

<?> theClass,
byte[] theClassFile)

Creates a new

ClassDefinition

binding using the supplied
class and class file bytes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

getDefinitionClass

()

Returns the class.

byte[]

getDefinitionClassFile

()

Returns the array of bytes that contains the new class file.

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

Constructor Summary

Constructors

Constructor

Description

ClassDefinition

​(

Class

<?> theClass,
byte[] theClassFile)

Creates a new

ClassDefinition

binding using the supplied
class and class file bytes.

---

#### Constructor Summary

Creates a new

ClassDefinition

binding using the supplied
class and class file bytes.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

getDefinitionClass

()

Returns the class.

byte[]

getDefinitionClassFile

()

Returns the array of bytes that contains the new class file.

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

Returns the class.

Returns the array of bytes that contains the new class file.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ClassDefinition

```java
public ClassDefinition​(
Class
<?> theClass,
byte[] theClassFile)
```

Creates a new

ClassDefinition

binding using the supplied
class and class file bytes. Does not copy the supplied buffer, just captures a reference to it.

**Parameters:** theClass

- the

Class

that needs redefining
**Parameters:** theClassFile

- the new class file bytes
**Throws:** NullPointerException

- if the supplied class or array is

null

.

============ METHOD DETAIL ==========

- Method Detail

- getDefinitionClass

```java
public
Class
<?> getDefinitionClass()
```

Returns the class.

**Returns:** the

Class

object referred to.

- getDefinitionClassFile

```java
public byte[] getDefinitionClassFile()
```

Returns the array of bytes that contains the new class file.

**Returns:** the class file bytes.

Constructor Detail

- ClassDefinition

```java
public ClassDefinition​(
Class
<?> theClass,
byte[] theClassFile)
```

Creates a new

ClassDefinition

binding using the supplied
class and class file bytes. Does not copy the supplied buffer, just captures a reference to it.

**Parameters:** theClass

- the

Class

that needs redefining
**Parameters:** theClassFile

- the new class file bytes
**Throws:** NullPointerException

- if the supplied class or array is

null

.

---

#### Constructor Detail

ClassDefinition

```java
public ClassDefinition​(
Class
<?> theClass,
byte[] theClassFile)
```

Creates a new

ClassDefinition

binding using the supplied
class and class file bytes. Does not copy the supplied buffer, just captures a reference to it.

**Parameters:** theClass

- the

Class

that needs redefining
**Parameters:** theClassFile

- the new class file bytes
**Throws:** NullPointerException

- if the supplied class or array is

null

.

---

#### ClassDefinition

public ClassDefinition​(

Class

<?> theClass,
byte[] theClassFile)

Creates a new

ClassDefinition

binding using the supplied
class and class file bytes. Does not copy the supplied buffer, just captures a reference to it.

Method Detail

- getDefinitionClass

```java
public
Class
<?> getDefinitionClass()
```

Returns the class.

**Returns:** the

Class

object referred to.

- getDefinitionClassFile

```java
public byte[] getDefinitionClassFile()
```

Returns the array of bytes that contains the new class file.

**Returns:** the class file bytes.

---

#### Method Detail

getDefinitionClass

```java
public
Class
<?> getDefinitionClass()
```

Returns the class.

**Returns:** the

Class

object referred to.

---

#### getDefinitionClass

public

Class

<?> getDefinitionClass()

Returns the class.

getDefinitionClassFile

```java
public byte[] getDefinitionClassFile()
```

Returns the array of bytes that contains the new class file.

**Returns:** the class file bytes.

---

#### getDefinitionClassFile

public byte[] getDefinitionClassFile()

Returns the array of bytes that contains the new class file.

---

