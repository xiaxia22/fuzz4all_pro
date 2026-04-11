# Class JdiExecutionControlProvider

**Source:** `jdk.jshell\jdk\jshell\execution\JdiExecutionControlProvider.html`

### Class Description

```java
public class
JdiExecutionControlProvider

extends
Object

implements
ExecutionControlProvider
```

A provider of remote JDI-controlled execution engines.

**All Implemented Interfaces:** ExecutionControlProvider

---

### Field Details

#### public static final
String
PARAM_REMOTE_AGENT

The remote agent to launch.

**See Also:**
- Constant Field Values

---

#### public static final
String
PARAM_TIMEOUT

Milliseconds before connect timeout.

**See Also:**
- Constant Field Values

---

#### public static final
String
PARAM_HOST_NAME

The local hostname to connect to.

**See Also:**
- Constant Field Values

---

#### public static final
String
PARAM_LAUNCH

Should JDI-controlled launching be used?

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public JdiExecutionControlProvider()

Create an instance. An instance can be used to

generate

an

ExecutionControl

instance
that uses the Java Debug Interface as part of the control of a remote
process.

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
- "jdi"

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

. The map can optionally be modified;
Modified or unmodified it can be passed to

ExecutionControlProvider.generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

.

Parameters

Parameter

Description

Constant Field

remoteAgent

the remote agent to launch

PARAM_REMOTE_AGENT

timeout

milliseconds before connect timeout

PARAM_TIMEOUT

launch

"true" for JDI controlled launch

PARAM_LAUNCH

hostname

connect to the named of the local host ("" for discovered)

PARAM_HOST_NAME

**Specified by:**
- defaultParameters

in interface

ExecutionControlProvider

**Returns:**
- the default parameter map

---

### Additional Sections

#### Class JdiExecutionControlProvider

java.lang.Object

- jdk.jshell.execution.JdiExecutionControlProvider

jdk.jshell.execution.JdiExecutionControlProvider

**All Implemented Interfaces:** ExecutionControlProvider

```java
public class
JdiExecutionControlProvider

extends
Object

implements
ExecutionControlProvider
```

A provider of remote JDI-controlled execution engines.

**Since:** 9

public class

JdiExecutionControlProvider

extends

Object

implements

ExecutionControlProvider

A provider of remote JDI-controlled execution engines.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

PARAM_HOST_NAME

The local hostname to connect to.

static

String

PARAM_LAUNCH

Should JDI-controlled launching be used?

static

String

PARAM_REMOTE_AGENT

The remote agent to launch.

static

String

PARAM_TIMEOUT

Milliseconds before connect timeout.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JdiExecutionControlProvider

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

- Methods declared in interface jdk.jshell.spi.

ExecutionControlProvider

generate

Field Summary

Fields

Modifier and Type

Field

Description

static

String

PARAM_HOST_NAME

The local hostname to connect to.

static

String

PARAM_LAUNCH

Should JDI-controlled launching be used?

static

String

PARAM_REMOTE_AGENT

The remote agent to launch.

static

String

PARAM_TIMEOUT

Milliseconds before connect timeout.

---

#### Field Summary

The local hostname to connect to.

Should JDI-controlled launching be used?

The remote agent to launch.

Milliseconds before connect timeout.

Constructor Summary

Constructors

Constructor

Description

JdiExecutionControlProvider

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

- Methods declared in interface jdk.jshell.spi.

ExecutionControlProvider

generate

---

#### Method Summary

Create and return the default parameter map for this

ExecutionControlProvider

.

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

Methods declared in interface jdk.jshell.spi.

ExecutionControlProvider

generate

---

#### Methods declared in interface jdk.jshell.spi. ExecutionControlProvider

============ FIELD DETAIL ===========

- Field Detail

- PARAM_REMOTE_AGENT

```java
public static final
String
PARAM_REMOTE_AGENT
```

The remote agent to launch.

**See Also:** Constant Field Values

- PARAM_TIMEOUT

```java
public static final
String
PARAM_TIMEOUT
```

Milliseconds before connect timeout.

**See Also:** Constant Field Values

- PARAM_HOST_NAME

```java
public static final
String
PARAM_HOST_NAME
```

The local hostname to connect to.

**See Also:** Constant Field Values

- PARAM_LAUNCH

```java
public static final
String
PARAM_LAUNCH
```

Should JDI-controlled launching be used?

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JdiExecutionControlProvider

```java
public JdiExecutionControlProvider()
```

Create an instance. An instance can be used to

generate

an

ExecutionControl

instance
that uses the Java Debug Interface as part of the control of a remote
process.

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
**Returns:** "jdi"

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

. The map can optionally be modified;
Modified or unmodified it can be passed to

ExecutionControlProvider.generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

.

Parameters

Parameter

Description

Constant Field

remoteAgent

the remote agent to launch

PARAM_REMOTE_AGENT

timeout

milliseconds before connect timeout

PARAM_TIMEOUT

launch

"true" for JDI controlled launch

PARAM_LAUNCH

hostname

connect to the named of the local host ("" for discovered)

PARAM_HOST_NAME

**Specified by:** defaultParameters

in interface

ExecutionControlProvider
**Returns:** the default parameter map

Field Detail

- PARAM_REMOTE_AGENT

```java
public static final
String
PARAM_REMOTE_AGENT
```

The remote agent to launch.

**See Also:** Constant Field Values

- PARAM_TIMEOUT

```java
public static final
String
PARAM_TIMEOUT
```

Milliseconds before connect timeout.

**See Also:** Constant Field Values

- PARAM_HOST_NAME

```java
public static final
String
PARAM_HOST_NAME
```

The local hostname to connect to.

**See Also:** Constant Field Values

- PARAM_LAUNCH

```java
public static final
String
PARAM_LAUNCH
```

Should JDI-controlled launching be used?

**See Also:** Constant Field Values

---

#### Field Detail

PARAM_REMOTE_AGENT

```java
public static final
String
PARAM_REMOTE_AGENT
```

The remote agent to launch.

**See Also:** Constant Field Values

---

#### PARAM_REMOTE_AGENT

public static final

String

PARAM_REMOTE_AGENT

The remote agent to launch.

PARAM_TIMEOUT

```java
public static final
String
PARAM_TIMEOUT
```

Milliseconds before connect timeout.

**See Also:** Constant Field Values

---

#### PARAM_TIMEOUT

public static final

String

PARAM_TIMEOUT

Milliseconds before connect timeout.

PARAM_HOST_NAME

```java
public static final
String
PARAM_HOST_NAME
```

The local hostname to connect to.

**See Also:** Constant Field Values

---

#### PARAM_HOST_NAME

public static final

String

PARAM_HOST_NAME

The local hostname to connect to.

PARAM_LAUNCH

```java
public static final
String
PARAM_LAUNCH
```

Should JDI-controlled launching be used?

**See Also:** Constant Field Values

---

#### PARAM_LAUNCH

public static final

String

PARAM_LAUNCH

Should JDI-controlled launching be used?

Constructor Detail

- JdiExecutionControlProvider

```java
public JdiExecutionControlProvider()
```

Create an instance. An instance can be used to

generate

an

ExecutionControl

instance
that uses the Java Debug Interface as part of the control of a remote
process.

---

#### Constructor Detail

JdiExecutionControlProvider

```java
public JdiExecutionControlProvider()
```

Create an instance. An instance can be used to

generate

an

ExecutionControl

instance
that uses the Java Debug Interface as part of the control of a remote
process.

---

#### JdiExecutionControlProvider

public JdiExecutionControlProvider()

Create an instance. An instance can be used to

generate

an

ExecutionControl

instance
that uses the Java Debug Interface as part of the control of a remote
process.

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
**Returns:** "jdi"

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

. The map can optionally be modified;
Modified or unmodified it can be passed to

ExecutionControlProvider.generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

.

Parameters

Parameter

Description

Constant Field

remoteAgent

the remote agent to launch

PARAM_REMOTE_AGENT

timeout

milliseconds before connect timeout

PARAM_TIMEOUT

launch

"true" for JDI controlled launch

PARAM_LAUNCH

hostname

connect to the named of the local host ("" for discovered)

PARAM_HOST_NAME

**Specified by:** defaultParameters

in interface

ExecutionControlProvider
**Returns:** the default parameter map

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
**Returns:** "jdi"

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

. The map can optionally be modified;
Modified or unmodified it can be passed to

ExecutionControlProvider.generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

.

Parameters

Parameter

Description

Constant Field

remoteAgent

the remote agent to launch

PARAM_REMOTE_AGENT

timeout

milliseconds before connect timeout

PARAM_TIMEOUT

launch

"true" for JDI controlled launch

PARAM_LAUNCH

hostname

connect to the named of the local host ("" for discovered)

PARAM_HOST_NAME

**Specified by:** defaultParameters

in interface

ExecutionControlProvider
**Returns:** the default parameter map

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

. The map can optionally be modified;
Modified or unmodified it can be passed to

ExecutionControlProvider.generate(jdk.jshell.spi.ExecutionEnv, java.util.Map)

.

Parameters

Parameter

Description

Constant Field

remoteAgent

the remote agent to launch

PARAM_REMOTE_AGENT

timeout

milliseconds before connect timeout

PARAM_TIMEOUT

launch

"true" for JDI controlled launch

PARAM_LAUNCH

hostname

connect to the named of the local host ("" for discovered)

PARAM_HOST_NAME

---

