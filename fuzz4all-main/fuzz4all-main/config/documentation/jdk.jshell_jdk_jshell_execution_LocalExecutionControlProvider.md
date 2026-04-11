# Class LocalExecutionControlProvider

**Source:** `jdk.jshell\jdk\jshell\execution\LocalExecutionControlProvider.html`

### Class Description

```java
public class
LocalExecutionControlProvider

extends
Object

implements
ExecutionControlProvider
```

A provider of execution engines which run in the same process as JShell.

**All Implemented Interfaces:** ExecutionControlProvider

---

### Field Details

*No entries found.*

### Constructor Details

#### public LocalExecutionControlProvider()

Create an instance. An instance can be used to

generate

an

ExecutionControl

instance
that executes code in the same process.

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
- "local"

---

#### public
Map
<
String
,​
String
> defaultParameters()

Create and return the default parameter map for

LocalExecutionControlProvider

.

LocalExecutionControlProvider

has no parameters.

**Specified by:**
- defaultParameters

in interface

ExecutionControlProvider

**Returns:**
- an empty parameter map

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

Create and return a locally executing

ExecutionControl

instance.

**Specified by:**
- generate

in interface

ExecutionControlProvider

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

---

### Additional Sections

#### Class LocalExecutionControlProvider

java.lang.Object

- jdk.jshell.execution.LocalExecutionControlProvider

jdk.jshell.execution.LocalExecutionControlProvider

**All Implemented Interfaces:** ExecutionControlProvider

```java
public class
LocalExecutionControlProvider

extends
Object

implements
ExecutionControlProvider
```

A provider of execution engines which run in the same process as JShell.

**Since:** 9

public class

LocalExecutionControlProvider

extends

Object

implements

ExecutionControlProvider

A provider of execution engines which run in the same process as JShell.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LocalExecutionControlProvider

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

Create and return the default parameter map for

LocalExecutionControlProvider

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

LocalExecutionControlProvider

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

Create and return the default parameter map for

LocalExecutionControlProvider

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

Create and return the default parameter map for

LocalExecutionControlProvider

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

- LocalExecutionControlProvider

```java
public LocalExecutionControlProvider()
```

Create an instance. An instance can be used to

generate

an

ExecutionControl

instance
that executes code in the same process.

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
**Returns:** "local"

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

Create and return the default parameter map for

LocalExecutionControlProvider

.

LocalExecutionControlProvider

has no parameters.

**Specified by:** defaultParameters

in interface

ExecutionControlProvider
**Returns:** an empty parameter map

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
```

Create and return a locally executing

ExecutionControl

instance.

**Specified by:** generate

in interface

ExecutionControlProvider
**Parameters:** env

- the execution environment, provided by JShell
**Parameters:** parameters

- the

default

or
modified parameter map.
**Returns:** the execution engine

Constructor Detail

- LocalExecutionControlProvider

```java
public LocalExecutionControlProvider()
```

Create an instance. An instance can be used to

generate

an

ExecutionControl

instance
that executes code in the same process.

---

#### Constructor Detail

LocalExecutionControlProvider

```java
public LocalExecutionControlProvider()
```

Create an instance. An instance can be used to

generate

an

ExecutionControl

instance
that executes code in the same process.

---

#### LocalExecutionControlProvider

public LocalExecutionControlProvider()

Create an instance. An instance can be used to

generate

an

ExecutionControl

instance
that executes code in the same process.

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
**Returns:** "local"

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

Create and return the default parameter map for

LocalExecutionControlProvider

.

LocalExecutionControlProvider

has no parameters.

**Specified by:** defaultParameters

in interface

ExecutionControlProvider
**Returns:** an empty parameter map

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
```

Create and return a locally executing

ExecutionControl

instance.

**Specified by:** generate

in interface

ExecutionControlProvider
**Parameters:** env

- the execution environment, provided by JShell
**Parameters:** parameters

- the

default

or
modified parameter map.
**Returns:** the execution engine

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
**Returns:** "local"

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

Create and return the default parameter map for

LocalExecutionControlProvider

.

LocalExecutionControlProvider

has no parameters.

**Specified by:** defaultParameters

in interface

ExecutionControlProvider
**Returns:** an empty parameter map

---

#### defaultParameters

public

Map

<

String

,​

String

> defaultParameters()

Create and return the default parameter map for

LocalExecutionControlProvider

.

LocalExecutionControlProvider

has no parameters.

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
```

Create and return a locally executing

ExecutionControl

instance.

**Specified by:** generate

in interface

ExecutionControlProvider
**Parameters:** env

- the execution environment, provided by JShell
**Parameters:** parameters

- the

default

or
modified parameter map.
**Returns:** the execution engine

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

Create and return a locally executing

ExecutionControl

instance.

---

