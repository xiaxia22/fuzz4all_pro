# Interface ExecutionControlProvider

**Source:** `jdk.jshell\jdk\jshell\spi\ExecutionControlProvider.html`

### Class Description

```java
public interface
ExecutionControlProvider
```

The provider used by JShell to generate the execution engine needed to
evaluate Snippets. Alternate execution engines can be created by
implementing this interface, then configuring JShell with the provider or
the providers name and parameter specifier.

**All Known Implementing Classes:** FailOverExecutionControlProvider

,

JdiExecutionControlProvider

,

LocalExecutionControlProvider

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

The unique name of this

ExecutionControlProvider

. The name must
be a sequence of characters from the Basic Multilingual Plane which are

Character.isJavaIdentifierPart(char)

.

**Returns:**
- the ExecutionControlProvider's name

---

#### default
Map
<
String
,​
String
> defaultParameters()

Create and return the default parameter map for this

ExecutionControlProvider

. The map can optionally be modified;
Modified or unmodified it can be passed to

generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

.

**Returns:**
- the default parameter map

---

#### ExecutionControl
generate​(
ExecutionEnv
env,

Map
<
String
,​
String
> parameters)
throws
Throwable

Create and return the

ExecutionControl

instance.

**Parameters:**
- env

- the execution environment, provided by JShell
- parameters

- the

default

or
modified parameter map.

**Returns:**
- the execution engine

**Throws:**
- Throwable

- an exception that occurred attempting to create the
execution engine.

---

### Additional Sections

#### Interface ExecutionControlProvider

**All Known Implementing Classes:** FailOverExecutionControlProvider

,

JdiExecutionControlProvider

,

LocalExecutionControlProvider

```java
public interface
ExecutionControlProvider
```

The provider used by JShell to generate the execution engine needed to
evaluate Snippets. Alternate execution engines can be created by
implementing this interface, then configuring JShell with the provider or
the providers name and parameter specifier.

**Since:** 9

public interface

ExecutionControlProvider

The provider used by JShell to generate the execution engine needed to
evaluate Snippets. Alternate execution engines can be created by
implementing this interface, then configuring JShell with the provider or
the providers name and parameter specifier.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

Map

<

String

,​

String

>

defaultParameters

()

Create and return the default parameter map for this

ExecutionControlProvider

.

ExecutionControl

generate

​(

ExecutionEnv

env,

Map

<

String

,​

String

> parameters)

Create and return the

ExecutionControl

instance.

String

name

()

The unique name of this

ExecutionControlProvider

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

Map

<

String

,​

String

>

defaultParameters

()

Create and return the default parameter map for this

ExecutionControlProvider

.

ExecutionControl

generate

​(

ExecutionEnv

env,

Map

<

String

,​

String

> parameters)

Create and return the

ExecutionControl

instance.

String

name

()

The unique name of this

ExecutionControlProvider

.

---

#### Method Summary

Create and return the default parameter map for this

ExecutionControlProvider

.

Create and return the

ExecutionControl

instance.

The unique name of this

ExecutionControlProvider

.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

The unique name of this

ExecutionControlProvider

. The name must
be a sequence of characters from the Basic Multilingual Plane which are

Character.isJavaIdentifierPart(char)

.

**Returns:** the ExecutionControlProvider's name

- defaultParameters

```java
default
Map
<
String
,​
String
> defaultParameters()
```

Create and return the default parameter map for this

ExecutionControlProvider

. The map can optionally be modified;
Modified or unmodified it can be passed to

generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

.

**Returns:** the default parameter map

- generate

```java
ExecutionControl
generate​(
ExecutionEnv
env,

Map
<
String
,​
String
> parameters)
throws
Throwable
```

Create and return the

ExecutionControl

instance.

**Parameters:** env

- the execution environment, provided by JShell
**Parameters:** parameters

- the

default

or
modified parameter map.
**Returns:** the execution engine
**Throws:** Throwable

- an exception that occurred attempting to create the
execution engine.

Method Detail

- name

```java
String
name()
```

The unique name of this

ExecutionControlProvider

. The name must
be a sequence of characters from the Basic Multilingual Plane which are

Character.isJavaIdentifierPart(char)

.

**Returns:** the ExecutionControlProvider's name

- defaultParameters

```java
default
Map
<
String
,​
String
> defaultParameters()
```

Create and return the default parameter map for this

ExecutionControlProvider

. The map can optionally be modified;
Modified or unmodified it can be passed to

generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

.

**Returns:** the default parameter map

- generate

```java
ExecutionControl
generate​(
ExecutionEnv
env,

Map
<
String
,​
String
> parameters)
throws
Throwable
```

Create and return the

ExecutionControl

instance.

**Parameters:** env

- the execution environment, provided by JShell
**Parameters:** parameters

- the

default

or
modified parameter map.
**Returns:** the execution engine
**Throws:** Throwable

- an exception that occurred attempting to create the
execution engine.

---

#### Method Detail

name

```java
String
name()
```

The unique name of this

ExecutionControlProvider

. The name must
be a sequence of characters from the Basic Multilingual Plane which are

Character.isJavaIdentifierPart(char)

.

**Returns:** the ExecutionControlProvider's name

---

#### name

String

name()

The unique name of this

ExecutionControlProvider

. The name must
be a sequence of characters from the Basic Multilingual Plane which are

Character.isJavaIdentifierPart(char)

.

defaultParameters

```java
default
Map
<
String
,​
String
> defaultParameters()
```

Create and return the default parameter map for this

ExecutionControlProvider

. The map can optionally be modified;
Modified or unmodified it can be passed to

generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

.

**Returns:** the default parameter map

---

#### defaultParameters

default

Map

<

String

,​

String

> defaultParameters()

Create and return the default parameter map for this

ExecutionControlProvider

. The map can optionally be modified;
Modified or unmodified it can be passed to

generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

.

generate

```java
ExecutionControl
generate​(
ExecutionEnv
env,

Map
<
String
,​
String
> parameters)
throws
Throwable
```

Create and return the

ExecutionControl

instance.

**Parameters:** env

- the execution environment, provided by JShell
**Parameters:** parameters

- the

default

or
modified parameter map.
**Returns:** the execution engine
**Throws:** Throwable

- an exception that occurred attempting to create the
execution engine.

---

#### generate

ExecutionControl

generate​(

ExecutionEnv

env,

Map

<

String

,​

String

> parameters)
throws

Throwable

Create and return the

ExecutionControl

instance.

---

