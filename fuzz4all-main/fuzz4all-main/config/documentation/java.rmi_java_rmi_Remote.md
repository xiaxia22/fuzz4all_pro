# Interface Remote

**Source:** `java.rmi\java\rmi\Remote.html`

### Class Description

```java
public interface
Remote
```

The

Remote

interface serves to identify interfaces whose
methods may be invoked from a non-local virtual machine. Any object that
is a remote object must directly or indirectly implement this interface.
Only those methods specified in a "remote interface", an interface that
extends

java.rmi.Remote

are available remotely.

Implementation classes can implement any number of remote interfaces and
can extend other remote implementation classes. RMI provides some
convenience classes that remote object implementations can extend which
facilitate remote object creation. These classes are

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

.

For complete details on RMI, see the

RMI Specification

which
describes the RMI API and system.

**All Known Subinterfaces:** ActivationInstantiator

,

ActivationMonitor

,

ActivationSystem

,

Activator

,

DGC

,

Registry

,

RMIConnection

,

RMIServer

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface Remote

**All Known Subinterfaces:** ActivationInstantiator

,

ActivationMonitor

,

ActivationSystem

,

Activator

,

DGC

,

Registry

,

RMIConnection

,

RMIServer

**All Known Implementing Classes:** Activatable

,

ActivationGroup

,

ActivationGroup_Stub

,

RemoteObject

,

RemoteObjectInvocationHandler

,

RemoteServer

,

RemoteStub

,

RMIConnectionImpl

,

RMIConnectionImpl_Stub

,

RMIIIOPServerImpl

,

RMIJRMPServerImpl

,

RMIServerImpl

,

RMIServerImpl_Stub

,

UnicastRemoteObject

```java
public interface
Remote
```

The

Remote

interface serves to identify interfaces whose
methods may be invoked from a non-local virtual machine. Any object that
is a remote object must directly or indirectly implement this interface.
Only those methods specified in a "remote interface", an interface that
extends

java.rmi.Remote

are available remotely.

Implementation classes can implement any number of remote interfaces and
can extend other remote implementation classes. RMI provides some
convenience classes that remote object implementations can extend which
facilitate remote object creation. These classes are

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

.

For complete details on RMI, see the

RMI Specification

which
describes the RMI API and system.

**Since:** 1.1
**See Also:** UnicastRemoteObject

,

Activatable

public interface

Remote

The

Remote

interface serves to identify interfaces whose
methods may be invoked from a non-local virtual machine. Any object that
is a remote object must directly or indirectly implement this interface.
Only those methods specified in a "remote interface", an interface that
extends

java.rmi.Remote

are available remotely.

Implementation classes can implement any number of remote interfaces and
can extend other remote implementation classes. RMI provides some
convenience classes that remote object implementations can extend which
facilitate remote object creation. These classes are

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

.

For complete details on RMI, see the

RMI Specification

which
describes the RMI API and system.

Implementation classes can implement any number of remote interfaces and
can extend other remote implementation classes. RMI provides some
convenience classes that remote object implementations can extend which
facilitate remote object creation. These classes are

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

.

For complete details on RMI, see the

RMI Specification

which
describes the RMI API and system.

For complete details on RMI, see the

RMI Specification

which
describes the RMI API and system.

---

