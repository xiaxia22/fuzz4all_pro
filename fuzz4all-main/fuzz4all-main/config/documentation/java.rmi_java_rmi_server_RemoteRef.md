# Interface RemoteRef

**Source:** `java.rmi\java\rmi\server\RemoteRef.html`

### Class Description

```java
public interface
RemoteRef

extends
Externalizable
```

RemoteRef

represents the handle for a remote object. A

RemoteStub

uses a remote reference to carry out a
remote method invocation to a remote object.

**All Superinterfaces:** Externalizable

,

Serializable

---

### Field Details

#### static final long serialVersionUID

indicate compatibility with JDK 1.1.x version of class.

**See Also:**
- Constant Field Values

---

#### static final
String
packagePrefix

Initialize the server package prefix: assumes that the
implementation of server ref classes (e.g., UnicastRef,
UnicastServerRef) are located in the package defined by the
prefix.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### Object
invoke​(
Remote
obj,

Method
method,

Object
[] params,
long opnum)
throws
Exception

Invoke a method. This form of delegating method invocation
to the reference allows the reference to take care of
setting up the connection to the remote host, marshaling
some representation for the method and parameters, then
communicating the method invocation to the remote host.
This method either returns the result of a method invocation
on the remote object which resides on the remote host or
throws a RemoteException if the call failed or an
application-level exception if the remote invocation throws
an exception.

**Parameters:**
- obj

- the object that contains the RemoteRef (e.g., the
RemoteStub for the object.
- method

- the method to be invoked
- params

- the parameter list
- opnum

- a hash that may be used to represent the method

**Returns:**
- result of remote method invocation

**Throws:**
- Exception

- if any exception occurs during remote method
invocation

**Since:**
- 1.2

---

#### @Deprecated

RemoteCall
newCall​(
RemoteObject
obj,

Operation
[] op,
int opnum,
long hash)
throws
RemoteException

Creates an appropriate call object for a new remote method
invocation on this object. Passing operation array and index,
allows the stubs generator to assign the operation indexes and
interpret them. The remote reference may need the operation to
encode in the call.

**Parameters:**
- obj

- remote stub through which to make call
- op

- array of stub operations
- opnum

- operation number
- hash

- stub/skeleton interface hash

**Returns:**
- call object representing remote call

**Throws:**
- RemoteException

- if failed to initiate new remote call

**See Also:**
- invoke(Remote,java.lang.reflect.Method,Object[],long)

**Since:**
- 1.1

---

#### @Deprecated

void invoke​(
RemoteCall
call)
throws
Exception

Executes the remote call.

Invoke will raise any "user" exceptions which
should pass through and not be caught by the stub. If any
exception is raised during the remote invocation, invoke should
take care of cleaning up the connection before raising the
"user" or remote exception.

**Parameters:**
- call

- object representing remote call

**Throws:**
- Exception

- if any exception occurs during remote method

**See Also:**
- invoke(Remote,java.lang.reflect.Method,Object[],long)

**Since:**
- 1.1

---

#### @Deprecated

void done​(
RemoteCall
call)
throws
RemoteException

Allows the remote reference to clean up (or reuse) the connection.
Done should only be called if the invoke returns successfully
(non-exceptionally) to the stub.

**Parameters:**
- call

- object representing remote call

**Throws:**
- RemoteException

- if remote error occurs during call cleanup

**See Also:**
- invoke(Remote,java.lang.reflect.Method,Object[],long)

**Since:**
- 1.1

---

#### String
getRefClass​(
ObjectOutput
out)

Returns the class name of the ref type to be serialized onto
the stream 'out'.

**Parameters:**
- out

- the output stream to which the reference will be serialized

**Returns:**
- the class name (without package qualification) of the reference
type

**Since:**
- 1.1

---

#### int remoteHashCode()

Returns a hashcode for a remote object. Two remote object stubs
that refer to the same remote object will have the same hash code
(in order to support remote objects as keys in hash tables).

**Returns:**
- remote object hashcode

**See Also:**
- Hashtable

**Since:**
- 1.1

---

#### boolean remoteEquals​(
RemoteRef
obj)

Compares two remote objects for equality.
Returns a boolean that indicates whether this remote object is
equivalent to the specified Object. This method is used when a
remote object is stored in a hashtable.

**Parameters:**
- obj

- the Object to compare with

**Returns:**
- true if these Objects are equal; false otherwise.

**See Also:**
- Hashtable

**Since:**
- 1.1

---

#### String
remoteToString()

Returns a String that represents the reference of this remote
object.

**Returns:**
- string representing remote object reference

**Since:**
- 1.1

---

### Additional Sections

#### Interface RemoteRef

**All Superinterfaces:** Externalizable

,

Serializable

**All Known Subinterfaces:** ServerRef

```java
public interface
RemoteRef

extends
Externalizable
```

RemoteRef

represents the handle for a remote object. A

RemoteStub

uses a remote reference to carry out a
remote method invocation to a remote object.

**Since:** 1.1
**See Also:** RemoteStub

public interface

RemoteRef

extends

Externalizable

RemoteRef

represents the handle for a remote object. A

RemoteStub

uses a remote reference to carry out a
remote method invocation to a remote object.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

packagePrefix

Initialize the server package prefix: assumes that the
implementation of server ref classes (e.g., UnicastRef,
UnicastServerRef) are located in the package defined by the
prefix.

static long

serialVersionUID

indicate compatibility with JDK 1.1.x version of class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

done

​(

RemoteCall

call)

Deprecated.

1.2 style stubs no longer use this method.

String

getRefClass

​(

ObjectOutput

out)

Returns the class name of the ref type to be serialized onto
the stream 'out'.

Object

invoke

​(

Remote

obj,

Method

method,

Object

[] params,
long opnum)

Invoke a method.

void

invoke

​(

RemoteCall

call)

Deprecated.

1.2 style stubs no longer use this method.

RemoteCall

newCall

​(

RemoteObject

obj,

Operation

[] op,
int opnum,
long hash)

Deprecated.

1.2 style stubs no longer use this method.

boolean

remoteEquals

​(

RemoteRef

obj)

Compares two remote objects for equality.

int

remoteHashCode

()

Returns a hashcode for a remote object.

String

remoteToString

()

Returns a String that represents the reference of this remote
object.

- Methods declared in interface java.io.

Externalizable

readExternal

,

writeExternal

Field Summary

Fields

Modifier and Type

Field

Description

static

String

packagePrefix

Initialize the server package prefix: assumes that the
implementation of server ref classes (e.g., UnicastRef,
UnicastServerRef) are located in the package defined by the
prefix.

static long

serialVersionUID

indicate compatibility with JDK 1.1.x version of class.

---

#### Field Summary

Initialize the server package prefix: assumes that the
implementation of server ref classes (e.g., UnicastRef,
UnicastServerRef) are located in the package defined by the
prefix.

indicate compatibility with JDK 1.1.x version of class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

done

​(

RemoteCall

call)

Deprecated.

1.2 style stubs no longer use this method.

String

getRefClass

​(

ObjectOutput

out)

Returns the class name of the ref type to be serialized onto
the stream 'out'.

Object

invoke

​(

Remote

obj,

Method

method,

Object

[] params,
long opnum)

Invoke a method.

void

invoke

​(

RemoteCall

call)

Deprecated.

1.2 style stubs no longer use this method.

RemoteCall

newCall

​(

RemoteObject

obj,

Operation

[] op,
int opnum,
long hash)

Deprecated.

1.2 style stubs no longer use this method.

boolean

remoteEquals

​(

RemoteRef

obj)

Compares two remote objects for equality.

int

remoteHashCode

()

Returns a hashcode for a remote object.

String

remoteToString

()

Returns a String that represents the reference of this remote
object.

- Methods declared in interface java.io.

Externalizable

readExternal

,

writeExternal

---

#### Method Summary

Deprecated.

1.2 style stubs no longer use this method.

Returns the class name of the ref type to be serialized onto
the stream 'out'.

Invoke a method.

Compares two remote objects for equality.

Returns a hashcode for a remote object.

Returns a String that represents the reference of this remote
object.

Methods declared in interface java.io.

Externalizable

readExternal

,

writeExternal

---

#### Methods declared in interface java.io. Externalizable

============ FIELD DETAIL ===========

- Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

indicate compatibility with JDK 1.1.x version of class.

**See Also:** Constant Field Values

- packagePrefix

```java
static final
String
packagePrefix
```

Initialize the server package prefix: assumes that the
implementation of server ref classes (e.g., UnicastRef,
UnicastServerRef) are located in the package defined by the
prefix.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- invoke

```java
Object
invoke​(
Remote
obj,

Method
method,

Object
[] params,
long opnum)
throws
Exception
```

Invoke a method. This form of delegating method invocation
to the reference allows the reference to take care of
setting up the connection to the remote host, marshaling
some representation for the method and parameters, then
communicating the method invocation to the remote host.
This method either returns the result of a method invocation
on the remote object which resides on the remote host or
throws a RemoteException if the call failed or an
application-level exception if the remote invocation throws
an exception.

**Parameters:** obj

- the object that contains the RemoteRef (e.g., the
RemoteStub for the object.
**Parameters:** method

- the method to be invoked
**Parameters:** params

- the parameter list
**Parameters:** opnum

- a hash that may be used to represent the method
**Returns:** result of remote method invocation
**Throws:** Exception

- if any exception occurs during remote method
invocation
**Since:** 1.2

- newCall

```java
@Deprecated

RemoteCall
newCall​(
RemoteObject
obj,

Operation
[] op,
int opnum,
long hash)
throws
RemoteException
```

Deprecated.

1.2 style stubs no longer use this method. Instead of
using a sequence of method calls on the stub's the remote reference
(

newCall

,

invoke

, and

done

), a
stub uses a single method,

invoke(Remote, Method, Object[],
int)

, on the remote reference to carry out parameter
marshalling, remote method executing and unmarshalling of the return
value.

Creates an appropriate call object for a new remote method
invocation on this object. Passing operation array and index,
allows the stubs generator to assign the operation indexes and
interpret them. The remote reference may need the operation to
encode in the call.

**Parameters:** obj

- remote stub through which to make call
**Parameters:** op

- array of stub operations
**Parameters:** opnum

- operation number
**Parameters:** hash

- stub/skeleton interface hash
**Returns:** call object representing remote call
**Throws:** RemoteException

- if failed to initiate new remote call
**Since:** 1.1
**See Also:** invoke(Remote,java.lang.reflect.Method,Object[],long)

- invoke

```java
@Deprecated

void invoke​(
RemoteCall
call)
throws
Exception
```

Deprecated.

1.2 style stubs no longer use this method. Instead of
using a sequence of method calls to the remote reference
(

newCall

,

invoke

, and

done

), a
stub uses a single method,

invoke(Remote, Method, Object[],
int)

, on the remote reference to carry out parameter
marshalling, remote method executing and unmarshalling of the return
value.

Executes the remote call.

Invoke will raise any "user" exceptions which
should pass through and not be caught by the stub. If any
exception is raised during the remote invocation, invoke should
take care of cleaning up the connection before raising the
"user" or remote exception.

**Parameters:** call

- object representing remote call
**Throws:** Exception

- if any exception occurs during remote method
**Since:** 1.1
**See Also:** invoke(Remote,java.lang.reflect.Method,Object[],long)

- done

```java
@Deprecated

void done​(
RemoteCall
call)
throws
RemoteException
```

Deprecated.

1.2 style stubs no longer use this method. Instead of
using a sequence of method calls to the remote reference
(

newCall

,

invoke

, and

done

), a
stub uses a single method,

invoke(Remote, Method, Object[],
int)

, on the remote reference to carry out parameter
marshalling, remote method executing and unmarshalling of the return
value.

Allows the remote reference to clean up (or reuse) the connection.
Done should only be called if the invoke returns successfully
(non-exceptionally) to the stub.

**Parameters:** call

- object representing remote call
**Throws:** RemoteException

- if remote error occurs during call cleanup
**Since:** 1.1
**See Also:** invoke(Remote,java.lang.reflect.Method,Object[],long)

- getRefClass

```java
String
getRefClass​(
ObjectOutput
out)
```

Returns the class name of the ref type to be serialized onto
the stream 'out'.

**Parameters:** out

- the output stream to which the reference will be serialized
**Returns:** the class name (without package qualification) of the reference
type
**Since:** 1.1

- remoteHashCode

```java
int remoteHashCode()
```

Returns a hashcode for a remote object. Two remote object stubs
that refer to the same remote object will have the same hash code
(in order to support remote objects as keys in hash tables).

**Returns:** remote object hashcode
**Since:** 1.1
**See Also:** Hashtable

- remoteEquals

```java
boolean remoteEquals​(
RemoteRef
obj)
```

Compares two remote objects for equality.
Returns a boolean that indicates whether this remote object is
equivalent to the specified Object. This method is used when a
remote object is stored in a hashtable.

**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**Since:** 1.1
**See Also:** Hashtable

- remoteToString

```java
String
remoteToString()
```

Returns a String that represents the reference of this remote
object.

**Returns:** string representing remote object reference
**Since:** 1.1

Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

indicate compatibility with JDK 1.1.x version of class.

**See Also:** Constant Field Values

- packagePrefix

```java
static final
String
packagePrefix
```

Initialize the server package prefix: assumes that the
implementation of server ref classes (e.g., UnicastRef,
UnicastServerRef) are located in the package defined by the
prefix.

**See Also:** Constant Field Values

---

#### Field Detail

serialVersionUID

```java
static final long serialVersionUID
```

indicate compatibility with JDK 1.1.x version of class.

**See Also:** Constant Field Values

---

#### serialVersionUID

static final long serialVersionUID

indicate compatibility with JDK 1.1.x version of class.

packagePrefix

```java
static final
String
packagePrefix
```

Initialize the server package prefix: assumes that the
implementation of server ref classes (e.g., UnicastRef,
UnicastServerRef) are located in the package defined by the
prefix.

**See Also:** Constant Field Values

---

#### packagePrefix

static final

String

packagePrefix

Initialize the server package prefix: assumes that the
implementation of server ref classes (e.g., UnicastRef,
UnicastServerRef) are located in the package defined by the
prefix.

Method Detail

- invoke

```java
Object
invoke​(
Remote
obj,

Method
method,

Object
[] params,
long opnum)
throws
Exception
```

Invoke a method. This form of delegating method invocation
to the reference allows the reference to take care of
setting up the connection to the remote host, marshaling
some representation for the method and parameters, then
communicating the method invocation to the remote host.
This method either returns the result of a method invocation
on the remote object which resides on the remote host or
throws a RemoteException if the call failed or an
application-level exception if the remote invocation throws
an exception.

**Parameters:** obj

- the object that contains the RemoteRef (e.g., the
RemoteStub for the object.
**Parameters:** method

- the method to be invoked
**Parameters:** params

- the parameter list
**Parameters:** opnum

- a hash that may be used to represent the method
**Returns:** result of remote method invocation
**Throws:** Exception

- if any exception occurs during remote method
invocation
**Since:** 1.2

- newCall

```java
@Deprecated

RemoteCall
newCall​(
RemoteObject
obj,

Operation
[] op,
int opnum,
long hash)
throws
RemoteException
```

Deprecated.

1.2 style stubs no longer use this method. Instead of
using a sequence of method calls on the stub's the remote reference
(

newCall

,

invoke

, and

done

), a
stub uses a single method,

invoke(Remote, Method, Object[],
int)

, on the remote reference to carry out parameter
marshalling, remote method executing and unmarshalling of the return
value.

Creates an appropriate call object for a new remote method
invocation on this object. Passing operation array and index,
allows the stubs generator to assign the operation indexes and
interpret them. The remote reference may need the operation to
encode in the call.

**Parameters:** obj

- remote stub through which to make call
**Parameters:** op

- array of stub operations
**Parameters:** opnum

- operation number
**Parameters:** hash

- stub/skeleton interface hash
**Returns:** call object representing remote call
**Throws:** RemoteException

- if failed to initiate new remote call
**Since:** 1.1
**See Also:** invoke(Remote,java.lang.reflect.Method,Object[],long)

- invoke

```java
@Deprecated

void invoke​(
RemoteCall
call)
throws
Exception
```

Deprecated.

1.2 style stubs no longer use this method. Instead of
using a sequence of method calls to the remote reference
(

newCall

,

invoke

, and

done

), a
stub uses a single method,

invoke(Remote, Method, Object[],
int)

, on the remote reference to carry out parameter
marshalling, remote method executing and unmarshalling of the return
value.

Executes the remote call.

Invoke will raise any "user" exceptions which
should pass through and not be caught by the stub. If any
exception is raised during the remote invocation, invoke should
take care of cleaning up the connection before raising the
"user" or remote exception.

**Parameters:** call

- object representing remote call
**Throws:** Exception

- if any exception occurs during remote method
**Since:** 1.1
**See Also:** invoke(Remote,java.lang.reflect.Method,Object[],long)

- done

```java
@Deprecated

void done​(
RemoteCall
call)
throws
RemoteException
```

Deprecated.

1.2 style stubs no longer use this method. Instead of
using a sequence of method calls to the remote reference
(

newCall

,

invoke

, and

done

), a
stub uses a single method,

invoke(Remote, Method, Object[],
int)

, on the remote reference to carry out parameter
marshalling, remote method executing and unmarshalling of the return
value.

Allows the remote reference to clean up (or reuse) the connection.
Done should only be called if the invoke returns successfully
(non-exceptionally) to the stub.

**Parameters:** call

- object representing remote call
**Throws:** RemoteException

- if remote error occurs during call cleanup
**Since:** 1.1
**See Also:** invoke(Remote,java.lang.reflect.Method,Object[],long)

- getRefClass

```java
String
getRefClass​(
ObjectOutput
out)
```

Returns the class name of the ref type to be serialized onto
the stream 'out'.

**Parameters:** out

- the output stream to which the reference will be serialized
**Returns:** the class name (without package qualification) of the reference
type
**Since:** 1.1

- remoteHashCode

```java
int remoteHashCode()
```

Returns a hashcode for a remote object. Two remote object stubs
that refer to the same remote object will have the same hash code
(in order to support remote objects as keys in hash tables).

**Returns:** remote object hashcode
**Since:** 1.1
**See Also:** Hashtable

- remoteEquals

```java
boolean remoteEquals​(
RemoteRef
obj)
```

Compares two remote objects for equality.
Returns a boolean that indicates whether this remote object is
equivalent to the specified Object. This method is used when a
remote object is stored in a hashtable.

**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**Since:** 1.1
**See Also:** Hashtable

- remoteToString

```java
String
remoteToString()
```

Returns a String that represents the reference of this remote
object.

**Returns:** string representing remote object reference
**Since:** 1.1

---

#### Method Detail

invoke

```java
Object
invoke​(
Remote
obj,

Method
method,

Object
[] params,
long opnum)
throws
Exception
```

Invoke a method. This form of delegating method invocation
to the reference allows the reference to take care of
setting up the connection to the remote host, marshaling
some representation for the method and parameters, then
communicating the method invocation to the remote host.
This method either returns the result of a method invocation
on the remote object which resides on the remote host or
throws a RemoteException if the call failed or an
application-level exception if the remote invocation throws
an exception.

**Parameters:** obj

- the object that contains the RemoteRef (e.g., the
RemoteStub for the object.
**Parameters:** method

- the method to be invoked
**Parameters:** params

- the parameter list
**Parameters:** opnum

- a hash that may be used to represent the method
**Returns:** result of remote method invocation
**Throws:** Exception

- if any exception occurs during remote method
invocation
**Since:** 1.2

---

#### invoke

Object

invoke​(

Remote

obj,

Method

method,

Object

[] params,
long opnum)
throws

Exception

Invoke a method. This form of delegating method invocation
to the reference allows the reference to take care of
setting up the connection to the remote host, marshaling
some representation for the method and parameters, then
communicating the method invocation to the remote host.
This method either returns the result of a method invocation
on the remote object which resides on the remote host or
throws a RemoteException if the call failed or an
application-level exception if the remote invocation throws
an exception.

newCall

```java
@Deprecated

RemoteCall
newCall​(
RemoteObject
obj,

Operation
[] op,
int opnum,
long hash)
throws
RemoteException
```

Deprecated.

1.2 style stubs no longer use this method. Instead of
using a sequence of method calls on the stub's the remote reference
(

newCall

,

invoke

, and

done

), a
stub uses a single method,

invoke(Remote, Method, Object[],
int)

, on the remote reference to carry out parameter
marshalling, remote method executing and unmarshalling of the return
value.

Creates an appropriate call object for a new remote method
invocation on this object. Passing operation array and index,
allows the stubs generator to assign the operation indexes and
interpret them. The remote reference may need the operation to
encode in the call.

**Parameters:** obj

- remote stub through which to make call
**Parameters:** op

- array of stub operations
**Parameters:** opnum

- operation number
**Parameters:** hash

- stub/skeleton interface hash
**Returns:** call object representing remote call
**Throws:** RemoteException

- if failed to initiate new remote call
**Since:** 1.1
**See Also:** invoke(Remote,java.lang.reflect.Method,Object[],long)

---

#### newCall

@Deprecated

RemoteCall

newCall​(

RemoteObject

obj,

Operation

[] op,
int opnum,
long hash)
throws

RemoteException

Creates an appropriate call object for a new remote method
invocation on this object. Passing operation array and index,
allows the stubs generator to assign the operation indexes and
interpret them. The remote reference may need the operation to
encode in the call.

invoke

```java
@Deprecated

void invoke​(
RemoteCall
call)
throws
Exception
```

Deprecated.

1.2 style stubs no longer use this method. Instead of
using a sequence of method calls to the remote reference
(

newCall

,

invoke

, and

done

), a
stub uses a single method,

invoke(Remote, Method, Object[],
int)

, on the remote reference to carry out parameter
marshalling, remote method executing and unmarshalling of the return
value.

Executes the remote call.

Invoke will raise any "user" exceptions which
should pass through and not be caught by the stub. If any
exception is raised during the remote invocation, invoke should
take care of cleaning up the connection before raising the
"user" or remote exception.

**Parameters:** call

- object representing remote call
**Throws:** Exception

- if any exception occurs during remote method
**Since:** 1.1
**See Also:** invoke(Remote,java.lang.reflect.Method,Object[],long)

---

#### invoke

@Deprecated

void invoke​(

RemoteCall

call)
throws

Exception

Executes the remote call.

Invoke will raise any "user" exceptions which
should pass through and not be caught by the stub. If any
exception is raised during the remote invocation, invoke should
take care of cleaning up the connection before raising the
"user" or remote exception.

done

```java
@Deprecated

void done​(
RemoteCall
call)
throws
RemoteException
```

Deprecated.

1.2 style stubs no longer use this method. Instead of
using a sequence of method calls to the remote reference
(

newCall

,

invoke

, and

done

), a
stub uses a single method,

invoke(Remote, Method, Object[],
int)

, on the remote reference to carry out parameter
marshalling, remote method executing and unmarshalling of the return
value.

Allows the remote reference to clean up (or reuse) the connection.
Done should only be called if the invoke returns successfully
(non-exceptionally) to the stub.

**Parameters:** call

- object representing remote call
**Throws:** RemoteException

- if remote error occurs during call cleanup
**Since:** 1.1
**See Also:** invoke(Remote,java.lang.reflect.Method,Object[],long)

---

#### done

@Deprecated

void done​(

RemoteCall

call)
throws

RemoteException

Allows the remote reference to clean up (or reuse) the connection.
Done should only be called if the invoke returns successfully
(non-exceptionally) to the stub.

getRefClass

```java
String
getRefClass​(
ObjectOutput
out)
```

Returns the class name of the ref type to be serialized onto
the stream 'out'.

**Parameters:** out

- the output stream to which the reference will be serialized
**Returns:** the class name (without package qualification) of the reference
type
**Since:** 1.1

---

#### getRefClass

String

getRefClass​(

ObjectOutput

out)

Returns the class name of the ref type to be serialized onto
the stream 'out'.

remoteHashCode

```java
int remoteHashCode()
```

Returns a hashcode for a remote object. Two remote object stubs
that refer to the same remote object will have the same hash code
(in order to support remote objects as keys in hash tables).

**Returns:** remote object hashcode
**Since:** 1.1
**See Also:** Hashtable

---

#### remoteHashCode

int remoteHashCode()

Returns a hashcode for a remote object. Two remote object stubs
that refer to the same remote object will have the same hash code
(in order to support remote objects as keys in hash tables).

remoteEquals

```java
boolean remoteEquals​(
RemoteRef
obj)
```

Compares two remote objects for equality.
Returns a boolean that indicates whether this remote object is
equivalent to the specified Object. This method is used when a
remote object is stored in a hashtable.

**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**Since:** 1.1
**See Also:** Hashtable

---

#### remoteEquals

boolean remoteEquals​(

RemoteRef

obj)

Compares two remote objects for equality.
Returns a boolean that indicates whether this remote object is
equivalent to the specified Object. This method is used when a
remote object is stored in a hashtable.

remoteToString

```java
String
remoteToString()
```

Returns a String that represents the reference of this remote
object.

**Returns:** string representing remote object reference
**Since:** 1.1

---

#### remoteToString

String

remoteToString()

Returns a String that represents the reference of this remote
object.

---

