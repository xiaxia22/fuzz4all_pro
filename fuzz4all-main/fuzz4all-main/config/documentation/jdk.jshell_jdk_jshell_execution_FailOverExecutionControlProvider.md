# Class FailOverExecutionControlProvider

**Source:** `jdk.jshell\jdk\jshell\execution\FailOverExecutionControlProvider.html`

### Class Description

```java
public class
FailOverExecutionControlProvider

extends
Object

implements
ExecutionControlProvider
```

Tries other providers in sequence until one works.

**All Implemented Interfaces:** ExecutionControlProvider

---

### Field Details

*No entries found.*

### Constructor Details

#### public FailOverExecutionControlProvider()

Create an instance. The instance can be used to start and return an

ExecutionControl

instance by attempting to start a series of

ExecutionControl

specs, until one is successful.

**See Also:**
- generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

---

### Method Details

#### public
String
name()

The unique name of this

ExecutionControlProvider

.

**Specified by:**
- name

in interface

ExecutionControlProvider

**Returns:**
- "failover"

---

#### public
Map
<
String
,​
String
> defaultParameters()

Create and return the default parameter map for this

ExecutionControlProvider

. There are ten parameters, "0" through
"9", their values are

ExecutionControlProvider

specification
strings, or empty string.

**Specified by:**
- defaultParameters

in interface

ExecutionControlProvider

**Returns:**
- a default parameter map

---

#### public
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

Create and return a locally executing

ExecutionControl

instance.
At least one parameter should have a spec.

**Specified by:**
- generate

in interface

ExecutionControlProvider

**Parameters:**
- env

- the execution environment, provided by JShell
- parameters

- the modified parameter map.

**Returns:**
- the execution engine

**Throws:**
- Throwable

- if all the given providers fail, the exception that
occurred on the first attempt to create the execution engine.

---

### Additional Sections

#### Class FailOverExecutionControlProvider

java.lang.Object

- jdk.jshell.execution.FailOverExecutionControlProvider

jdk.jshell.execution.FailOverExecutionControlProvider

**All Implemented Interfaces:** ExecutionControlProvider

```java
public class
FailOverExecutionControlProvider

extends
Object

implements
ExecutionControlProvider
```

Tries other providers in sequence until one works.

**Since:** 9

public class

FailOverExecutionControlProvider

extends

Object

implements

ExecutionControlProvider

Tries other providers in sequence until one works.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FailOverExecutionControlProvider

()

Create an instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

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

Create and return a locally executing

ExecutionControl

instance.

String

name

()

The unique name of this

ExecutionControlProvider

.

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

FailOverExecutionControlProvider

()

Create an instance.

---

#### Constructor Summary

Create an instance.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

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

Create and return a locally executing

ExecutionControl

instance.

String

name

()

The unique name of this

ExecutionControlProvider

.

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

Create and return the default parameter map for this

ExecutionControlProvider

.

Create and return a locally executing

ExecutionControl

instance.

The unique name of this

ExecutionControlProvider

.

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

- FailOverExecutionControlProvider

```java
public FailOverExecutionControlProvider()
```

Create an instance. The instance can be used to start and return an

ExecutionControl

instance by attempting to start a series of

ExecutionControl

specs, until one is successful.

**See Also:** generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

============ METHOD DETAIL ==========

- Method Detail

- name

```java
public
String
name()
```

The unique name of this

ExecutionControlProvider

.

**Specified by:** name

in interface

ExecutionControlProvider
**Returns:** "failover"

- defaultParameters

```java
public
Map
<
String
,​
String
> defaultParameters()
```

Create and return the default parameter map for this

ExecutionControlProvider

. There are ten parameters, "0" through
"9", their values are

ExecutionControlProvider

specification
strings, or empty string.

**Specified by:** defaultParameters

in interface

ExecutionControlProvider
**Returns:** a default parameter map

- generate

```java
public
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

Create and return a locally executing

ExecutionControl

instance.
At least one parameter should have a spec.

**Specified by:** generate

in interface

ExecutionControlProvider
**Parameters:** env

- the execution environment, provided by JShell
**Parameters:** parameters

- the modified parameter map.
**Returns:** the execution engine
**Throws:** Throwable

- if all the given providers fail, the exception that
occurred on the first attempt to create the execution engine.

Constructor Detail

- FailOverExecutionControlProvider

```java
public FailOverExecutionControlProvider()
```

Create an instance. The instance can be used to start and return an

ExecutionControl

instance by attempting to start a series of

ExecutionControl

specs, until one is successful.

**See Also:** generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

---

#### Constructor Detail

FailOverExecutionControlProvider

```java
public FailOverExecutionControlProvider()
```

Create an instance. The instance can be used to start and return an

ExecutionControl

instance by attempting to start a series of

ExecutionControl

specs, until one is successful.

**See Also:** generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

---

#### FailOverExecutionControlProvider

public FailOverExecutionControlProvider()

Create an instance. The instance can be used to start and return an

ExecutionControl

instance by attempting to start a series of

ExecutionControl

specs, until one is successful.

Method Detail

- name

```java
public
String
name()
```

The unique name of this

ExecutionControlProvider

.

**Specified by:** name

in interface

ExecutionControlProvider
**Returns:** "failover"

- defaultParameters

```java
public
Map
<
String
,​
String
> defaultParameters()
```

Create and return the default parameter map for this

ExecutionControlProvider

. There are ten parameters, "0" through
"9", their values are

ExecutionControlProvider

specification
strings, or empty string.

**Specified by:** defaultParameters

in interface

ExecutionControlProvider
**Returns:** a default parameter map

- generate

```java
public
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

Create and return a locally executing

ExecutionControl

instance.
At least one parameter should have a spec.

**Specified by:** generate

in interface

ExecutionControlProvider
**Parameters:** env

- the execution environment, provided by JShell
**Parameters:** parameters

- the modified parameter map.
**Returns:** the execution engine
**Throws:** Throwable

- if all the given providers fail, the exception that
occurred on the first attempt to create the execution engine.

---

#### Method Detail

name

```java
public
String
name()
```

The unique name of this

ExecutionControlProvider

.

**Specified by:** name

in interface

ExecutionControlProvider
**Returns:** "failover"

---

#### name

public

String

name()

The unique name of this

ExecutionControlProvider

.

defaultParameters

```java
public
Map
<
String
,​
String
> defaultParameters()
```

Create and return the default parameter map for this

ExecutionControlProvider

. There are ten parameters, "0" through
"9", their values are

ExecutionControlProvider

specification
strings, or empty string.

**Specified by:** defaultParameters

in interface

ExecutionControlProvider
**Returns:** a default parameter map

---

#### defaultParameters

public

Map

<

String

,​

String

> defaultParameters()

Create and return the default parameter map for this

ExecutionControlProvider

. There are ten parameters, "0" through
"9", their values are

ExecutionControlProvider

specification
strings, or empty string.

generate

```java
public
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

Create and return a locally executing

ExecutionControl

instance.
At least one parameter should have a spec.

**Specified by:** generate

in interface

ExecutionControlProvider
**Parameters:** env

- the execution environment, provided by JShell
**Parameters:** parameters

- the modified parameter map.
**Returns:** the execution engine
**Throws:** Throwable

- if all the given providers fail, the exception that
occurred on the first attempt to create the execution engine.

---

#### generate

public

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

Create and return a locally executing

ExecutionControl

instance.
At least one parameter should have a spec.

---

