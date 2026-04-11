# Class Util

**Source:** `jdk.jshell\jdk\jshell\execution\Util.html`

### Class Description

```java
public class
Util

extends
Object
```

Miscellaneous utility methods for setting-up implementations of

ExecutionControl

. Particularly implementations with remote
execution.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static void forwardExecutionControl​(
ExecutionControl
ec,

ObjectInput
in,

ObjectOutput
out)

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

**Parameters:**
- ec

- the direct instance of

ExecutionControl

to process commands
- in

- the command input
- out

- the command response output

---

#### public static void forwardExecutionControlAndIO​(
ExecutionControl
ec,

InputStream
inStream,

OutputStream
outStream,

Map
<
String
,​
Consumer
<
OutputStream
>> outputStreamMap,

Map
<
String
,​
Consumer
<
InputStream
>> inputStreamMap)
throws
IOException

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

**Parameters:**
- ec

- the direct instance of

ExecutionControl

to process commands
- inStream

- the stream from which to create the command input
- outStream

- the stream that will carry any specified auxiliary channels (like

System.out

and

System.err

), and the command response output.
- outputStreamMap

- a map between names of additional streams to carry and setters
for the stream. Names starting with '$' are reserved for internal use.
- inputStreamMap

- a map between names of additional streams to carry and setters
for the stream. Names starting with '$' are reserved for internal use.

**Throws:**
- IOException

- if there are errors using the passed streams

---

#### public static
ExecutionControl
remoteInputOutput​(
InputStream
input,

OutputStream
output,

Map
<
String
,​
OutputStream
> outputStreamMap,

Map
<
String
,​
InputStream
> inputStreamMap,

BiFunction
<
ObjectInput
,​
ObjectOutput
,​
ExecutionControl
> factory)
throws
IOException

Creates an ExecutionControl for given packetized input and output. The given InputStream
is de-packetized, and content forwarded to ObjectInput and given OutputStreams. The ObjectOutput
and values read from the given InputStream are packetized and sent to the given OutputStream.

**Parameters:**
- input

- the packetized input stream
- output

- the packetized output stream
- outputStreamMap

- a map between stream names and the output streams to forward.
Names starting with '$' are reserved for internal use.
- inputStreamMap

- a map between stream names and the input streams to forward.
Names starting with '$' are reserved for internal use.
- factory

- to create the ExecutionControl from ObjectInput and ObjectOutput.

**Returns:**
- the created ExecutionControl

**Throws:**
- IOException

- if setting up the streams raised an exception

---

#### public static void detectJdiExitEvent​(
VirtualMachine
vm,

Consumer
<
String
> unbiddenExitHandler)

Monitor the JDI event stream for

VMDeathEvent

and

VMDisconnectEvent

. If encountered, invokes

unbiddenExitHandler

.

**Parameters:**
- vm

- the virtual machine to check
- unbiddenExitHandler

- the handler, which will accept the exit
information

---

### Additional Sections

#### Class Util

java.lang.Object

- jdk.jshell.execution.Util

jdk.jshell.execution.Util

```java
public class
Util

extends
Object
```

Miscellaneous utility methods for setting-up implementations of

ExecutionControl

. Particularly implementations with remote
execution.

**Since:** 9

public class

Util

extends

Object

Miscellaneous utility methods for setting-up implementations of

ExecutionControl

. Particularly implementations with remote
execution.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static void

detectJdiExitEvent

​(

VirtualMachine

vm,

Consumer

<

String

> unbiddenExitHandler)

Monitor the JDI event stream for

VMDeathEvent

and

VMDisconnectEvent

.

static void

forwardExecutionControl

​(

ExecutionControl

ec,

ObjectInput

in,

ObjectOutput

out)

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

static void

forwardExecutionControlAndIO

​(

ExecutionControl

ec,

InputStream

inStream,

OutputStream

outStream,

Map

<

String

,​

Consumer

<

OutputStream

>> outputStreamMap,

Map

<

String

,​

Consumer

<

InputStream

>> inputStreamMap)

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

static

ExecutionControl

remoteInputOutput

​(

InputStream

input,

OutputStream

output,

Map

<

String

,​

OutputStream

> outputStreamMap,

Map

<

String

,​

InputStream

> inputStreamMap,

BiFunction

<

ObjectInput

,​

ObjectOutput

,​

ExecutionControl

> factory)

Creates an ExecutionControl for given packetized input and output.

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

Modifier and Type

Method

Description

static void

detectJdiExitEvent

​(

VirtualMachine

vm,

Consumer

<

String

> unbiddenExitHandler)

Monitor the JDI event stream for

VMDeathEvent

and

VMDisconnectEvent

.

static void

forwardExecutionControl

​(

ExecutionControl

ec,

ObjectInput

in,

ObjectOutput

out)

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

static void

forwardExecutionControlAndIO

​(

ExecutionControl

ec,

InputStream

inStream,

OutputStream

outStream,

Map

<

String

,​

Consumer

<

OutputStream

>> outputStreamMap,

Map

<

String

,​

Consumer

<

InputStream

>> inputStreamMap)

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

static

ExecutionControl

remoteInputOutput

​(

InputStream

input,

OutputStream

output,

Map

<

String

,​

OutputStream

> outputStreamMap,

Map

<

String

,​

InputStream

> inputStreamMap,

BiFunction

<

ObjectInput

,​

ObjectOutput

,​

ExecutionControl

> factory)

Creates an ExecutionControl for given packetized input and output.

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

Monitor the JDI event stream for

VMDeathEvent

and

VMDisconnectEvent

.

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

Creates an ExecutionControl for given packetized input and output.

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

- forwardExecutionControl

```java
public static void forwardExecutionControl​(
ExecutionControl
ec,

ObjectInput
in,

ObjectOutput
out)
```

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

**Parameters:** ec

- the direct instance of

ExecutionControl

to process commands
**Parameters:** in

- the command input
**Parameters:** out

- the command response output

- forwardExecutionControlAndIO

```java
public static void forwardExecutionControlAndIO​(
ExecutionControl
ec,

InputStream
inStream,

OutputStream
outStream,

Map
<
String
,​
Consumer
<
OutputStream
>> outputStreamMap,

Map
<
String
,​
Consumer
<
InputStream
>> inputStreamMap)
throws
IOException
```

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

**Parameters:** ec

- the direct instance of

ExecutionControl

to process commands
**Parameters:** inStream

- the stream from which to create the command input
**Parameters:** outStream

- the stream that will carry any specified auxiliary channels (like

System.out

and

System.err

), and the command response output.
**Parameters:** outputStreamMap

- a map between names of additional streams to carry and setters
for the stream. Names starting with '$' are reserved for internal use.
**Parameters:** inputStreamMap

- a map between names of additional streams to carry and setters
for the stream. Names starting with '$' are reserved for internal use.
**Throws:** IOException

- if there are errors using the passed streams

- remoteInputOutput

```java
public static
ExecutionControl
remoteInputOutput​(
InputStream
input,

OutputStream
output,

Map
<
String
,​
OutputStream
> outputStreamMap,

Map
<
String
,​
InputStream
> inputStreamMap,

BiFunction
<
ObjectInput
,​
ObjectOutput
,​
ExecutionControl
> factory)
throws
IOException
```

Creates an ExecutionControl for given packetized input and output. The given InputStream
is de-packetized, and content forwarded to ObjectInput and given OutputStreams. The ObjectOutput
and values read from the given InputStream are packetized and sent to the given OutputStream.

**Parameters:** input

- the packetized input stream
**Parameters:** output

- the packetized output stream
**Parameters:** outputStreamMap

- a map between stream names and the output streams to forward.
Names starting with '$' are reserved for internal use.
**Parameters:** inputStreamMap

- a map between stream names and the input streams to forward.
Names starting with '$' are reserved for internal use.
**Parameters:** factory

- to create the ExecutionControl from ObjectInput and ObjectOutput.
**Returns:** the created ExecutionControl
**Throws:** IOException

- if setting up the streams raised an exception

- detectJdiExitEvent

```java
public static void detectJdiExitEvent​(
VirtualMachine
vm,

Consumer
<
String
> unbiddenExitHandler)
```

Monitor the JDI event stream for

VMDeathEvent

and

VMDisconnectEvent

. If encountered, invokes

unbiddenExitHandler

.

**Parameters:** vm

- the virtual machine to check
**Parameters:** unbiddenExitHandler

- the handler, which will accept the exit
information

Method Detail

- forwardExecutionControl

```java
public static void forwardExecutionControl​(
ExecutionControl
ec,

ObjectInput
in,

ObjectOutput
out)
```

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

**Parameters:** ec

- the direct instance of

ExecutionControl

to process commands
**Parameters:** in

- the command input
**Parameters:** out

- the command response output

- forwardExecutionControlAndIO

```java
public static void forwardExecutionControlAndIO​(
ExecutionControl
ec,

InputStream
inStream,

OutputStream
outStream,

Map
<
String
,​
Consumer
<
OutputStream
>> outputStreamMap,

Map
<
String
,​
Consumer
<
InputStream
>> inputStreamMap)
throws
IOException
```

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

**Parameters:** ec

- the direct instance of

ExecutionControl

to process commands
**Parameters:** inStream

- the stream from which to create the command input
**Parameters:** outStream

- the stream that will carry any specified auxiliary channels (like

System.out

and

System.err

), and the command response output.
**Parameters:** outputStreamMap

- a map between names of additional streams to carry and setters
for the stream. Names starting with '$' are reserved for internal use.
**Parameters:** inputStreamMap

- a map between names of additional streams to carry and setters
for the stream. Names starting with '$' are reserved for internal use.
**Throws:** IOException

- if there are errors using the passed streams

- remoteInputOutput

```java
public static
ExecutionControl
remoteInputOutput​(
InputStream
input,

OutputStream
output,

Map
<
String
,​
OutputStream
> outputStreamMap,

Map
<
String
,​
InputStream
> inputStreamMap,

BiFunction
<
ObjectInput
,​
ObjectOutput
,​
ExecutionControl
> factory)
throws
IOException
```

Creates an ExecutionControl for given packetized input and output. The given InputStream
is de-packetized, and content forwarded to ObjectInput and given OutputStreams. The ObjectOutput
and values read from the given InputStream are packetized and sent to the given OutputStream.

**Parameters:** input

- the packetized input stream
**Parameters:** output

- the packetized output stream
**Parameters:** outputStreamMap

- a map between stream names and the output streams to forward.
Names starting with '$' are reserved for internal use.
**Parameters:** inputStreamMap

- a map between stream names and the input streams to forward.
Names starting with '$' are reserved for internal use.
**Parameters:** factory

- to create the ExecutionControl from ObjectInput and ObjectOutput.
**Returns:** the created ExecutionControl
**Throws:** IOException

- if setting up the streams raised an exception

- detectJdiExitEvent

```java
public static void detectJdiExitEvent​(
VirtualMachine
vm,

Consumer
<
String
> unbiddenExitHandler)
```

Monitor the JDI event stream for

VMDeathEvent

and

VMDisconnectEvent

. If encountered, invokes

unbiddenExitHandler

.

**Parameters:** vm

- the virtual machine to check
**Parameters:** unbiddenExitHandler

- the handler, which will accept the exit
information

---

#### Method Detail

forwardExecutionControl

```java
public static void forwardExecutionControl​(
ExecutionControl
ec,

ObjectInput
in,

ObjectOutput
out)
```

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

**Parameters:** ec

- the direct instance of

ExecutionControl

to process commands
**Parameters:** in

- the command input
**Parameters:** out

- the command response output

---

#### forwardExecutionControl

public static void forwardExecutionControl​(

ExecutionControl

ec,

ObjectInput

in,

ObjectOutput

out)

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

forwardExecutionControlAndIO

```java
public static void forwardExecutionControlAndIO​(
ExecutionControl
ec,

InputStream
inStream,

OutputStream
outStream,

Map
<
String
,​
Consumer
<
OutputStream
>> outputStreamMap,

Map
<
String
,​
Consumer
<
InputStream
>> inputStreamMap)
throws
IOException
```

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

**Parameters:** ec

- the direct instance of

ExecutionControl

to process commands
**Parameters:** inStream

- the stream from which to create the command input
**Parameters:** outStream

- the stream that will carry any specified auxiliary channels (like

System.out

and

System.err

), and the command response output.
**Parameters:** outputStreamMap

- a map between names of additional streams to carry and setters
for the stream. Names starting with '$' are reserved for internal use.
**Parameters:** inputStreamMap

- a map between names of additional streams to carry and setters
for the stream. Names starting with '$' are reserved for internal use.
**Throws:** IOException

- if there are errors using the passed streams

---

#### forwardExecutionControlAndIO

public static void forwardExecutionControlAndIO​(

ExecutionControl

ec,

InputStream

inStream,

OutputStream

outStream,

Map

<

String

,​

Consumer

<

OutputStream

>> outputStreamMap,

Map

<

String

,​

Consumer

<

InputStream

>> inputStreamMap)
throws

IOException

Forward commands from the input to the specified

ExecutionControl

instance, then responses back on the output.

remoteInputOutput

```java
public static
ExecutionControl
remoteInputOutput​(
InputStream
input,

OutputStream
output,

Map
<
String
,​
OutputStream
> outputStreamMap,

Map
<
String
,​
InputStream
> inputStreamMap,

BiFunction
<
ObjectInput
,​
ObjectOutput
,​
ExecutionControl
> factory)
throws
IOException
```

Creates an ExecutionControl for given packetized input and output. The given InputStream
is de-packetized, and content forwarded to ObjectInput and given OutputStreams. The ObjectOutput
and values read from the given InputStream are packetized and sent to the given OutputStream.

**Parameters:** input

- the packetized input stream
**Parameters:** output

- the packetized output stream
**Parameters:** outputStreamMap

- a map between stream names and the output streams to forward.
Names starting with '$' are reserved for internal use.
**Parameters:** inputStreamMap

- a map between stream names and the input streams to forward.
Names starting with '$' are reserved for internal use.
**Parameters:** factory

- to create the ExecutionControl from ObjectInput and ObjectOutput.
**Returns:** the created ExecutionControl
**Throws:** IOException

- if setting up the streams raised an exception

---

#### remoteInputOutput

public static

ExecutionControl

remoteInputOutput​(

InputStream

input,

OutputStream

output,

Map

<

String

,​

OutputStream

> outputStreamMap,

Map

<

String

,​

InputStream

> inputStreamMap,

BiFunction

<

ObjectInput

,​

ObjectOutput

,​

ExecutionControl

> factory)
throws

IOException

Creates an ExecutionControl for given packetized input and output. The given InputStream
is de-packetized, and content forwarded to ObjectInput and given OutputStreams. The ObjectOutput
and values read from the given InputStream are packetized and sent to the given OutputStream.

detectJdiExitEvent

```java
public static void detectJdiExitEvent​(
VirtualMachine
vm,

Consumer
<
String
> unbiddenExitHandler)
```

Monitor the JDI event stream for

VMDeathEvent

and

VMDisconnectEvent

. If encountered, invokes

unbiddenExitHandler

.

**Parameters:** vm

- the virtual machine to check
**Parameters:** unbiddenExitHandler

- the handler, which will accept the exit
information

---

#### detectJdiExitEvent

public static void detectJdiExitEvent​(

VirtualMachine

vm,

Consumer

<

String

> unbiddenExitHandler)

Monitor the JDI event stream for

VMDeathEvent

and

VMDisconnectEvent

. If encountered, invokes

unbiddenExitHandler

.

---

