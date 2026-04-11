# Class VirtualMachine

**Source:** `jdk.attach\com\sun\tools\attach\VirtualMachine.html`

### Class Description

```java
public abstract class
VirtualMachine

extends
Object
```

A Java virtual machine.

A

VirtualMachine

represents a Java virtual machine to which this
Java virtual machine has attached. The Java virtual machine to which it is
attached is sometimes called the

target virtual machine

, or

target VM

.
An application (typically a tool such as a managemet console or profiler) uses a
VirtualMachine to load an agent into the target VM. For example, a profiler tool
written in the Java Language might attach to a running application and load its
profiler agent to profile the running application.

A VirtualMachine is obtained by invoking the

attach

method
with an identifier that identifies the target virtual machine. The identifier is
implementation-dependent but is typically the process identifier (or pid) in
environments where each Java virtual machine runs in its own operating system process.
Alternatively, a

VirtualMachine

instance is obtained by invoking the

attach

method with a

VirtualMachineDescriptor

obtained
from the list of virtual machine descriptors returned by the

list

method.
Once a reference to a virtual machine is obtained, the

loadAgent

,

loadAgentLibrary

, and

loadAgentPath

methods are used to load agents into target virtual machine. The

loadAgent

method is used to load agents that are written in the Java
Language and deployed in a

JAR file

. (See

java.lang.instrument

for a detailed description on how these agents
are loaded and started). The

loadAgentLibrary

and

loadAgentPath

methods are used to load agents that
are deployed either in a dynamic library or statically linked into the VM and
make use of the

JVM Tools Interface

.

In addition to loading agents a VirtualMachine provides read access to the

system properties

in the target VM.
This can be useful in some environments where properties such as

java.home

,

os.name

, or

os.arch

are
used to construct the path to agent that will be loaded into the target VM.

The following example demonstrates how VirtualMachine may be used:

```java
// attach to target VM
VirtualMachine vm = VirtualMachine.attach("2177");

// start management agent
Properties props = new Properties();
props.put("com.sun.management.jmxremote.port", "5000");
vm.startManagementAgent(props);

// detach
vm.detach();
```

In this example we attach to a Java virtual machine that is identified by
the process identifier

2177

. Then the JMX management agent is
started in the target process using the supplied arguments. Finally, the
client detaches from the target VM.

A VirtualMachine is safe for use by multiple concurrent threads.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected VirtualMachine​(
AttachProvider
provider,

String
id)

Initializes a new instance of this class.

**Parameters:**
- provider

- The attach provider creating this class.
- id

- The abstract identifier that identifies the Java virtual machine.

**Throws:**
- NullPointerException

- If

provider

or

id

is

null

.

---

### Method Details

#### public static
List
<
VirtualMachineDescriptor
> list()

Return a list of Java virtual machines.

This method returns a list of Java

VirtualMachineDescriptor

elements.
The list is an aggregation of the virtual machine
descriptor lists obtained by invoking the

listVirtualMachines

method of all installed

attach providers

.
If there are no Java virtual machines known to any provider
then an empty list is returned.

**Returns:**
- The list of virtual machine descriptors.

---

#### public static
VirtualMachine
attach​(
String
id)
throws
AttachNotSupportedException
,

IOException

Attaches to a Java virtual machine.

This method obtains the list of attach providers by invoking the

AttachProvider.providers()

method. It then iterates overs the list
and invokes each provider's

attachVirtualMachine

method in turn. If a provider successfully
attaches then the iteration terminates, and the VirtualMachine created
by the provider that successfully attached is returned by this method.
If the

attachVirtualMachine

method of all providers throws

AttachNotSupportedException

then this method also throws

AttachNotSupportedException

.
This means that

AttachNotSupportedException

is thrown when
the identifier provided to this method is invalid, or the identifier
corresponds to a Java virtual machine that does not exist, or none
of the providers can attach to it. This exception is also thrown if

AttachProvider.providers()

returns an empty list.

**Parameters:**
- id

- The abstract identifier that identifies the Java virtual machine.

**Returns:**
- A VirtualMachine representing the target VM.

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

AttachPermission

("attachVirtualMachine")

, or another permission
required by the implementation.
- AttachNotSupportedException

- If the

attachVirtualmachine

method of all installed
providers throws

AttachNotSupportedException

, or
there aren't any providers installed.
- IOException

- If an I/O error occurs
- NullPointerException

- If

id

is

null

.

---

#### public static
VirtualMachine
attach​(
VirtualMachineDescriptor
vmd)
throws
AttachNotSupportedException
,

IOException

Attaches to a Java virtual machine.

This method first invokes the

provider()

method
of the given virtual machine descriptor to obtain the attach provider. It
then invokes the attach provider's

attachVirtualMachine

to attach to the target VM.

**Parameters:**
- vmd

- The virtual machine descriptor.

**Returns:**
- A VirtualMachine representing the target VM.

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

AttachPermission

("attachVirtualMachine")

, or another permission
required by the implementation.
- AttachNotSupportedException

- If the attach provider's

attachVirtualmachine

throws

AttachNotSupportedException

.
- IOException

- If an I/O error occurs
- NullPointerException

- If

vmd

is

null

.

---

#### public abstract void detach()
throws
IOException

Detach from the virtual machine.

After detaching from the virtual machine, any further attempt to invoke
operations on that virtual machine will cause an

IOException

to be thrown. If an operation (such as

loadAgent

for example) is in progress when this method is invoked then
the behaviour is implementation dependent. In other words, it is
implementation specific if the operation completes or throws

IOException

.

If already detached from the virtual machine then invoking this
method has no effect.

**Throws:**
- IOException

- If an I/O error occurs

---

#### public final
AttachProvider
provider()

Returns the provider that created this virtual machine.

**Returns:**
- The provider that created this virtual machine.

---

#### public final
String
id()

Returns the identifier for this Java virtual machine.

**Returns:**
- The identifier for this Java virtual machine.

---

#### public abstract void loadAgentLibrary​(
String
agentLibrary,

String
options)
throws
AgentLoadException
,

AgentInitializationException
,

IOException

Loads an agent library.

A

JVM TI

client is called an

agent

. It is developed in a native language.
A JVM TI agent is deployed in a platform specific manner but it is typically the
platform equivalent of a dynamic library. Alternatively, it may be statically linked into the VM.
This method causes the given agent library to be loaded into the target
VM (if not already loaded or if not statically linked into the VM).
It then causes the target VM to invoke the

Agent_OnAttach

function
or, for a statically linked agent named 'L', the

Agent_OnAttach_L

function
as specified in the

JVM Tools Interface

specification.
Note that the

Agent_OnAttach[_L]

function is invoked even if the agent library was loaded prior to invoking
this method.

The agent library provided is the name of the agent library. It is interpreted
in the target virtual machine in an implementation-dependent manner. Typically an
implementation will expand the library name into an operating system specific file
name. For example, on UNIX systems, the name

L

might be expanded to

libL.so

, and located using the search path specified by the

LD_LIBRARY_PATH

environment variable. If the agent named 'L' is
statically linked into the VM then the VM must export a function named

Agent_OnAttach_L

.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

**Parameters:**
- agentLibrary

- The name of the agent library.
- options

- The options to provide to the

Agent_OnAttach[_L]

function (can be

null

).

**Throws:**
- AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
- AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
- IOException

- If an I/O error occurs
- NullPointerException

- If

agentLibrary

is

null

.

**See Also:**
- AgentInitializationException.returnValue()

---

#### public void loadAgentLibrary​(
String
agentLibrary)
throws
AgentLoadException
,

AgentInitializationException
,

IOException

Loads an agent library.

This convenience method works as if by invoking:

loadAgentLibrary

(agentLibrary, null);

**Parameters:**
- agentLibrary

- The name of the agent library.

**Throws:**
- AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
- AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
- IOException

- If an I/O error occurs
- NullPointerException

- If

agentLibrary

is

null

.

---

#### public abstract void loadAgentPath​(
String
agentPath,

String
options)
throws
AgentLoadException
,

AgentInitializationException
,

IOException

Load a native agent library by full pathname.

A

JVM TI

client is called an

agent

. It is developed in a native language.
A JVM TI agent is deployed in a platform specific manner but it is typically the
platform equivalent of a dynamic library. Alternatively, the native
library specified by the agentPath parameter may be statically
linked with the VM. The parsing of the agentPath parameter into
a statically linked library name is done in a platform
specific manner in the VM. For example, in UNIX, an agentPath parameter
of

/a/b/libL.so

would name a library 'L'.

See the JVM TI Specification for more details.

This method causes the given agent library to be loaded into the target
VM (if not already loaded or if not statically linked into the VM).
It then causes the target VM to invoke the

Agent_OnAttach

function or, for a statically linked agent named 'L', the

Agent_OnAttach_L

function as specified in the

JVM Tools Interface

specification.
Note that the

Agent_OnAttach[_L]

function is invoked even if the agent library was loaded prior to invoking
this method.

The agent library provided is the absolute path from which to load the
agent library. Unlike

loadAgentLibrary

, the library name
is not expanded in the target virtual machine.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

**Parameters:**
- agentPath

- The full path of the agent library.
- options

- The options to provide to the

Agent_OnAttach[_L]

function (can be

null

).

**Throws:**
- AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
- AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
- IOException

- If an I/O error occurs
- NullPointerException

- If

agentPath

is

null

.

**See Also:**
- AgentInitializationException.returnValue()

---

#### public void loadAgentPath​(
String
agentPath)
throws
AgentLoadException
,

AgentInitializationException
,

IOException

Load a native agent library by full pathname.

This convenience method works as if by invoking:

loadAgentPath

(agentLibrary, null);

**Parameters:**
- agentPath

- The full path to the agent library.

**Throws:**
- AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
- AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
- IOException

- If an I/O error occurs
- NullPointerException

- If

agentPath

is

null

.

---

#### public abstract void loadAgent​(
String
agent,

String
options)
throws
AgentLoadException
,

AgentInitializationException
,

IOException

Loads an agent.

The agent provided to this method is a path name to a JAR file on the file
system of the target virtual machine. This path is passed to the target virtual
machine where it is interpreted. The target virtual machine attempts to start
the agent as specified by the

java.lang.instrument

specification.
That is, the specified JAR file is added to the system class path (of the target
virtual machine), and the

agentmain

method of the agent class, specified
by the

Agent-Class

attribute in the JAR manifest, is invoked. This
method completes when the

agentmain

method completes.

**Parameters:**
- agent

- Path to the JAR file containing the agent.
- options

- The options to provide to the agent's

agentmain

method (can be

null

).

**Throws:**
- AgentLoadException

- If the agent does not exist, or cannot be started in the manner
specified in the

java.lang.instrument

specification.
- AgentInitializationException

- If the

agentmain

throws an exception
- IOException

- If an I/O error occurs
- NullPointerException

- If

agent

is

null

.

---

#### public void loadAgent​(
String
agent)
throws
AgentLoadException
,

AgentInitializationException
,

IOException

Loads an agent.

This convenience method works as if by invoking:

loadAgent

(agent, null);

**Parameters:**
- agent

- Path to the JAR file containing the agent.

**Throws:**
- AgentLoadException

- If the agent does not exist, or cannot be started in the manner
specified in the

java.lang.instrument

specification.
- AgentInitializationException

- If the

agentmain

throws an exception
- IOException

- If an I/O error occurs
- NullPointerException

- If

agent

is

null

.

---

#### public abstract
Properties
getSystemProperties()
throws
IOException

Returns the current system properties in the target virtual machine.

This method returns the system properties in the target virtual
machine. Properties whose key or value is not a

String

are
omitted. The method is approximately equivalent to the invocation of the
method

System.getProperties

in the target virtual machine except that properties with a key or
value that is not a

String

are not included.

This method is typically used to decide which agent to load into
the target virtual machine with

loadAgent

, or

loadAgentLibrary

. For example, the

java.home

or

user.dir

properties might be
use to create the path to the agent library or JAR file.

**Returns:**
- The system properties

**Throws:**
- AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
- IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.

**See Also:**
- System.getProperties()

,

loadAgentLibrary(java.lang.String, java.lang.String)

,

loadAgent(java.lang.String, java.lang.String)

---

#### public abstract
Properties
getAgentProperties()
throws
IOException

Returns the current

agent properties

in the target virtual
machine.

The target virtual machine can maintain a list of properties on
behalf of agents. The manner in which this is done, the names of the
properties, and the types of values that are allowed, is implementation
specific. Agent properties are typically used to store communication
end-points and other agent configuration details. For example, a debugger
agent might create an agent property for its transport address.

This method returns the agent properties whose key and value is a

String

. Properties whose key or value is not a

String

are omitted. If there are no agent properties maintained in the target
virtual machine then an empty property list is returned.

**Returns:**
- The agent properties

**Throws:**
- AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
- IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.

---

#### public abstract void startManagementAgent​(
Properties
agentProperties)
throws
IOException

Starts the JMX management agent in the target virtual machine.

The configuration properties are the same as those specified on
the command line when starting the JMX management agent. In the same
way as on the command line, you need to specify at least the

com.sun.management.jmxremote.port

property.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

**Parameters:**
- agentProperties

- A Properties object containing the configuration properties
for the agent.

**Throws:**
- AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
- IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.
- IllegalArgumentException

- If keys or values in agentProperties are invalid.
- NullPointerException

- If agentProperties is null.

**Since:**
- 1.8

---

#### public abstract
String
startLocalManagementAgent()
throws
IOException

Starts the local JMX management agent in the target virtual machine.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

**Returns:**
- The String representation of the local connector's service address.
The value can be parsed by the

JMXServiceURL(String)

constructor.

**Throws:**
- AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
- IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.

**Since:**
- 1.8

---

#### public int hashCode()

Returns a hash-code value for this VirtualMachine. The hash
code is based upon the VirtualMachine's components, and satifies
the general contract of the

Object.hashCode

method.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- A hash-code value for this virtual machine

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
ob)

Tests this VirtualMachine for equality with another object.

If the given object is not a VirtualMachine then this
method returns

false

. For two VirtualMachines to
be considered equal requires that they both reference the same
provider, and their

identifiers

are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:**
- equals

in class

Object

**Parameters:**
- ob

- The object to which this object is to be compared

**Returns:**
- true

if, and only if, the given object is
a VirtualMachine that is equal to this
VirtualMachine.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns the string representation of the

VirtualMachine

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class VirtualMachine

java.lang.Object

- com.sun.tools.attach.VirtualMachine

com.sun.tools.attach.VirtualMachine

```java
public abstract class
VirtualMachine

extends
Object
```

A Java virtual machine.

A

VirtualMachine

represents a Java virtual machine to which this
Java virtual machine has attached. The Java virtual machine to which it is
attached is sometimes called the

target virtual machine

, or

target VM

.
An application (typically a tool such as a managemet console or profiler) uses a
VirtualMachine to load an agent into the target VM. For example, a profiler tool
written in the Java Language might attach to a running application and load its
profiler agent to profile the running application.

A VirtualMachine is obtained by invoking the

attach

method
with an identifier that identifies the target virtual machine. The identifier is
implementation-dependent but is typically the process identifier (or pid) in
environments where each Java virtual machine runs in its own operating system process.
Alternatively, a

VirtualMachine

instance is obtained by invoking the

attach

method with a

VirtualMachineDescriptor

obtained
from the list of virtual machine descriptors returned by the

list

method.
Once a reference to a virtual machine is obtained, the

loadAgent

,

loadAgentLibrary

, and

loadAgentPath

methods are used to load agents into target virtual machine. The

loadAgent

method is used to load agents that are written in the Java
Language and deployed in a

JAR file

. (See

java.lang.instrument

for a detailed description on how these agents
are loaded and started). The

loadAgentLibrary

and

loadAgentPath

methods are used to load agents that
are deployed either in a dynamic library or statically linked into the VM and
make use of the

JVM Tools Interface

.

In addition to loading agents a VirtualMachine provides read access to the

system properties

in the target VM.
This can be useful in some environments where properties such as

java.home

,

os.name

, or

os.arch

are
used to construct the path to agent that will be loaded into the target VM.

The following example demonstrates how VirtualMachine may be used:

```java
// attach to target VM
VirtualMachine vm = VirtualMachine.attach("2177");

// start management agent
Properties props = new Properties();
props.put("com.sun.management.jmxremote.port", "5000");
vm.startManagementAgent(props);

// detach
vm.detach();
```

In this example we attach to a Java virtual machine that is identified by
the process identifier

2177

. Then the JMX management agent is
started in the target process using the supplied arguments. Finally, the
client detaches from the target VM.

A VirtualMachine is safe for use by multiple concurrent threads.

**Since:** 1.6

public abstract class

VirtualMachine

extends

Object

A Java virtual machine.

A

VirtualMachine

represents a Java virtual machine to which this
Java virtual machine has attached. The Java virtual machine to which it is
attached is sometimes called the

target virtual machine

, or

target VM

.
An application (typically a tool such as a managemet console or profiler) uses a
VirtualMachine to load an agent into the target VM. For example, a profiler tool
written in the Java Language might attach to a running application and load its
profiler agent to profile the running application.

A VirtualMachine is obtained by invoking the

attach

method
with an identifier that identifies the target virtual machine. The identifier is
implementation-dependent but is typically the process identifier (or pid) in
environments where each Java virtual machine runs in its own operating system process.
Alternatively, a

VirtualMachine

instance is obtained by invoking the

attach

method with a

VirtualMachineDescriptor

obtained
from the list of virtual machine descriptors returned by the

list

method.
Once a reference to a virtual machine is obtained, the

loadAgent

,

loadAgentLibrary

, and

loadAgentPath

methods are used to load agents into target virtual machine. The

loadAgent

method is used to load agents that are written in the Java
Language and deployed in a

JAR file

. (See

java.lang.instrument

for a detailed description on how these agents
are loaded and started). The

loadAgentLibrary

and

loadAgentPath

methods are used to load agents that
are deployed either in a dynamic library or statically linked into the VM and
make use of the

JVM Tools Interface

.

In addition to loading agents a VirtualMachine provides read access to the

system properties

in the target VM.
This can be useful in some environments where properties such as

java.home

,

os.name

, or

os.arch

are
used to construct the path to agent that will be loaded into the target VM.

The following example demonstrates how VirtualMachine may be used:

```java
// attach to target VM
VirtualMachine vm = VirtualMachine.attach("2177");

// start management agent
Properties props = new Properties();
props.put("com.sun.management.jmxremote.port", "5000");
vm.startManagementAgent(props);

// detach
vm.detach();
```

In this example we attach to a Java virtual machine that is identified by
the process identifier

2177

. Then the JMX management agent is
started in the target process using the supplied arguments. Finally, the
client detaches from the target VM.

A VirtualMachine is safe for use by multiple concurrent threads.

A

VirtualMachine

represents a Java virtual machine to which this
Java virtual machine has attached. The Java virtual machine to which it is
attached is sometimes called the

target virtual machine

, or

target VM

.
An application (typically a tool such as a managemet console or profiler) uses a
VirtualMachine to load an agent into the target VM. For example, a profiler tool
written in the Java Language might attach to a running application and load its
profiler agent to profile the running application.

A VirtualMachine is obtained by invoking the

attach

method
with an identifier that identifies the target virtual machine. The identifier is
implementation-dependent but is typically the process identifier (or pid) in
environments where each Java virtual machine runs in its own operating system process.
Alternatively, a

VirtualMachine

instance is obtained by invoking the

attach

method with a

VirtualMachineDescriptor

obtained
from the list of virtual machine descriptors returned by the

list

method.
Once a reference to a virtual machine is obtained, the

loadAgent

,

loadAgentLibrary

, and

loadAgentPath

methods are used to load agents into target virtual machine. The

loadAgent

method is used to load agents that are written in the Java
Language and deployed in a

JAR file

. (See

java.lang.instrument

for a detailed description on how these agents
are loaded and started). The

loadAgentLibrary

and

loadAgentPath

methods are used to load agents that
are deployed either in a dynamic library or statically linked into the VM and
make use of the

JVM Tools Interface

.

In addition to loading agents a VirtualMachine provides read access to the

system properties

in the target VM.
This can be useful in some environments where properties such as

java.home

,

os.name

, or

os.arch

are
used to construct the path to agent that will be loaded into the target VM.

The following example demonstrates how VirtualMachine may be used:

```java
// attach to target VM
VirtualMachine vm = VirtualMachine.attach("2177");

// start management agent
Properties props = new Properties();
props.put("com.sun.management.jmxremote.port", "5000");
vm.startManagementAgent(props);

// detach
vm.detach();
```

In this example we attach to a Java virtual machine that is identified by
the process identifier

2177

. Then the JMX management agent is
started in the target process using the supplied arguments. Finally, the
client detaches from the target VM.

A VirtualMachine is safe for use by multiple concurrent threads.

The following example demonstrates how VirtualMachine may be used:

// attach to target VM
VirtualMachine vm = VirtualMachine.attach("2177");

// start management agent
Properties props = new Properties();
props.put("com.sun.management.jmxremote.port", "5000");
vm.startManagementAgent(props);

// detach
vm.detach();

In this example we attach to a Java virtual machine that is identified by
the process identifier

2177

. Then the JMX management agent is
started in the target process using the supplied arguments. Finally, the
client detaches from the target VM.

A VirtualMachine is safe for use by multiple concurrent threads.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

VirtualMachine

​(

AttachProvider

provider,

String

id)

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

VirtualMachine

attach

​(

VirtualMachineDescriptor

vmd)

Attaches to a Java virtual machine.

static

VirtualMachine

attach

​(

String

id)

Attaches to a Java virtual machine.

abstract void

detach

()

Detach from the virtual machine.

boolean

equals

​(

Object

ob)

Tests this VirtualMachine for equality with another object.

abstract

Properties

getAgentProperties

()

Returns the current

agent properties

in the target virtual
machine.

abstract

Properties

getSystemProperties

()

Returns the current system properties in the target virtual machine.

int

hashCode

()

Returns a hash-code value for this VirtualMachine.

String

id

()

Returns the identifier for this Java virtual machine.

static

List

<

VirtualMachineDescriptor

>

list

()

Return a list of Java virtual machines.

void

loadAgent

​(

String

agent)

Loads an agent.

abstract void

loadAgent

​(

String

agent,

String

options)

Loads an agent.

void

loadAgentLibrary

​(

String

agentLibrary)

Loads an agent library.

abstract void

loadAgentLibrary

​(

String

agentLibrary,

String

options)

Loads an agent library.

void

loadAgentPath

​(

String

agentPath)

Load a native agent library by full pathname.

abstract void

loadAgentPath

​(

String

agentPath,

String

options)

Load a native agent library by full pathname.

AttachProvider

provider

()

Returns the provider that created this virtual machine.

abstract

String

startLocalManagementAgent

()

Starts the local JMX management agent in the target virtual machine.

abstract void

startManagementAgent

​(

Properties

agentProperties)

Starts the JMX management agent in the target virtual machine.

String

toString

()

Returns the string representation of the

VirtualMachine

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Modifier

Constructor

Description

protected

VirtualMachine

​(

AttachProvider

provider,

String

id)

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

VirtualMachine

attach

​(

VirtualMachineDescriptor

vmd)

Attaches to a Java virtual machine.

static

VirtualMachine

attach

​(

String

id)

Attaches to a Java virtual machine.

abstract void

detach

()

Detach from the virtual machine.

boolean

equals

​(

Object

ob)

Tests this VirtualMachine for equality with another object.

abstract

Properties

getAgentProperties

()

Returns the current

agent properties

in the target virtual
machine.

abstract

Properties

getSystemProperties

()

Returns the current system properties in the target virtual machine.

int

hashCode

()

Returns a hash-code value for this VirtualMachine.

String

id

()

Returns the identifier for this Java virtual machine.

static

List

<

VirtualMachineDescriptor

>

list

()

Return a list of Java virtual machines.

void

loadAgent

​(

String

agent)

Loads an agent.

abstract void

loadAgent

​(

String

agent,

String

options)

Loads an agent.

void

loadAgentLibrary

​(

String

agentLibrary)

Loads an agent library.

abstract void

loadAgentLibrary

​(

String

agentLibrary,

String

options)

Loads an agent library.

void

loadAgentPath

​(

String

agentPath)

Load a native agent library by full pathname.

abstract void

loadAgentPath

​(

String

agentPath,

String

options)

Load a native agent library by full pathname.

AttachProvider

provider

()

Returns the provider that created this virtual machine.

abstract

String

startLocalManagementAgent

()

Starts the local JMX management agent in the target virtual machine.

abstract void

startManagementAgent

​(

Properties

agentProperties)

Starts the JMX management agent in the target virtual machine.

String

toString

()

Returns the string representation of the

VirtualMachine

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Attaches to a Java virtual machine.

Detach from the virtual machine.

Tests this VirtualMachine for equality with another object.

Returns the current

agent properties

in the target virtual
machine.

Returns the current system properties in the target virtual machine.

Returns a hash-code value for this VirtualMachine.

Returns the identifier for this Java virtual machine.

Return a list of Java virtual machines.

Loads an agent.

Loads an agent library.

Load a native agent library by full pathname.

Returns the provider that created this virtual machine.

Starts the local JMX management agent in the target virtual machine.

Starts the JMX management agent in the target virtual machine.

Returns the string representation of the

VirtualMachine

.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- VirtualMachine

```java
protected VirtualMachine​(
AttachProvider
provider,

String
id)
```

Initializes a new instance of this class.

**Parameters:** provider

- The attach provider creating this class.
**Parameters:** id

- The abstract identifier that identifies the Java virtual machine.
**Throws:** NullPointerException

- If

provider

or

id

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- list

```java
public static
List
<
VirtualMachineDescriptor
> list()
```

Return a list of Java virtual machines.

This method returns a list of Java

VirtualMachineDescriptor

elements.
The list is an aggregation of the virtual machine
descriptor lists obtained by invoking the

listVirtualMachines

method of all installed

attach providers

.
If there are no Java virtual machines known to any provider
then an empty list is returned.

**Returns:** The list of virtual machine descriptors.

- attach

```java
public static
VirtualMachine
attach​(
String
id)
throws
AttachNotSupportedException
,

IOException
```

Attaches to a Java virtual machine.

This method obtains the list of attach providers by invoking the

AttachProvider.providers()

method. It then iterates overs the list
and invokes each provider's

attachVirtualMachine

method in turn. If a provider successfully
attaches then the iteration terminates, and the VirtualMachine created
by the provider that successfully attached is returned by this method.
If the

attachVirtualMachine

method of all providers throws

AttachNotSupportedException

then this method also throws

AttachNotSupportedException

.
This means that

AttachNotSupportedException

is thrown when
the identifier provided to this method is invalid, or the identifier
corresponds to a Java virtual machine that does not exist, or none
of the providers can attach to it. This exception is also thrown if

AttachProvider.providers()

returns an empty list.

**Parameters:** id

- The abstract identifier that identifies the Java virtual machine.
**Returns:** A VirtualMachine representing the target VM.
**Throws:** SecurityException

- If a security manager has been installed and it denies

AttachPermission

("attachVirtualMachine")

, or another permission
required by the implementation.
**Throws:** AttachNotSupportedException

- If the

attachVirtualmachine

method of all installed
providers throws

AttachNotSupportedException

, or
there aren't any providers installed.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

id

is

null

.

- attach

```java
public static
VirtualMachine
attach​(
VirtualMachineDescriptor
vmd)
throws
AttachNotSupportedException
,

IOException
```

Attaches to a Java virtual machine.

This method first invokes the

provider()

method
of the given virtual machine descriptor to obtain the attach provider. It
then invokes the attach provider's

attachVirtualMachine

to attach to the target VM.

**Parameters:** vmd

- The virtual machine descriptor.
**Returns:** A VirtualMachine representing the target VM.
**Throws:** SecurityException

- If a security manager has been installed and it denies

AttachPermission

("attachVirtualMachine")

, or another permission
required by the implementation.
**Throws:** AttachNotSupportedException

- If the attach provider's

attachVirtualmachine

throws

AttachNotSupportedException

.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

vmd

is

null

.

- detach

```java
public abstract void detach()
throws
IOException
```

Detach from the virtual machine.

After detaching from the virtual machine, any further attempt to invoke
operations on that virtual machine will cause an

IOException

to be thrown. If an operation (such as

loadAgent

for example) is in progress when this method is invoked then
the behaviour is implementation dependent. In other words, it is
implementation specific if the operation completes or throws

IOException

.

If already detached from the virtual machine then invoking this
method has no effect.

**Throws:** IOException

- If an I/O error occurs

- provider

```java
public final
AttachProvider
provider()
```

Returns the provider that created this virtual machine.

**Returns:** The provider that created this virtual machine.

- id

```java
public final
String
id()
```

Returns the identifier for this Java virtual machine.

**Returns:** The identifier for this Java virtual machine.

- loadAgentLibrary

```java
public abstract void loadAgentLibrary​(
String
agentLibrary,

String
options)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Loads an agent library.

A

JVM TI

client is called an

agent

. It is developed in a native language.
A JVM TI agent is deployed in a platform specific manner but it is typically the
platform equivalent of a dynamic library. Alternatively, it may be statically linked into the VM.
This method causes the given agent library to be loaded into the target
VM (if not already loaded or if not statically linked into the VM).
It then causes the target VM to invoke the

Agent_OnAttach

function
or, for a statically linked agent named 'L', the

Agent_OnAttach_L

function
as specified in the

JVM Tools Interface

specification.
Note that the

Agent_OnAttach[_L]

function is invoked even if the agent library was loaded prior to invoking
this method.

The agent library provided is the name of the agent library. It is interpreted
in the target virtual machine in an implementation-dependent manner. Typically an
implementation will expand the library name into an operating system specific file
name. For example, on UNIX systems, the name

L

might be expanded to

libL.so

, and located using the search path specified by the

LD_LIBRARY_PATH

environment variable. If the agent named 'L' is
statically linked into the VM then the VM must export a function named

Agent_OnAttach_L

.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

**Parameters:** agentLibrary

- The name of the agent library.
**Parameters:** options

- The options to provide to the

Agent_OnAttach[_L]

function (can be

null

).
**Throws:** AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
**Throws:** AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agentLibrary

is

null

.
**See Also:** AgentInitializationException.returnValue()

- loadAgentLibrary

```java
public void loadAgentLibrary​(
String
agentLibrary)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Loads an agent library.

This convenience method works as if by invoking:

loadAgentLibrary

(agentLibrary, null);

**Parameters:** agentLibrary

- The name of the agent library.
**Throws:** AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
**Throws:** AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agentLibrary

is

null

.

- loadAgentPath

```java
public abstract void loadAgentPath​(
String
agentPath,

String
options)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Load a native agent library by full pathname.

A

JVM TI

client is called an

agent

. It is developed in a native language.
A JVM TI agent is deployed in a platform specific manner but it is typically the
platform equivalent of a dynamic library. Alternatively, the native
library specified by the agentPath parameter may be statically
linked with the VM. The parsing of the agentPath parameter into
a statically linked library name is done in a platform
specific manner in the VM. For example, in UNIX, an agentPath parameter
of

/a/b/libL.so

would name a library 'L'.

See the JVM TI Specification for more details.

This method causes the given agent library to be loaded into the target
VM (if not already loaded or if not statically linked into the VM).
It then causes the target VM to invoke the

Agent_OnAttach

function or, for a statically linked agent named 'L', the

Agent_OnAttach_L

function as specified in the

JVM Tools Interface

specification.
Note that the

Agent_OnAttach[_L]

function is invoked even if the agent library was loaded prior to invoking
this method.

The agent library provided is the absolute path from which to load the
agent library. Unlike

loadAgentLibrary

, the library name
is not expanded in the target virtual machine.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

**Parameters:** agentPath

- The full path of the agent library.
**Parameters:** options

- The options to provide to the

Agent_OnAttach[_L]

function (can be

null

).
**Throws:** AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
**Throws:** AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agentPath

is

null

.
**See Also:** AgentInitializationException.returnValue()

- loadAgentPath

```java
public void loadAgentPath​(
String
agentPath)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Load a native agent library by full pathname.

This convenience method works as if by invoking:

loadAgentPath

(agentLibrary, null);

**Parameters:** agentPath

- The full path to the agent library.
**Throws:** AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
**Throws:** AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agentPath

is

null

.

- loadAgent

```java
public abstract void loadAgent​(
String
agent,

String
options)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Loads an agent.

The agent provided to this method is a path name to a JAR file on the file
system of the target virtual machine. This path is passed to the target virtual
machine where it is interpreted. The target virtual machine attempts to start
the agent as specified by the

java.lang.instrument

specification.
That is, the specified JAR file is added to the system class path (of the target
virtual machine), and the

agentmain

method of the agent class, specified
by the

Agent-Class

attribute in the JAR manifest, is invoked. This
method completes when the

agentmain

method completes.

**Parameters:** agent

- Path to the JAR file containing the agent.
**Parameters:** options

- The options to provide to the agent's

agentmain

method (can be

null

).
**Throws:** AgentLoadException

- If the agent does not exist, or cannot be started in the manner
specified in the

java.lang.instrument

specification.
**Throws:** AgentInitializationException

- If the

agentmain

throws an exception
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agent

is

null

.

- loadAgent

```java
public void loadAgent​(
String
agent)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Loads an agent.

This convenience method works as if by invoking:

loadAgent

(agent, null);

**Parameters:** agent

- Path to the JAR file containing the agent.
**Throws:** AgentLoadException

- If the agent does not exist, or cannot be started in the manner
specified in the

java.lang.instrument

specification.
**Throws:** AgentInitializationException

- If the

agentmain

throws an exception
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agent

is

null

.

- getSystemProperties

```java
public abstract
Properties
getSystemProperties()
throws
IOException
```

Returns the current system properties in the target virtual machine.

This method returns the system properties in the target virtual
machine. Properties whose key or value is not a

String

are
omitted. The method is approximately equivalent to the invocation of the
method

System.getProperties

in the target virtual machine except that properties with a key or
value that is not a

String

are not included.

This method is typically used to decide which agent to load into
the target virtual machine with

loadAgent

, or

loadAgentLibrary

. For example, the

java.home

or

user.dir

properties might be
use to create the path to the agent library or JAR file.

**Returns:** The system properties
**Throws:** AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
**Throws:** IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.
**See Also:** System.getProperties()

,

loadAgentLibrary(java.lang.String, java.lang.String)

,

loadAgent(java.lang.String, java.lang.String)

- getAgentProperties

```java
public abstract
Properties
getAgentProperties()
throws
IOException
```

Returns the current

agent properties

in the target virtual
machine.

The target virtual machine can maintain a list of properties on
behalf of agents. The manner in which this is done, the names of the
properties, and the types of values that are allowed, is implementation
specific. Agent properties are typically used to store communication
end-points and other agent configuration details. For example, a debugger
agent might create an agent property for its transport address.

This method returns the agent properties whose key and value is a

String

. Properties whose key or value is not a

String

are omitted. If there are no agent properties maintained in the target
virtual machine then an empty property list is returned.

**Returns:** The agent properties
**Throws:** AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
**Throws:** IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.

- startManagementAgent

```java
public abstract void startManagementAgent​(
Properties
agentProperties)
throws
IOException
```

Starts the JMX management agent in the target virtual machine.

The configuration properties are the same as those specified on
the command line when starting the JMX management agent. In the same
way as on the command line, you need to specify at least the

com.sun.management.jmxremote.port

property.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

**Parameters:** agentProperties

- A Properties object containing the configuration properties
for the agent.
**Throws:** AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
**Throws:** IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.
**Throws:** IllegalArgumentException

- If keys or values in agentProperties are invalid.
**Throws:** NullPointerException

- If agentProperties is null.
**Since:** 1.8

- startLocalManagementAgent

```java
public abstract
String
startLocalManagementAgent()
throws
IOException
```

Starts the local JMX management agent in the target virtual machine.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

**Returns:** The String representation of the local connector's service address.
The value can be parsed by the

JMXServiceURL(String)

constructor.
**Throws:** AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
**Throws:** IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.
**Since:** 1.8

- hashCode

```java
public int hashCode()
```

Returns a hash-code value for this VirtualMachine. The hash
code is based upon the VirtualMachine's components, and satifies
the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** A hash-code value for this virtual machine
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this VirtualMachine for equality with another object.

If the given object is not a VirtualMachine then this
method returns

false

. For two VirtualMachines to
be considered equal requires that they both reference the same
provider, and their

identifiers

are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- The object to which this object is to be compared
**Returns:** true

if, and only if, the given object is
a VirtualMachine that is equal to this
VirtualMachine.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns the string representation of the

VirtualMachine

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- VirtualMachine

```java
protected VirtualMachine​(
AttachProvider
provider,

String
id)
```

Initializes a new instance of this class.

**Parameters:** provider

- The attach provider creating this class.
**Parameters:** id

- The abstract identifier that identifies the Java virtual machine.
**Throws:** NullPointerException

- If

provider

or

id

is

null

.

---

#### Constructor Detail

VirtualMachine

```java
protected VirtualMachine​(
AttachProvider
provider,

String
id)
```

Initializes a new instance of this class.

**Parameters:** provider

- The attach provider creating this class.
**Parameters:** id

- The abstract identifier that identifies the Java virtual machine.
**Throws:** NullPointerException

- If

provider

or

id

is

null

.

---

#### VirtualMachine

protected VirtualMachine​(

AttachProvider

provider,

String

id)

Initializes a new instance of this class.

Method Detail

- list

```java
public static
List
<
VirtualMachineDescriptor
> list()
```

Return a list of Java virtual machines.

This method returns a list of Java

VirtualMachineDescriptor

elements.
The list is an aggregation of the virtual machine
descriptor lists obtained by invoking the

listVirtualMachines

method of all installed

attach providers

.
If there are no Java virtual machines known to any provider
then an empty list is returned.

**Returns:** The list of virtual machine descriptors.

- attach

```java
public static
VirtualMachine
attach​(
String
id)
throws
AttachNotSupportedException
,

IOException
```

Attaches to a Java virtual machine.

This method obtains the list of attach providers by invoking the

AttachProvider.providers()

method. It then iterates overs the list
and invokes each provider's

attachVirtualMachine

method in turn. If a provider successfully
attaches then the iteration terminates, and the VirtualMachine created
by the provider that successfully attached is returned by this method.
If the

attachVirtualMachine

method of all providers throws

AttachNotSupportedException

then this method also throws

AttachNotSupportedException

.
This means that

AttachNotSupportedException

is thrown when
the identifier provided to this method is invalid, or the identifier
corresponds to a Java virtual machine that does not exist, or none
of the providers can attach to it. This exception is also thrown if

AttachProvider.providers()

returns an empty list.

**Parameters:** id

- The abstract identifier that identifies the Java virtual machine.
**Returns:** A VirtualMachine representing the target VM.
**Throws:** SecurityException

- If a security manager has been installed and it denies

AttachPermission

("attachVirtualMachine")

, or another permission
required by the implementation.
**Throws:** AttachNotSupportedException

- If the

attachVirtualmachine

method of all installed
providers throws

AttachNotSupportedException

, or
there aren't any providers installed.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

id

is

null

.

- attach

```java
public static
VirtualMachine
attach​(
VirtualMachineDescriptor
vmd)
throws
AttachNotSupportedException
,

IOException
```

Attaches to a Java virtual machine.

This method first invokes the

provider()

method
of the given virtual machine descriptor to obtain the attach provider. It
then invokes the attach provider's

attachVirtualMachine

to attach to the target VM.

**Parameters:** vmd

- The virtual machine descriptor.
**Returns:** A VirtualMachine representing the target VM.
**Throws:** SecurityException

- If a security manager has been installed and it denies

AttachPermission

("attachVirtualMachine")

, or another permission
required by the implementation.
**Throws:** AttachNotSupportedException

- If the attach provider's

attachVirtualmachine

throws

AttachNotSupportedException

.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

vmd

is

null

.

- detach

```java
public abstract void detach()
throws
IOException
```

Detach from the virtual machine.

After detaching from the virtual machine, any further attempt to invoke
operations on that virtual machine will cause an

IOException

to be thrown. If an operation (such as

loadAgent

for example) is in progress when this method is invoked then
the behaviour is implementation dependent. In other words, it is
implementation specific if the operation completes or throws

IOException

.

If already detached from the virtual machine then invoking this
method has no effect.

**Throws:** IOException

- If an I/O error occurs

- provider

```java
public final
AttachProvider
provider()
```

Returns the provider that created this virtual machine.

**Returns:** The provider that created this virtual machine.

- id

```java
public final
String
id()
```

Returns the identifier for this Java virtual machine.

**Returns:** The identifier for this Java virtual machine.

- loadAgentLibrary

```java
public abstract void loadAgentLibrary​(
String
agentLibrary,

String
options)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Loads an agent library.

A

JVM TI

client is called an

agent

. It is developed in a native language.
A JVM TI agent is deployed in a platform specific manner but it is typically the
platform equivalent of a dynamic library. Alternatively, it may be statically linked into the VM.
This method causes the given agent library to be loaded into the target
VM (if not already loaded or if not statically linked into the VM).
It then causes the target VM to invoke the

Agent_OnAttach

function
or, for a statically linked agent named 'L', the

Agent_OnAttach_L

function
as specified in the

JVM Tools Interface

specification.
Note that the

Agent_OnAttach[_L]

function is invoked even if the agent library was loaded prior to invoking
this method.

The agent library provided is the name of the agent library. It is interpreted
in the target virtual machine in an implementation-dependent manner. Typically an
implementation will expand the library name into an operating system specific file
name. For example, on UNIX systems, the name

L

might be expanded to

libL.so

, and located using the search path specified by the

LD_LIBRARY_PATH

environment variable. If the agent named 'L' is
statically linked into the VM then the VM must export a function named

Agent_OnAttach_L

.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

**Parameters:** agentLibrary

- The name of the agent library.
**Parameters:** options

- The options to provide to the

Agent_OnAttach[_L]

function (can be

null

).
**Throws:** AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
**Throws:** AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agentLibrary

is

null

.
**See Also:** AgentInitializationException.returnValue()

- loadAgentLibrary

```java
public void loadAgentLibrary​(
String
agentLibrary)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Loads an agent library.

This convenience method works as if by invoking:

loadAgentLibrary

(agentLibrary, null);

**Parameters:** agentLibrary

- The name of the agent library.
**Throws:** AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
**Throws:** AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agentLibrary

is

null

.

- loadAgentPath

```java
public abstract void loadAgentPath​(
String
agentPath,

String
options)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Load a native agent library by full pathname.

A

JVM TI

client is called an

agent

. It is developed in a native language.
A JVM TI agent is deployed in a platform specific manner but it is typically the
platform equivalent of a dynamic library. Alternatively, the native
library specified by the agentPath parameter may be statically
linked with the VM. The parsing of the agentPath parameter into
a statically linked library name is done in a platform
specific manner in the VM. For example, in UNIX, an agentPath parameter
of

/a/b/libL.so

would name a library 'L'.

See the JVM TI Specification for more details.

This method causes the given agent library to be loaded into the target
VM (if not already loaded or if not statically linked into the VM).
It then causes the target VM to invoke the

Agent_OnAttach

function or, for a statically linked agent named 'L', the

Agent_OnAttach_L

function as specified in the

JVM Tools Interface

specification.
Note that the

Agent_OnAttach[_L]

function is invoked even if the agent library was loaded prior to invoking
this method.

The agent library provided is the absolute path from which to load the
agent library. Unlike

loadAgentLibrary

, the library name
is not expanded in the target virtual machine.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

**Parameters:** agentPath

- The full path of the agent library.
**Parameters:** options

- The options to provide to the

Agent_OnAttach[_L]

function (can be

null

).
**Throws:** AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
**Throws:** AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agentPath

is

null

.
**See Also:** AgentInitializationException.returnValue()

- loadAgentPath

```java
public void loadAgentPath​(
String
agentPath)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Load a native agent library by full pathname.

This convenience method works as if by invoking:

loadAgentPath

(agentLibrary, null);

**Parameters:** agentPath

- The full path to the agent library.
**Throws:** AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
**Throws:** AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agentPath

is

null

.

- loadAgent

```java
public abstract void loadAgent​(
String
agent,

String
options)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Loads an agent.

The agent provided to this method is a path name to a JAR file on the file
system of the target virtual machine. This path is passed to the target virtual
machine where it is interpreted. The target virtual machine attempts to start
the agent as specified by the

java.lang.instrument

specification.
That is, the specified JAR file is added to the system class path (of the target
virtual machine), and the

agentmain

method of the agent class, specified
by the

Agent-Class

attribute in the JAR manifest, is invoked. This
method completes when the

agentmain

method completes.

**Parameters:** agent

- Path to the JAR file containing the agent.
**Parameters:** options

- The options to provide to the agent's

agentmain

method (can be

null

).
**Throws:** AgentLoadException

- If the agent does not exist, or cannot be started in the manner
specified in the

java.lang.instrument

specification.
**Throws:** AgentInitializationException

- If the

agentmain

throws an exception
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agent

is

null

.

- loadAgent

```java
public void loadAgent​(
String
agent)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Loads an agent.

This convenience method works as if by invoking:

loadAgent

(agent, null);

**Parameters:** agent

- Path to the JAR file containing the agent.
**Throws:** AgentLoadException

- If the agent does not exist, or cannot be started in the manner
specified in the

java.lang.instrument

specification.
**Throws:** AgentInitializationException

- If the

agentmain

throws an exception
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agent

is

null

.

- getSystemProperties

```java
public abstract
Properties
getSystemProperties()
throws
IOException
```

Returns the current system properties in the target virtual machine.

This method returns the system properties in the target virtual
machine. Properties whose key or value is not a

String

are
omitted. The method is approximately equivalent to the invocation of the
method

System.getProperties

in the target virtual machine except that properties with a key or
value that is not a

String

are not included.

This method is typically used to decide which agent to load into
the target virtual machine with

loadAgent

, or

loadAgentLibrary

. For example, the

java.home

or

user.dir

properties might be
use to create the path to the agent library or JAR file.

**Returns:** The system properties
**Throws:** AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
**Throws:** IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.
**See Also:** System.getProperties()

,

loadAgentLibrary(java.lang.String, java.lang.String)

,

loadAgent(java.lang.String, java.lang.String)

- getAgentProperties

```java
public abstract
Properties
getAgentProperties()
throws
IOException
```

Returns the current

agent properties

in the target virtual
machine.

The target virtual machine can maintain a list of properties on
behalf of agents. The manner in which this is done, the names of the
properties, and the types of values that are allowed, is implementation
specific. Agent properties are typically used to store communication
end-points and other agent configuration details. For example, a debugger
agent might create an agent property for its transport address.

This method returns the agent properties whose key and value is a

String

. Properties whose key or value is not a

String

are omitted. If there are no agent properties maintained in the target
virtual machine then an empty property list is returned.

**Returns:** The agent properties
**Throws:** AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
**Throws:** IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.

- startManagementAgent

```java
public abstract void startManagementAgent​(
Properties
agentProperties)
throws
IOException
```

Starts the JMX management agent in the target virtual machine.

The configuration properties are the same as those specified on
the command line when starting the JMX management agent. In the same
way as on the command line, you need to specify at least the

com.sun.management.jmxremote.port

property.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

**Parameters:** agentProperties

- A Properties object containing the configuration properties
for the agent.
**Throws:** AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
**Throws:** IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.
**Throws:** IllegalArgumentException

- If keys or values in agentProperties are invalid.
**Throws:** NullPointerException

- If agentProperties is null.
**Since:** 1.8

- startLocalManagementAgent

```java
public abstract
String
startLocalManagementAgent()
throws
IOException
```

Starts the local JMX management agent in the target virtual machine.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

**Returns:** The String representation of the local connector's service address.
The value can be parsed by the

JMXServiceURL(String)

constructor.
**Throws:** AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
**Throws:** IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.
**Since:** 1.8

- hashCode

```java
public int hashCode()
```

Returns a hash-code value for this VirtualMachine. The hash
code is based upon the VirtualMachine's components, and satifies
the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** A hash-code value for this virtual machine
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this VirtualMachine for equality with another object.

If the given object is not a VirtualMachine then this
method returns

false

. For two VirtualMachines to
be considered equal requires that they both reference the same
provider, and their

identifiers

are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- The object to which this object is to be compared
**Returns:** true

if, and only if, the given object is
a VirtualMachine that is equal to this
VirtualMachine.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns the string representation of the

VirtualMachine

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

list

```java
public static
List
<
VirtualMachineDescriptor
> list()
```

Return a list of Java virtual machines.

This method returns a list of Java

VirtualMachineDescriptor

elements.
The list is an aggregation of the virtual machine
descriptor lists obtained by invoking the

listVirtualMachines

method of all installed

attach providers

.
If there are no Java virtual machines known to any provider
then an empty list is returned.

**Returns:** The list of virtual machine descriptors.

---

#### list

public static

List

<

VirtualMachineDescriptor

> list()

Return a list of Java virtual machines.

This method returns a list of Java

VirtualMachineDescriptor

elements.
The list is an aggregation of the virtual machine
descriptor lists obtained by invoking the

listVirtualMachines

method of all installed

attach providers

.
If there are no Java virtual machines known to any provider
then an empty list is returned.

This method returns a list of Java

VirtualMachineDescriptor

elements.
The list is an aggregation of the virtual machine
descriptor lists obtained by invoking the

listVirtualMachines

method of all installed

attach providers

.
If there are no Java virtual machines known to any provider
then an empty list is returned.

attach

```java
public static
VirtualMachine
attach​(
String
id)
throws
AttachNotSupportedException
,

IOException
```

Attaches to a Java virtual machine.

This method obtains the list of attach providers by invoking the

AttachProvider.providers()

method. It then iterates overs the list
and invokes each provider's

attachVirtualMachine

method in turn. If a provider successfully
attaches then the iteration terminates, and the VirtualMachine created
by the provider that successfully attached is returned by this method.
If the

attachVirtualMachine

method of all providers throws

AttachNotSupportedException

then this method also throws

AttachNotSupportedException

.
This means that

AttachNotSupportedException

is thrown when
the identifier provided to this method is invalid, or the identifier
corresponds to a Java virtual machine that does not exist, or none
of the providers can attach to it. This exception is also thrown if

AttachProvider.providers()

returns an empty list.

**Parameters:** id

- The abstract identifier that identifies the Java virtual machine.
**Returns:** A VirtualMachine representing the target VM.
**Throws:** SecurityException

- If a security manager has been installed and it denies

AttachPermission

("attachVirtualMachine")

, or another permission
required by the implementation.
**Throws:** AttachNotSupportedException

- If the

attachVirtualmachine

method of all installed
providers throws

AttachNotSupportedException

, or
there aren't any providers installed.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

id

is

null

.

---

#### attach

public static

VirtualMachine

attach​(

String

id)
throws

AttachNotSupportedException

,

IOException

Attaches to a Java virtual machine.

This method obtains the list of attach providers by invoking the

AttachProvider.providers()

method. It then iterates overs the list
and invokes each provider's

attachVirtualMachine

method in turn. If a provider successfully
attaches then the iteration terminates, and the VirtualMachine created
by the provider that successfully attached is returned by this method.
If the

attachVirtualMachine

method of all providers throws

AttachNotSupportedException

then this method also throws

AttachNotSupportedException

.
This means that

AttachNotSupportedException

is thrown when
the identifier provided to this method is invalid, or the identifier
corresponds to a Java virtual machine that does not exist, or none
of the providers can attach to it. This exception is also thrown if

AttachProvider.providers()

returns an empty list.

This method obtains the list of attach providers by invoking the

AttachProvider.providers()

method. It then iterates overs the list
and invokes each provider's

attachVirtualMachine

method in turn. If a provider successfully
attaches then the iteration terminates, and the VirtualMachine created
by the provider that successfully attached is returned by this method.
If the

attachVirtualMachine

method of all providers throws

AttachNotSupportedException

then this method also throws

AttachNotSupportedException

.
This means that

AttachNotSupportedException

is thrown when
the identifier provided to this method is invalid, or the identifier
corresponds to a Java virtual machine that does not exist, or none
of the providers can attach to it. This exception is also thrown if

AttachProvider.providers()

returns an empty list.

attach

```java
public static
VirtualMachine
attach​(
VirtualMachineDescriptor
vmd)
throws
AttachNotSupportedException
,

IOException
```

Attaches to a Java virtual machine.

This method first invokes the

provider()

method
of the given virtual machine descriptor to obtain the attach provider. It
then invokes the attach provider's

attachVirtualMachine

to attach to the target VM.

**Parameters:** vmd

- The virtual machine descriptor.
**Returns:** A VirtualMachine representing the target VM.
**Throws:** SecurityException

- If a security manager has been installed and it denies

AttachPermission

("attachVirtualMachine")

, or another permission
required by the implementation.
**Throws:** AttachNotSupportedException

- If the attach provider's

attachVirtualmachine

throws

AttachNotSupportedException

.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

vmd

is

null

.

---

#### attach

public static

VirtualMachine

attach​(

VirtualMachineDescriptor

vmd)
throws

AttachNotSupportedException

,

IOException

Attaches to a Java virtual machine.

This method first invokes the

provider()

method
of the given virtual machine descriptor to obtain the attach provider. It
then invokes the attach provider's

attachVirtualMachine

to attach to the target VM.

This method first invokes the

provider()

method
of the given virtual machine descriptor to obtain the attach provider. It
then invokes the attach provider's

attachVirtualMachine

to attach to the target VM.

detach

```java
public abstract void detach()
throws
IOException
```

Detach from the virtual machine.

After detaching from the virtual machine, any further attempt to invoke
operations on that virtual machine will cause an

IOException

to be thrown. If an operation (such as

loadAgent

for example) is in progress when this method is invoked then
the behaviour is implementation dependent. In other words, it is
implementation specific if the operation completes or throws

IOException

.

If already detached from the virtual machine then invoking this
method has no effect.

**Throws:** IOException

- If an I/O error occurs

---

#### detach

public abstract void detach()
throws

IOException

Detach from the virtual machine.

After detaching from the virtual machine, any further attempt to invoke
operations on that virtual machine will cause an

IOException

to be thrown. If an operation (such as

loadAgent

for example) is in progress when this method is invoked then
the behaviour is implementation dependent. In other words, it is
implementation specific if the operation completes or throws

IOException

.

If already detached from the virtual machine then invoking this
method has no effect.

After detaching from the virtual machine, any further attempt to invoke
operations on that virtual machine will cause an

IOException

to be thrown. If an operation (such as

loadAgent

for example) is in progress when this method is invoked then
the behaviour is implementation dependent. In other words, it is
implementation specific if the operation completes or throws

IOException

.

If already detached from the virtual machine then invoking this
method has no effect.

If already detached from the virtual machine then invoking this
method has no effect.

provider

```java
public final
AttachProvider
provider()
```

Returns the provider that created this virtual machine.

**Returns:** The provider that created this virtual machine.

---

#### provider

public final

AttachProvider

provider()

Returns the provider that created this virtual machine.

id

```java
public final
String
id()
```

Returns the identifier for this Java virtual machine.

**Returns:** The identifier for this Java virtual machine.

---

#### id

public final

String

id()

Returns the identifier for this Java virtual machine.

loadAgentLibrary

```java
public abstract void loadAgentLibrary​(
String
agentLibrary,

String
options)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Loads an agent library.

A

JVM TI

client is called an

agent

. It is developed in a native language.
A JVM TI agent is deployed in a platform specific manner but it is typically the
platform equivalent of a dynamic library. Alternatively, it may be statically linked into the VM.
This method causes the given agent library to be loaded into the target
VM (if not already loaded or if not statically linked into the VM).
It then causes the target VM to invoke the

Agent_OnAttach

function
or, for a statically linked agent named 'L', the

Agent_OnAttach_L

function
as specified in the

JVM Tools Interface

specification.
Note that the

Agent_OnAttach[_L]

function is invoked even if the agent library was loaded prior to invoking
this method.

The agent library provided is the name of the agent library. It is interpreted
in the target virtual machine in an implementation-dependent manner. Typically an
implementation will expand the library name into an operating system specific file
name. For example, on UNIX systems, the name

L

might be expanded to

libL.so

, and located using the search path specified by the

LD_LIBRARY_PATH

environment variable. If the agent named 'L' is
statically linked into the VM then the VM must export a function named

Agent_OnAttach_L

.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

**Parameters:** agentLibrary

- The name of the agent library.
**Parameters:** options

- The options to provide to the

Agent_OnAttach[_L]

function (can be

null

).
**Throws:** AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
**Throws:** AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agentLibrary

is

null

.
**See Also:** AgentInitializationException.returnValue()

---

#### loadAgentLibrary

public abstract void loadAgentLibrary​(

String

agentLibrary,

String

options)
throws

AgentLoadException

,

AgentInitializationException

,

IOException

Loads an agent library.

A

JVM TI

client is called an

agent

. It is developed in a native language.
A JVM TI agent is deployed in a platform specific manner but it is typically the
platform equivalent of a dynamic library. Alternatively, it may be statically linked into the VM.
This method causes the given agent library to be loaded into the target
VM (if not already loaded or if not statically linked into the VM).
It then causes the target VM to invoke the

Agent_OnAttach

function
or, for a statically linked agent named 'L', the

Agent_OnAttach_L

function
as specified in the

JVM Tools Interface

specification.
Note that the

Agent_OnAttach[_L]

function is invoked even if the agent library was loaded prior to invoking
this method.

The agent library provided is the name of the agent library. It is interpreted
in the target virtual machine in an implementation-dependent manner. Typically an
implementation will expand the library name into an operating system specific file
name. For example, on UNIX systems, the name

L

might be expanded to

libL.so

, and located using the search path specified by the

LD_LIBRARY_PATH

environment variable. If the agent named 'L' is
statically linked into the VM then the VM must export a function named

Agent_OnAttach_L

.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

A

JVM TI

client is called an

agent

. It is developed in a native language.
A JVM TI agent is deployed in a platform specific manner but it is typically the
platform equivalent of a dynamic library. Alternatively, it may be statically linked into the VM.
This method causes the given agent library to be loaded into the target
VM (if not already loaded or if not statically linked into the VM).
It then causes the target VM to invoke the

Agent_OnAttach

function
or, for a statically linked agent named 'L', the

Agent_OnAttach_L

function
as specified in the

JVM Tools Interface

specification.
Note that the

Agent_OnAttach[_L]

function is invoked even if the agent library was loaded prior to invoking
this method.

The agent library provided is the name of the agent library. It is interpreted
in the target virtual machine in an implementation-dependent manner. Typically an
implementation will expand the library name into an operating system specific file
name. For example, on UNIX systems, the name

L

might be expanded to

libL.so

, and located using the search path specified by the

LD_LIBRARY_PATH

environment variable. If the agent named 'L' is
statically linked into the VM then the VM must export a function named

Agent_OnAttach_L

.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

The agent library provided is the name of the agent library. It is interpreted
in the target virtual machine in an implementation-dependent manner. Typically an
implementation will expand the library name into an operating system specific file
name. For example, on UNIX systems, the name

L

might be expanded to

libL.so

, and located using the search path specified by the

LD_LIBRARY_PATH

environment variable. If the agent named 'L' is
statically linked into the VM then the VM must export a function named

Agent_OnAttach_L

.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

loadAgentLibrary

```java
public void loadAgentLibrary​(
String
agentLibrary)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Loads an agent library.

This convenience method works as if by invoking:

loadAgentLibrary

(agentLibrary, null);

**Parameters:** agentLibrary

- The name of the agent library.
**Throws:** AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
**Throws:** AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agentLibrary

is

null

.

---

#### loadAgentLibrary

public void loadAgentLibrary​(

String

agentLibrary)
throws

AgentLoadException

,

AgentInitializationException

,

IOException

Loads an agent library.

This convenience method works as if by invoking:

loadAgentLibrary

(agentLibrary, null);

This convenience method works as if by invoking:

loadAgentLibrary

(agentLibrary, null);

loadAgentPath

```java
public abstract void loadAgentPath​(
String
agentPath,

String
options)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Load a native agent library by full pathname.

A

JVM TI

client is called an

agent

. It is developed in a native language.
A JVM TI agent is deployed in a platform specific manner but it is typically the
platform equivalent of a dynamic library. Alternatively, the native
library specified by the agentPath parameter may be statically
linked with the VM. The parsing of the agentPath parameter into
a statically linked library name is done in a platform
specific manner in the VM. For example, in UNIX, an agentPath parameter
of

/a/b/libL.so

would name a library 'L'.

See the JVM TI Specification for more details.

This method causes the given agent library to be loaded into the target
VM (if not already loaded or if not statically linked into the VM).
It then causes the target VM to invoke the

Agent_OnAttach

function or, for a statically linked agent named 'L', the

Agent_OnAttach_L

function as specified in the

JVM Tools Interface

specification.
Note that the

Agent_OnAttach[_L]

function is invoked even if the agent library was loaded prior to invoking
this method.

The agent library provided is the absolute path from which to load the
agent library. Unlike

loadAgentLibrary

, the library name
is not expanded in the target virtual machine.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

**Parameters:** agentPath

- The full path of the agent library.
**Parameters:** options

- The options to provide to the

Agent_OnAttach[_L]

function (can be

null

).
**Throws:** AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
**Throws:** AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agentPath

is

null

.
**See Also:** AgentInitializationException.returnValue()

---

#### loadAgentPath

public abstract void loadAgentPath​(

String

agentPath,

String

options)
throws

AgentLoadException

,

AgentInitializationException

,

IOException

Load a native agent library by full pathname.

A

JVM TI

client is called an

agent

. It is developed in a native language.
A JVM TI agent is deployed in a platform specific manner but it is typically the
platform equivalent of a dynamic library. Alternatively, the native
library specified by the agentPath parameter may be statically
linked with the VM. The parsing of the agentPath parameter into
a statically linked library name is done in a platform
specific manner in the VM. For example, in UNIX, an agentPath parameter
of

/a/b/libL.so

would name a library 'L'.

See the JVM TI Specification for more details.

This method causes the given agent library to be loaded into the target
VM (if not already loaded or if not statically linked into the VM).
It then causes the target VM to invoke the

Agent_OnAttach

function or, for a statically linked agent named 'L', the

Agent_OnAttach_L

function as specified in the

JVM Tools Interface

specification.
Note that the

Agent_OnAttach[_L]

function is invoked even if the agent library was loaded prior to invoking
this method.

The agent library provided is the absolute path from which to load the
agent library. Unlike

loadAgentLibrary

, the library name
is not expanded in the target virtual machine.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

A

JVM TI

client is called an

agent

. It is developed in a native language.
A JVM TI agent is deployed in a platform specific manner but it is typically the
platform equivalent of a dynamic library. Alternatively, the native
library specified by the agentPath parameter may be statically
linked with the VM. The parsing of the agentPath parameter into
a statically linked library name is done in a platform
specific manner in the VM. For example, in UNIX, an agentPath parameter
of

/a/b/libL.so

would name a library 'L'.

See the JVM TI Specification for more details.

This method causes the given agent library to be loaded into the target
VM (if not already loaded or if not statically linked into the VM).
It then causes the target VM to invoke the

Agent_OnAttach

function or, for a statically linked agent named 'L', the

Agent_OnAttach_L

function as specified in the

JVM Tools Interface

specification.
Note that the

Agent_OnAttach[_L]

function is invoked even if the agent library was loaded prior to invoking
this method.

The agent library provided is the absolute path from which to load the
agent library. Unlike

loadAgentLibrary

, the library name
is not expanded in the target virtual machine.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

The agent library provided is the absolute path from which to load the
agent library. Unlike

loadAgentLibrary

, the library name
is not expanded in the target virtual machine.

If the

Agent_OnAttach[_L]

function in the agent library returns
an error then an

AgentInitializationException

is
thrown. The return value from the

Agent_OnAttach[_L]

can then be
obtained by invoking the

returnValue

method on the exception.

loadAgentPath

```java
public void loadAgentPath​(
String
agentPath)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Load a native agent library by full pathname.

This convenience method works as if by invoking:

loadAgentPath

(agentLibrary, null);

**Parameters:** agentPath

- The full path to the agent library.
**Throws:** AgentLoadException

- If the agent library does not exist, the agent library is not
statically linked with the VM, or the agent library cannot be
loaded for another reason.
**Throws:** AgentInitializationException

- If the

Agent_OnAttach[_L]

function returns an error.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agentPath

is

null

.

---

#### loadAgentPath

public void loadAgentPath​(

String

agentPath)
throws

AgentLoadException

,

AgentInitializationException

,

IOException

Load a native agent library by full pathname.

This convenience method works as if by invoking:

loadAgentPath

(agentLibrary, null);

This convenience method works as if by invoking:

loadAgentPath

(agentLibrary, null);

loadAgent

```java
public abstract void loadAgent​(
String
agent,

String
options)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Loads an agent.

The agent provided to this method is a path name to a JAR file on the file
system of the target virtual machine. This path is passed to the target virtual
machine where it is interpreted. The target virtual machine attempts to start
the agent as specified by the

java.lang.instrument

specification.
That is, the specified JAR file is added to the system class path (of the target
virtual machine), and the

agentmain

method of the agent class, specified
by the

Agent-Class

attribute in the JAR manifest, is invoked. This
method completes when the

agentmain

method completes.

**Parameters:** agent

- Path to the JAR file containing the agent.
**Parameters:** options

- The options to provide to the agent's

agentmain

method (can be

null

).
**Throws:** AgentLoadException

- If the agent does not exist, or cannot be started in the manner
specified in the

java.lang.instrument

specification.
**Throws:** AgentInitializationException

- If the

agentmain

throws an exception
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agent

is

null

.

---

#### loadAgent

public abstract void loadAgent​(

String

agent,

String

options)
throws

AgentLoadException

,

AgentInitializationException

,

IOException

Loads an agent.

The agent provided to this method is a path name to a JAR file on the file
system of the target virtual machine. This path is passed to the target virtual
machine where it is interpreted. The target virtual machine attempts to start
the agent as specified by the

java.lang.instrument

specification.
That is, the specified JAR file is added to the system class path (of the target
virtual machine), and the

agentmain

method of the agent class, specified
by the

Agent-Class

attribute in the JAR manifest, is invoked. This
method completes when the

agentmain

method completes.

The agent provided to this method is a path name to a JAR file on the file
system of the target virtual machine. This path is passed to the target virtual
machine where it is interpreted. The target virtual machine attempts to start
the agent as specified by the

java.lang.instrument

specification.
That is, the specified JAR file is added to the system class path (of the target
virtual machine), and the

agentmain

method of the agent class, specified
by the

Agent-Class

attribute in the JAR manifest, is invoked. This
method completes when the

agentmain

method completes.

loadAgent

```java
public void loadAgent​(
String
agent)
throws
AgentLoadException
,

AgentInitializationException
,

IOException
```

Loads an agent.

This convenience method works as if by invoking:

loadAgent

(agent, null);

**Parameters:** agent

- Path to the JAR file containing the agent.
**Throws:** AgentLoadException

- If the agent does not exist, or cannot be started in the manner
specified in the

java.lang.instrument

specification.
**Throws:** AgentInitializationException

- If the

agentmain

throws an exception
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

agent

is

null

.

---

#### loadAgent

public void loadAgent​(

String

agent)
throws

AgentLoadException

,

AgentInitializationException

,

IOException

Loads an agent.

This convenience method works as if by invoking:

loadAgent

(agent, null);

This convenience method works as if by invoking:

loadAgent

(agent, null);

getSystemProperties

```java
public abstract
Properties
getSystemProperties()
throws
IOException
```

Returns the current system properties in the target virtual machine.

This method returns the system properties in the target virtual
machine. Properties whose key or value is not a

String

are
omitted. The method is approximately equivalent to the invocation of the
method

System.getProperties

in the target virtual machine except that properties with a key or
value that is not a

String

are not included.

This method is typically used to decide which agent to load into
the target virtual machine with

loadAgent

, or

loadAgentLibrary

. For example, the

java.home

or

user.dir

properties might be
use to create the path to the agent library or JAR file.

**Returns:** The system properties
**Throws:** AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
**Throws:** IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.
**See Also:** System.getProperties()

,

loadAgentLibrary(java.lang.String, java.lang.String)

,

loadAgent(java.lang.String, java.lang.String)

---

#### getSystemProperties

public abstract

Properties

getSystemProperties()
throws

IOException

Returns the current system properties in the target virtual machine.

This method returns the system properties in the target virtual
machine. Properties whose key or value is not a

String

are
omitted. The method is approximately equivalent to the invocation of the
method

System.getProperties

in the target virtual machine except that properties with a key or
value that is not a

String

are not included.

This method is typically used to decide which agent to load into
the target virtual machine with

loadAgent

, or

loadAgentLibrary

. For example, the

java.home

or

user.dir

properties might be
use to create the path to the agent library or JAR file.

This method returns the system properties in the target virtual
machine. Properties whose key or value is not a

String

are
omitted. The method is approximately equivalent to the invocation of the
method

System.getProperties

in the target virtual machine except that properties with a key or
value that is not a

String

are not included.

This method is typically used to decide which agent to load into
the target virtual machine with

loadAgent

, or

loadAgentLibrary

. For example, the

java.home

or

user.dir

properties might be
use to create the path to the agent library or JAR file.

This method is typically used to decide which agent to load into
the target virtual machine with

loadAgent

, or

loadAgentLibrary

. For example, the

java.home

or

user.dir

properties might be
use to create the path to the agent library or JAR file.

getAgentProperties

```java
public abstract
Properties
getAgentProperties()
throws
IOException
```

Returns the current

agent properties

in the target virtual
machine.

The target virtual machine can maintain a list of properties on
behalf of agents. The manner in which this is done, the names of the
properties, and the types of values that are allowed, is implementation
specific. Agent properties are typically used to store communication
end-points and other agent configuration details. For example, a debugger
agent might create an agent property for its transport address.

This method returns the agent properties whose key and value is a

String

. Properties whose key or value is not a

String

are omitted. If there are no agent properties maintained in the target
virtual machine then an empty property list is returned.

**Returns:** The agent properties
**Throws:** AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
**Throws:** IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.

---

#### getAgentProperties

public abstract

Properties

getAgentProperties()
throws

IOException

Returns the current

agent properties

in the target virtual
machine.

The target virtual machine can maintain a list of properties on
behalf of agents. The manner in which this is done, the names of the
properties, and the types of values that are allowed, is implementation
specific. Agent properties are typically used to store communication
end-points and other agent configuration details. For example, a debugger
agent might create an agent property for its transport address.

This method returns the agent properties whose key and value is a

String

. Properties whose key or value is not a

String

are omitted. If there are no agent properties maintained in the target
virtual machine then an empty property list is returned.

The target virtual machine can maintain a list of properties on
behalf of agents. The manner in which this is done, the names of the
properties, and the types of values that are allowed, is implementation
specific. Agent properties are typically used to store communication
end-points and other agent configuration details. For example, a debugger
agent might create an agent property for its transport address.

This method returns the agent properties whose key and value is a

String

. Properties whose key or value is not a

String

are omitted. If there are no agent properties maintained in the target
virtual machine then an empty property list is returned.

This method returns the agent properties whose key and value is a

String

. Properties whose key or value is not a

String

are omitted. If there are no agent properties maintained in the target
virtual machine then an empty property list is returned.

startManagementAgent

```java
public abstract void startManagementAgent​(
Properties
agentProperties)
throws
IOException
```

Starts the JMX management agent in the target virtual machine.

The configuration properties are the same as those specified on
the command line when starting the JMX management agent. In the same
way as on the command line, you need to specify at least the

com.sun.management.jmxremote.port

property.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

**Parameters:** agentProperties

- A Properties object containing the configuration properties
for the agent.
**Throws:** AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
**Throws:** IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.
**Throws:** IllegalArgumentException

- If keys or values in agentProperties are invalid.
**Throws:** NullPointerException

- If agentProperties is null.
**Since:** 1.8

---

#### startManagementAgent

public abstract void startManagementAgent​(

Properties

agentProperties)
throws

IOException

Starts the JMX management agent in the target virtual machine.

The configuration properties are the same as those specified on
the command line when starting the JMX management agent. In the same
way as on the command line, you need to specify at least the

com.sun.management.jmxremote.port

property.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

The configuration properties are the same as those specified on
the command line when starting the JMX management agent. In the same
way as on the command line, you need to specify at least the

com.sun.management.jmxremote.port

property.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

startLocalManagementAgent

```java
public abstract
String
startLocalManagementAgent()
throws
IOException
```

Starts the local JMX management agent in the target virtual machine.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

**Returns:** The String representation of the local connector's service address.
The value can be parsed by the

JMXServiceURL(String)

constructor.
**Throws:** AttachOperationFailedException

- If the target virtual machine is unable to complete the
attach operation. A more specific error message will be
given by

Throwable.getMessage()

.
**Throws:** IOException

- If an I/O error occurs, a communication error for example,
that cannot be identified as an error to indicate that the
operation failed in the target VM.
**Since:** 1.8

---

#### startLocalManagementAgent

public abstract

String

startLocalManagementAgent()
throws

IOException

Starts the local JMX management agent in the target virtual machine.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

See the online documentation for

Monitoring and Management Using JMX Technology

for further details.

hashCode

```java
public int hashCode()
```

Returns a hash-code value for this VirtualMachine. The hash
code is based upon the VirtualMachine's components, and satifies
the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** A hash-code value for this virtual machine
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash-code value for this VirtualMachine. The hash
code is based upon the VirtualMachine's components, and satifies
the general contract of the

Object.hashCode

method.

equals

```java
public boolean equals​(
Object
ob)
```

Tests this VirtualMachine for equality with another object.

If the given object is not a VirtualMachine then this
method returns

false

. For two VirtualMachines to
be considered equal requires that they both reference the same
provider, and their

identifiers

are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- The object to which this object is to be compared
**Returns:** true

if, and only if, the given object is
a VirtualMachine that is equal to this
VirtualMachine.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

ob)

Tests this VirtualMachine for equality with another object.

If the given object is not a VirtualMachine then this
method returns

false

. For two VirtualMachines to
be considered equal requires that they both reference the same
provider, and their

identifiers

are equal.

This method satisfies the general contract of the

Object.equals

method.

If the given object is not a VirtualMachine then this
method returns

false

. For two VirtualMachines to
be considered equal requires that they both reference the same
provider, and their

identifiers

are equal.

This method satisfies the general contract of the

Object.equals

method.

toString

```java
public
String
toString()
```

Returns the string representation of the

VirtualMachine

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns the string representation of the

VirtualMachine

.

---

