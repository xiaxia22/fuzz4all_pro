# Class JdiInitiator

**Source:** `jdk.jshell\jdk\jshell\execution\JdiInitiator.html`

### Class Description

```java
public class
JdiInitiator

extends
Object
```

Sets up a JDI connection, providing the resulting JDI

VirtualMachine

and the

Process

the remote agent is running in.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

#### public JdiInitiator​(int port,

List
<
String
> remoteVMOptions,

String
remoteAgent,
boolean isLaunch,

String
host,
int timeout,

Map
<
String
,​
String
> customConnectorArgs)

Start the remote agent and establish a JDI connection to it.

**Parameters:**
- port

- the socket port for (non-JDI) commands
- remoteVMOptions

- any user requested VM command-line options
- remoteAgent

- full class name of remote agent to launch
- isLaunch

- does JDI do the launch? That is, LaunchingConnector,
otherwise we start explicitly and use ListeningConnector
- host

- explicit hostname to use, if null use discovered
hostname, applies to listening only (!isLaunch)
- timeout

- the start-up time-out in milliseconds. If zero or negative,
will not wait thus will timeout immediately if not already started.
- customConnectorArgs

- custom arguments passed to the connector.
These are JDI com.sun.jdi.connect.Connector arguments. The

vmexec

argument is not supported.

---

### Method Details

#### public
VirtualMachine
vm()

Returns the resulting

VirtualMachine

instance.

**Returns:**
- the virtual machine

---

#### public
Process
process()

Returns the launched process.

**Returns:**
- the remote agent process

---

### Additional Sections

#### Class JdiInitiator

java.lang.Object

- jdk.jshell.execution.JdiInitiator

jdk.jshell.execution.JdiInitiator

```java
public class
JdiInitiator

extends
Object
```

Sets up a JDI connection, providing the resulting JDI

VirtualMachine

and the

Process

the remote agent is running in.

**Since:** 9

public class

JdiInitiator

extends

Object

Sets up a JDI connection, providing the resulting JDI

VirtualMachine

and the

Process

the remote agent is running in.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JdiInitiator

​(int port,

List

<

String

> remoteVMOptions,

String

remoteAgent,
boolean isLaunch,

String

host,
int timeout,

Map

<

String

,​

String

> customConnectorArgs)

Start the remote agent and establish a JDI connection to it.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Process

process

()

Returns the launched process.

VirtualMachine

vm

()

Returns the resulting

VirtualMachine

instance.

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

JdiInitiator

​(int port,

List

<

String

> remoteVMOptions,

String

remoteAgent,
boolean isLaunch,

String

host,
int timeout,

Map

<

String

,​

String

> customConnectorArgs)

Start the remote agent and establish a JDI connection to it.

---

#### Constructor Summary

Start the remote agent and establish a JDI connection to it.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Process

process

()

Returns the launched process.

VirtualMachine

vm

()

Returns the resulting

VirtualMachine

instance.

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

Returns the launched process.

Returns the resulting

VirtualMachine

instance.

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

- JdiInitiator

```java
public JdiInitiator​(int port,

List
<
String
> remoteVMOptions,

String
remoteAgent,
boolean isLaunch,

String
host,
int timeout,

Map
<
String
,​
String
> customConnectorArgs)
```

Start the remote agent and establish a JDI connection to it.

**Parameters:** port

- the socket port for (non-JDI) commands
**Parameters:** remoteVMOptions

- any user requested VM command-line options
**Parameters:** remoteAgent

- full class name of remote agent to launch
**Parameters:** isLaunch

- does JDI do the launch? That is, LaunchingConnector,
otherwise we start explicitly and use ListeningConnector
**Parameters:** host

- explicit hostname to use, if null use discovered
hostname, applies to listening only (!isLaunch)
**Parameters:** timeout

- the start-up time-out in milliseconds. If zero or negative,
will not wait thus will timeout immediately if not already started.
**Parameters:** customConnectorArgs

- custom arguments passed to the connector.
These are JDI com.sun.jdi.connect.Connector arguments. The

vmexec

argument is not supported.

============ METHOD DETAIL ==========

- Method Detail

- vm

```java
public
VirtualMachine
vm()
```

Returns the resulting

VirtualMachine

instance.

**Returns:** the virtual machine

- process

```java
public
Process
process()
```

Returns the launched process.

**Returns:** the remote agent process

Constructor Detail

- JdiInitiator

```java
public JdiInitiator​(int port,

List
<
String
> remoteVMOptions,

String
remoteAgent,
boolean isLaunch,

String
host,
int timeout,

Map
<
String
,​
String
> customConnectorArgs)
```

Start the remote agent and establish a JDI connection to it.

**Parameters:** port

- the socket port for (non-JDI) commands
**Parameters:** remoteVMOptions

- any user requested VM command-line options
**Parameters:** remoteAgent

- full class name of remote agent to launch
**Parameters:** isLaunch

- does JDI do the launch? That is, LaunchingConnector,
otherwise we start explicitly and use ListeningConnector
**Parameters:** host

- explicit hostname to use, if null use discovered
hostname, applies to listening only (!isLaunch)
**Parameters:** timeout

- the start-up time-out in milliseconds. If zero or negative,
will not wait thus will timeout immediately if not already started.
**Parameters:** customConnectorArgs

- custom arguments passed to the connector.
These are JDI com.sun.jdi.connect.Connector arguments. The

vmexec

argument is not supported.

---

#### Constructor Detail

JdiInitiator

```java
public JdiInitiator​(int port,

List
<
String
> remoteVMOptions,

String
remoteAgent,
boolean isLaunch,

String
host,
int timeout,

Map
<
String
,​
String
> customConnectorArgs)
```

Start the remote agent and establish a JDI connection to it.

**Parameters:** port

- the socket port for (non-JDI) commands
**Parameters:** remoteVMOptions

- any user requested VM command-line options
**Parameters:** remoteAgent

- full class name of remote agent to launch
**Parameters:** isLaunch

- does JDI do the launch? That is, LaunchingConnector,
otherwise we start explicitly and use ListeningConnector
**Parameters:** host

- explicit hostname to use, if null use discovered
hostname, applies to listening only (!isLaunch)
**Parameters:** timeout

- the start-up time-out in milliseconds. If zero or negative,
will not wait thus will timeout immediately if not already started.
**Parameters:** customConnectorArgs

- custom arguments passed to the connector.
These are JDI com.sun.jdi.connect.Connector arguments. The

vmexec

argument is not supported.

---

#### JdiInitiator

public JdiInitiator​(int port,

List

<

String

> remoteVMOptions,

String

remoteAgent,
boolean isLaunch,

String

host,
int timeout,

Map

<

String

,​

String

> customConnectorArgs)

Start the remote agent and establish a JDI connection to it.

Method Detail

- vm

```java
public
VirtualMachine
vm()
```

Returns the resulting

VirtualMachine

instance.

**Returns:** the virtual machine

- process

```java
public
Process
process()
```

Returns the launched process.

**Returns:** the remote agent process

---

#### Method Detail

vm

```java
public
VirtualMachine
vm()
```

Returns the resulting

VirtualMachine

instance.

**Returns:** the virtual machine

---

#### vm

public

VirtualMachine

vm()

Returns the resulting

VirtualMachine

instance.

process

```java
public
Process
process()
```

Returns the launched process.

**Returns:** the remote agent process

---

#### process

public

Process

process()

Returns the launched process.

---

