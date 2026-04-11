# Class AgentInitializationException

**Source:** `jdk.attach\com\sun\tools\attach\AgentInitializationException.html`

### Class Description

```java
public class
AgentInitializationException

extends
Exception
```

The exception thrown when an agent fails to initialize in the target
Java virtual machine.

This exception is thrown by

VirtualMachine.loadAgent

,

VirtualMachine.loadAgentLibrary

,

VirtualMachine.loadAgentPath

methods if an agent, or agent library, cannot be initialized.
When thrown by

VirtualMachine.loadAgentLibrary

, or

VirtualMachine.loadAgentPath

then the exception encapsulates
the error returned by the agent's

Agent_OnAttach

function.
This error code can be obtained by invoking the

returnValue

method.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AgentInitializationException()

Constructs an

AgentInitializationException

with
no detail message.

---

#### public AgentInitializationException​(
String
s)

Constructs an

AgentInitializationException

with
the specified detail message.

**Parameters:**
- s

- the detail message.

---

#### public AgentInitializationException​(
String
s,
int returnValue)

Constructs an

AgentInitializationException

with
the specified detail message and the return value from the
execution of the agent's

Agent_OnAttach

function.

**Parameters:**
- s

- the detail message.
- returnValue

- the return value

---

### Method Details

#### public int returnValue()

If the exception was created with the return value from the agent

Agent_OnAttach

function then this returns that value,
otherwise returns

0

.

**Returns:**
- the return value

---

### Additional Sections

#### Class AgentInitializationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - com.sun.tools.attach.AgentInitializationException

java.lang.Throwable

- java.lang.Exception
- - com.sun.tools.attach.AgentInitializationException

java.lang.Exception

- com.sun.tools.attach.AgentInitializationException

com.sun.tools.attach.AgentInitializationException

**All Implemented Interfaces:** Serializable

```java
public class
AgentInitializationException

extends
Exception
```

The exception thrown when an agent fails to initialize in the target
Java virtual machine.

This exception is thrown by

VirtualMachine.loadAgent

,

VirtualMachine.loadAgentLibrary

,

VirtualMachine.loadAgentPath

methods if an agent, or agent library, cannot be initialized.
When thrown by

VirtualMachine.loadAgentLibrary

, or

VirtualMachine.loadAgentPath

then the exception encapsulates
the error returned by the agent's

Agent_OnAttach

function.
This error code can be obtained by invoking the

returnValue

method.

**See Also:** Serialized Form

public class

AgentInitializationException

extends

Exception

The exception thrown when an agent fails to initialize in the target
Java virtual machine.

This exception is thrown by

VirtualMachine.loadAgent

,

VirtualMachine.loadAgentLibrary

,

VirtualMachine.loadAgentPath

methods if an agent, or agent library, cannot be initialized.
When thrown by

VirtualMachine.loadAgentLibrary

, or

VirtualMachine.loadAgentPath

then the exception encapsulates
the error returned by the agent's

Agent_OnAttach

function.
This error code can be obtained by invoking the

returnValue

method.

This exception is thrown by

VirtualMachine.loadAgent

,

VirtualMachine.loadAgentLibrary

,

VirtualMachine.loadAgentPath

methods if an agent, or agent library, cannot be initialized.
When thrown by

VirtualMachine.loadAgentLibrary

, or

VirtualMachine.loadAgentPath

then the exception encapsulates
the error returned by the agent's

Agent_OnAttach

function.
This error code can be obtained by invoking the

returnValue

method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AgentInitializationException

()

Constructs an

AgentInitializationException

with
no detail message.

AgentInitializationException

​(

String

s)

Constructs an

AgentInitializationException

with
the specified detail message.

AgentInitializationException

​(

String

s,
int returnValue)

Constructs an

AgentInitializationException

with
the specified detail message and the return value from the
execution of the agent's

Agent_OnAttach

function.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

returnValue

()

If the exception was created with the return value from the agent

Agent_OnAttach

function then this returns that value,
otherwise returns

0

.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

AgentInitializationException

()

Constructs an

AgentInitializationException

with
no detail message.

AgentInitializationException

​(

String

s)

Constructs an

AgentInitializationException

with
the specified detail message.

AgentInitializationException

​(

String

s,
int returnValue)

Constructs an

AgentInitializationException

with
the specified detail message and the return value from the
execution of the agent's

Agent_OnAttach

function.

---

#### Constructor Summary

Constructs an

AgentInitializationException

with
no detail message.

Constructs an

AgentInitializationException

with
the specified detail message.

Constructs an

AgentInitializationException

with
the specified detail message and the return value from the
execution of the agent's

Agent_OnAttach

function.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

returnValue

()

If the exception was created with the return value from the agent

Agent_OnAttach

function then this returns that value,
otherwise returns

0

.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

If the exception was created with the return value from the agent

Agent_OnAttach

function then this returns that value,
otherwise returns

0

.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AgentInitializationException

```java
public AgentInitializationException()
```

Constructs an

AgentInitializationException

with
no detail message.

- AgentInitializationException

```java
public AgentInitializationException​(
String
s)
```

Constructs an

AgentInitializationException

with
the specified detail message.

**Parameters:** s

- the detail message.

- AgentInitializationException

```java
public AgentInitializationException​(
String
s,
int returnValue)
```

Constructs an

AgentInitializationException

with
the specified detail message and the return value from the
execution of the agent's

Agent_OnAttach

function.

**Parameters:** s

- the detail message.
**Parameters:** returnValue

- the return value

============ METHOD DETAIL ==========

- Method Detail

- returnValue

```java
public int returnValue()
```

If the exception was created with the return value from the agent

Agent_OnAttach

function then this returns that value,
otherwise returns

0

.

**Returns:** the return value

Constructor Detail

- AgentInitializationException

```java
public AgentInitializationException()
```

Constructs an

AgentInitializationException

with
no detail message.

- AgentInitializationException

```java
public AgentInitializationException​(
String
s)
```

Constructs an

AgentInitializationException

with
the specified detail message.

**Parameters:** s

- the detail message.

- AgentInitializationException

```java
public AgentInitializationException​(
String
s,
int returnValue)
```

Constructs an

AgentInitializationException

with
the specified detail message and the return value from the
execution of the agent's

Agent_OnAttach

function.

**Parameters:** s

- the detail message.
**Parameters:** returnValue

- the return value

---

#### Constructor Detail

AgentInitializationException

```java
public AgentInitializationException()
```

Constructs an

AgentInitializationException

with
no detail message.

---

#### AgentInitializationException

public AgentInitializationException()

Constructs an

AgentInitializationException

with
no detail message.

AgentInitializationException

```java
public AgentInitializationException​(
String
s)
```

Constructs an

AgentInitializationException

with
the specified detail message.

**Parameters:** s

- the detail message.

---

#### AgentInitializationException

public AgentInitializationException​(

String

s)

Constructs an

AgentInitializationException

with
the specified detail message.

AgentInitializationException

```java
public AgentInitializationException​(
String
s,
int returnValue)
```

Constructs an

AgentInitializationException

with
the specified detail message and the return value from the
execution of the agent's

Agent_OnAttach

function.

**Parameters:** s

- the detail message.
**Parameters:** returnValue

- the return value

---

#### AgentInitializationException

public AgentInitializationException​(

String

s,
int returnValue)

Constructs an

AgentInitializationException

with
the specified detail message and the return value from the
execution of the agent's

Agent_OnAttach

function.

Method Detail

- returnValue

```java
public int returnValue()
```

If the exception was created with the return value from the agent

Agent_OnAttach

function then this returns that value,
otherwise returns

0

.

**Returns:** the return value

---

#### Method Detail

returnValue

```java
public int returnValue()
```

If the exception was created with the return value from the agent

Agent_OnAttach

function then this returns that value,
otherwise returns

0

.

**Returns:** the return value

---

#### returnValue

public int returnValue()

If the exception was created with the return value from the agent

Agent_OnAttach

function then this returns that value,
otherwise returns

0

.

---

