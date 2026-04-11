# Class SchemaFactoryLoader

**Source:** `java.xml\javax\xml\validation\SchemaFactoryLoader.html`

### Class Description

```java
public abstract class
SchemaFactoryLoader

extends
Object
```

Factory that creates

SchemaFactory

.

DO NOT USE THIS CLASS

This class was introduced as a part of an early proposal during the
JSR-206 standardization process. The proposal was eventually abandoned
but this class accidentally remained in the source tree, and made its
way into the final version.

This class does not participate in any JAXP 1.3 or JAXP 1.4 processing.
It must not be used by users or JAXP implementations.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SchemaFactoryLoader()

A do-nothing constructor.

---

### Method Details

#### public abstract
SchemaFactory
newFactory​(
String
schemaLanguage)

Creates a new

SchemaFactory

object for the specified
schema language.

**Parameters:**
- schemaLanguage

- See

the list of available schema languages

.

**Returns:**
- null

if the callee fails to create one.

**Throws:**
- NullPointerException

- If the

schemaLanguage

parameter is null.

---

### Additional Sections

#### Class SchemaFactoryLoader

java.lang.Object

- javax.xml.validation.SchemaFactoryLoader

javax.xml.validation.SchemaFactoryLoader

```java
public abstract class
SchemaFactoryLoader

extends
Object
```

Factory that creates

SchemaFactory

.

DO NOT USE THIS CLASS

This class was introduced as a part of an early proposal during the
JSR-206 standardization process. The proposal was eventually abandoned
but this class accidentally remained in the source tree, and made its
way into the final version.

This class does not participate in any JAXP 1.3 or JAXP 1.4 processing.
It must not be used by users or JAXP implementations.

**Since:** 1.5

public abstract class

SchemaFactoryLoader

extends

Object

Factory that creates

SchemaFactory

.

DO NOT USE THIS CLASS

This class was introduced as a part of an early proposal during the
JSR-206 standardization process. The proposal was eventually abandoned
but this class accidentally remained in the source tree, and made its
way into the final version.

This class does not participate in any JAXP 1.3 or JAXP 1.4 processing.
It must not be used by users or JAXP implementations.

Factory that creates

SchemaFactory

.

DO NOT USE THIS CLASS

This class was introduced as a part of an early proposal during the
JSR-206 standardization process. The proposal was eventually abandoned
but this class accidentally remained in the source tree, and made its
way into the final version.

This class does not participate in any JAXP 1.3 or JAXP 1.4 processing.
It must not be used by users or JAXP implementations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SchemaFactoryLoader

()

A do-nothing constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

SchemaFactory

newFactory

​(

String

schemaLanguage)

Creates a new

SchemaFactory

object for the specified
schema language.

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

Modifier

Constructor

Description

protected

SchemaFactoryLoader

()

A do-nothing constructor.

---

#### Constructor Summary

A do-nothing constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

SchemaFactory

newFactory

​(

String

schemaLanguage)

Creates a new

SchemaFactory

object for the specified
schema language.

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

Creates a new

SchemaFactory

object for the specified
schema language.

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

- SchemaFactoryLoader

```java
protected SchemaFactoryLoader()
```

A do-nothing constructor.

============ METHOD DETAIL ==========

- Method Detail

- newFactory

```java
public abstract
SchemaFactory
newFactory​(
String
schemaLanguage)
```

Creates a new

SchemaFactory

object for the specified
schema language.

**Parameters:** schemaLanguage

- See

the list of available schema languages

.
**Returns:** null

if the callee fails to create one.
**Throws:** NullPointerException

- If the

schemaLanguage

parameter is null.

Constructor Detail

- SchemaFactoryLoader

```java
protected SchemaFactoryLoader()
```

A do-nothing constructor.

---

#### Constructor Detail

SchemaFactoryLoader

```java
protected SchemaFactoryLoader()
```

A do-nothing constructor.

---

#### SchemaFactoryLoader

protected SchemaFactoryLoader()

A do-nothing constructor.

Method Detail

- newFactory

```java
public abstract
SchemaFactory
newFactory​(
String
schemaLanguage)
```

Creates a new

SchemaFactory

object for the specified
schema language.

**Parameters:** schemaLanguage

- See

the list of available schema languages

.
**Returns:** null

if the callee fails to create one.
**Throws:** NullPointerException

- If the

schemaLanguage

parameter is null.

---

#### Method Detail

newFactory

```java
public abstract
SchemaFactory
newFactory​(
String
schemaLanguage)
```

Creates a new

SchemaFactory

object for the specified
schema language.

**Parameters:** schemaLanguage

- See

the list of available schema languages

.
**Returns:** null

if the callee fails to create one.
**Throws:** NullPointerException

- If the

schemaLanguage

parameter is null.

---

#### newFactory

public abstract

SchemaFactory

newFactory​(

String

schemaLanguage)

Creates a new

SchemaFactory

object for the specified
schema language.

---

