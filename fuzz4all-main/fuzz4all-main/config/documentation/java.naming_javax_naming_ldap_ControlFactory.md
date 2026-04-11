# Class ControlFactory

**Source:** `java.naming\javax\naming\ldap\ControlFactory.html`

### Class Description

```java
public abstract class
ControlFactory

extends
Object
```

This abstract class represents a factory for creating LDAPv3 controls.
LDAPv3 controls are defined in

RFC 2251

.

When a service provider receives a response control, it uses control
factories to return the specific/appropriate control class implementation.

**Since:** 1.3
**See Also:** Control

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ControlFactory()

Creates a new instance of a control factory.

---

### Method Details

#### public abstract
Control
getControlInstance​(
Control
ctl)
throws
NamingException

Creates a control using this control factory.

The factory is used by the service provider to return controls
that it reads from the LDAP protocol as specialized control classes.
Without this mechanism, the provider would be returning
controls that only contained data in BER encoded format.

Typically,

ctl

is a "basic" control containing
BER encoded data. The factory is used to create a specialized
control implementation, usually by decoding the BER encoded data,
that provides methods to access that data in a type-safe and friendly
manner.

For example, a factory might use the BER encoded data in
basic control and return an instance of a VirtualListReplyControl.

If this factory cannot create a control using the argument supplied,
it should return null.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other control factories
should be tried. This might happen, for example, if the BER data
in the control does not match what is expected of a control with
the given OID. Since this method throws

NamingException

,
any other internally generated exception that should be propagated
must be wrapped inside a

NamingException

.

**Parameters:**
- ctl

- A non-null control.

**Returns:**
- A possibly null Control.

**Throws:**
- NamingException

- If

ctl

contains invalid data that prevents it
from being used to create a control. A factory should only throw
an exception if it knows how to produce the control (identified by the OID)
but is unable to because of, for example invalid BER data.

---

#### public static
Control
getControlInstance​(
Control
ctl,

Context
ctx,

Hashtable
<?,​?> env)
throws
NamingException

Creates a control using known control factories.

The following rule is used to create the control:

- Use the control factories specified in
the

LdapContext.CONTROL_FACTORIES

property of the
environment, and of the provider resource file associated with

ctx

, in that order.
The value of this property is a colon-separated list of factory
class names that are tried in order, and the first one that succeeds
in creating the control is the one used.
If none of the factories can be loaded,
return

ctl

.
If an exception is encountered while creating the control, the
exception is passed up to the caller.

Note that a control factory must be public and must have a public
constructor that accepts no arguments.
In cases where the factory is in a named module then it must be in a
package which is exported by that module to the

java.naming

module.

**Parameters:**
- ctl

- The non-null control object containing the OID and BER data.
- ctx

- The possibly null context in which the control is being created.
If null, no such information is available.
- env

- The possibly null environment of the context. This is used
to find the value of the

LdapContext.CONTROL_FACTORIES

property.

**Returns:**
- A control object created using

ctl

; or

ctl

if a control object cannot be created using
the algorithm described above.

**Throws:**
- NamingException

- if a naming exception was encountered
while attempting to create the control object.
If one of the factories accessed throws an
exception, it is propagated up to the caller.
If an error was encountered while loading
and instantiating the factory and object classes, the exception
is wrapped inside a

NamingException

and then rethrown.

---

### Additional Sections

#### Class ControlFactory

java.lang.Object

- javax.naming.ldap.ControlFactory

javax.naming.ldap.ControlFactory

```java
public abstract class
ControlFactory

extends
Object
```

This abstract class represents a factory for creating LDAPv3 controls.
LDAPv3 controls are defined in

RFC 2251

.

When a service provider receives a response control, it uses control
factories to return the specific/appropriate control class implementation.

**Since:** 1.3
**See Also:** Control

public abstract class

ControlFactory

extends

Object

This abstract class represents a factory for creating LDAPv3 controls.
LDAPv3 controls are defined in

RFC 2251

.

When a service provider receives a response control, it uses control
factories to return the specific/appropriate control class implementation.

When a service provider receives a response control, it uses control
factories to return the specific/appropriate control class implementation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ControlFactory

()

Creates a new instance of a control factory.

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

abstract

Control

getControlInstance

​(

Control

ctl)

Creates a control using this control factory.

static

Control

getControlInstance

​(

Control

ctl,

Context

ctx,

Hashtable

<?,​?> env)

Creates a control using known control factories.

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

Modifier

Constructor

Description

protected

ControlFactory

()

Creates a new instance of a control factory.

---

#### Constructor Summary

Creates a new instance of a control factory.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Control

getControlInstance

​(

Control

ctl)

Creates a control using this control factory.

static

Control

getControlInstance

​(

Control

ctl,

Context

ctx,

Hashtable

<?,​?> env)

Creates a control using known control factories.

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

Creates a control using this control factory.

Creates a control using known control factories.

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

- ControlFactory

```java
protected ControlFactory()
```

Creates a new instance of a control factory.

============ METHOD DETAIL ==========

- Method Detail

- getControlInstance

```java
public abstract
Control
getControlInstance​(
Control
ctl)
throws
NamingException
```

Creates a control using this control factory.

The factory is used by the service provider to return controls
that it reads from the LDAP protocol as specialized control classes.
Without this mechanism, the provider would be returning
controls that only contained data in BER encoded format.

Typically,

ctl

is a "basic" control containing
BER encoded data. The factory is used to create a specialized
control implementation, usually by decoding the BER encoded data,
that provides methods to access that data in a type-safe and friendly
manner.

For example, a factory might use the BER encoded data in
basic control and return an instance of a VirtualListReplyControl.

If this factory cannot create a control using the argument supplied,
it should return null.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other control factories
should be tried. This might happen, for example, if the BER data
in the control does not match what is expected of a control with
the given OID. Since this method throws

NamingException

,
any other internally generated exception that should be propagated
must be wrapped inside a

NamingException

.

**Parameters:** ctl

- A non-null control.
**Returns:** A possibly null Control.
**Throws:** NamingException

- If

ctl

contains invalid data that prevents it
from being used to create a control. A factory should only throw
an exception if it knows how to produce the control (identified by the OID)
but is unable to because of, for example invalid BER data.

- getControlInstance

```java
public static
Control
getControlInstance​(
Control
ctl,

Context
ctx,

Hashtable
<?,​?> env)
throws
NamingException
```

Creates a control using known control factories.

The following rule is used to create the control:

- Use the control factories specified in
the

LdapContext.CONTROL_FACTORIES

property of the
environment, and of the provider resource file associated with

ctx

, in that order.
The value of this property is a colon-separated list of factory
class names that are tried in order, and the first one that succeeds
in creating the control is the one used.
If none of the factories can be loaded,
return

ctl

.
If an exception is encountered while creating the control, the
exception is passed up to the caller.

Note that a control factory must be public and must have a public
constructor that accepts no arguments.
In cases where the factory is in a named module then it must be in a
package which is exported by that module to the

java.naming

module.

**Parameters:** ctl

- The non-null control object containing the OID and BER data.
**Parameters:** ctx

- The possibly null context in which the control is being created.
If null, no such information is available.
**Parameters:** env

- The possibly null environment of the context. This is used
to find the value of the

LdapContext.CONTROL_FACTORIES

property.
**Returns:** A control object created using

ctl

; or

ctl

if a control object cannot be created using
the algorithm described above.
**Throws:** NamingException

- if a naming exception was encountered
while attempting to create the control object.
If one of the factories accessed throws an
exception, it is propagated up to the caller.
If an error was encountered while loading
and instantiating the factory and object classes, the exception
is wrapped inside a

NamingException

and then rethrown.

Constructor Detail

- ControlFactory

```java
protected ControlFactory()
```

Creates a new instance of a control factory.

---

#### Constructor Detail

ControlFactory

```java
protected ControlFactory()
```

Creates a new instance of a control factory.

---

#### ControlFactory

protected ControlFactory()

Creates a new instance of a control factory.

Method Detail

- getControlInstance

```java
public abstract
Control
getControlInstance​(
Control
ctl)
throws
NamingException
```

Creates a control using this control factory.

The factory is used by the service provider to return controls
that it reads from the LDAP protocol as specialized control classes.
Without this mechanism, the provider would be returning
controls that only contained data in BER encoded format.

Typically,

ctl

is a "basic" control containing
BER encoded data. The factory is used to create a specialized
control implementation, usually by decoding the BER encoded data,
that provides methods to access that data in a type-safe and friendly
manner.

For example, a factory might use the BER encoded data in
basic control and return an instance of a VirtualListReplyControl.

If this factory cannot create a control using the argument supplied,
it should return null.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other control factories
should be tried. This might happen, for example, if the BER data
in the control does not match what is expected of a control with
the given OID. Since this method throws

NamingException

,
any other internally generated exception that should be propagated
must be wrapped inside a

NamingException

.

**Parameters:** ctl

- A non-null control.
**Returns:** A possibly null Control.
**Throws:** NamingException

- If

ctl

contains invalid data that prevents it
from being used to create a control. A factory should only throw
an exception if it knows how to produce the control (identified by the OID)
but is unable to because of, for example invalid BER data.

- getControlInstance

```java
public static
Control
getControlInstance​(
Control
ctl,

Context
ctx,

Hashtable
<?,​?> env)
throws
NamingException
```

Creates a control using known control factories.

The following rule is used to create the control:

- Use the control factories specified in
the

LdapContext.CONTROL_FACTORIES

property of the
environment, and of the provider resource file associated with

ctx

, in that order.
The value of this property is a colon-separated list of factory
class names that are tried in order, and the first one that succeeds
in creating the control is the one used.
If none of the factories can be loaded,
return

ctl

.
If an exception is encountered while creating the control, the
exception is passed up to the caller.

Note that a control factory must be public and must have a public
constructor that accepts no arguments.
In cases where the factory is in a named module then it must be in a
package which is exported by that module to the

java.naming

module.

**Parameters:** ctl

- The non-null control object containing the OID and BER data.
**Parameters:** ctx

- The possibly null context in which the control is being created.
If null, no such information is available.
**Parameters:** env

- The possibly null environment of the context. This is used
to find the value of the

LdapContext.CONTROL_FACTORIES

property.
**Returns:** A control object created using

ctl

; or

ctl

if a control object cannot be created using
the algorithm described above.
**Throws:** NamingException

- if a naming exception was encountered
while attempting to create the control object.
If one of the factories accessed throws an
exception, it is propagated up to the caller.
If an error was encountered while loading
and instantiating the factory and object classes, the exception
is wrapped inside a

NamingException

and then rethrown.

---

#### Method Detail

getControlInstance

```java
public abstract
Control
getControlInstance​(
Control
ctl)
throws
NamingException
```

Creates a control using this control factory.

The factory is used by the service provider to return controls
that it reads from the LDAP protocol as specialized control classes.
Without this mechanism, the provider would be returning
controls that only contained data in BER encoded format.

Typically,

ctl

is a "basic" control containing
BER encoded data. The factory is used to create a specialized
control implementation, usually by decoding the BER encoded data,
that provides methods to access that data in a type-safe and friendly
manner.

For example, a factory might use the BER encoded data in
basic control and return an instance of a VirtualListReplyControl.

If this factory cannot create a control using the argument supplied,
it should return null.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other control factories
should be tried. This might happen, for example, if the BER data
in the control does not match what is expected of a control with
the given OID. Since this method throws

NamingException

,
any other internally generated exception that should be propagated
must be wrapped inside a

NamingException

.

**Parameters:** ctl

- A non-null control.
**Returns:** A possibly null Control.
**Throws:** NamingException

- If

ctl

contains invalid data that prevents it
from being used to create a control. A factory should only throw
an exception if it knows how to produce the control (identified by the OID)
but is unable to because of, for example invalid BER data.

---

#### getControlInstance

public abstract

Control

getControlInstance​(

Control

ctl)
throws

NamingException

Creates a control using this control factory.

The factory is used by the service provider to return controls
that it reads from the LDAP protocol as specialized control classes.
Without this mechanism, the provider would be returning
controls that only contained data in BER encoded format.

Typically,

ctl

is a "basic" control containing
BER encoded data. The factory is used to create a specialized
control implementation, usually by decoding the BER encoded data,
that provides methods to access that data in a type-safe and friendly
manner.

For example, a factory might use the BER encoded data in
basic control and return an instance of a VirtualListReplyControl.

If this factory cannot create a control using the argument supplied,
it should return null.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other control factories
should be tried. This might happen, for example, if the BER data
in the control does not match what is expected of a control with
the given OID. Since this method throws

NamingException

,
any other internally generated exception that should be propagated
must be wrapped inside a

NamingException

.

The factory is used by the service provider to return controls
that it reads from the LDAP protocol as specialized control classes.
Without this mechanism, the provider would be returning
controls that only contained data in BER encoded format.

Typically,

ctl

is a "basic" control containing
BER encoded data. The factory is used to create a specialized
control implementation, usually by decoding the BER encoded data,
that provides methods to access that data in a type-safe and friendly
manner.

For example, a factory might use the BER encoded data in
basic control and return an instance of a VirtualListReplyControl.

If this factory cannot create a control using the argument supplied,
it should return null.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other control factories
should be tried. This might happen, for example, if the BER data
in the control does not match what is expected of a control with
the given OID. Since this method throws

NamingException

,
any other internally generated exception that should be propagated
must be wrapped inside a

NamingException

.

Typically,

ctl

is a "basic" control containing
BER encoded data. The factory is used to create a specialized
control implementation, usually by decoding the BER encoded data,
that provides methods to access that data in a type-safe and friendly
manner.

For example, a factory might use the BER encoded data in
basic control and return an instance of a VirtualListReplyControl.

If this factory cannot create a control using the argument supplied,
it should return null.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other control factories
should be tried. This might happen, for example, if the BER data
in the control does not match what is expected of a control with
the given OID. Since this method throws

NamingException

,
any other internally generated exception that should be propagated
must be wrapped inside a

NamingException

.

For example, a factory might use the BER encoded data in
basic control and return an instance of a VirtualListReplyControl.

If this factory cannot create a control using the argument supplied,
it should return null.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other control factories
should be tried. This might happen, for example, if the BER data
in the control does not match what is expected of a control with
the given OID. Since this method throws

NamingException

,
any other internally generated exception that should be propagated
must be wrapped inside a

NamingException

.

If this factory cannot create a control using the argument supplied,
it should return null.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other control factories
should be tried. This might happen, for example, if the BER data
in the control does not match what is expected of a control with
the given OID. Since this method throws

NamingException

,
any other internally generated exception that should be propagated
must be wrapped inside a

NamingException

.

getControlInstance

```java
public static
Control
getControlInstance​(
Control
ctl,

Context
ctx,

Hashtable
<?,​?> env)
throws
NamingException
```

Creates a control using known control factories.

The following rule is used to create the control:

- Use the control factories specified in
the

LdapContext.CONTROL_FACTORIES

property of the
environment, and of the provider resource file associated with

ctx

, in that order.
The value of this property is a colon-separated list of factory
class names that are tried in order, and the first one that succeeds
in creating the control is the one used.
If none of the factories can be loaded,
return

ctl

.
If an exception is encountered while creating the control, the
exception is passed up to the caller.

Note that a control factory must be public and must have a public
constructor that accepts no arguments.
In cases where the factory is in a named module then it must be in a
package which is exported by that module to the

java.naming

module.

**Parameters:** ctl

- The non-null control object containing the OID and BER data.
**Parameters:** ctx

- The possibly null context in which the control is being created.
If null, no such information is available.
**Parameters:** env

- The possibly null environment of the context. This is used
to find the value of the

LdapContext.CONTROL_FACTORIES

property.
**Returns:** A control object created using

ctl

; or

ctl

if a control object cannot be created using
the algorithm described above.
**Throws:** NamingException

- if a naming exception was encountered
while attempting to create the control object.
If one of the factories accessed throws an
exception, it is propagated up to the caller.
If an error was encountered while loading
and instantiating the factory and object classes, the exception
is wrapped inside a

NamingException

and then rethrown.

---

#### getControlInstance

public static

Control

getControlInstance​(

Control

ctl,

Context

ctx,

Hashtable

<?,​?> env)
throws

NamingException

Creates a control using known control factories.

The following rule is used to create the control:

- Use the control factories specified in
the

LdapContext.CONTROL_FACTORIES

property of the
environment, and of the provider resource file associated with

ctx

, in that order.
The value of this property is a colon-separated list of factory
class names that are tried in order, and the first one that succeeds
in creating the control is the one used.
If none of the factories can be loaded,
return

ctl

.
If an exception is encountered while creating the control, the
exception is passed up to the caller.

Note that a control factory must be public and must have a public
constructor that accepts no arguments.
In cases where the factory is in a named module then it must be in a
package which is exported by that module to the

java.naming

module.

The following rule is used to create the control:

- Use the control factories specified in
the

LdapContext.CONTROL_FACTORIES

property of the
environment, and of the provider resource file associated with

ctx

, in that order.
The value of this property is a colon-separated list of factory
class names that are tried in order, and the first one that succeeds
in creating the control is the one used.
If none of the factories can be loaded,
return

ctl

.
If an exception is encountered while creating the control, the
exception is passed up to the caller.

Note that a control factory must be public and must have a public
constructor that accepts no arguments.
In cases where the factory is in a named module then it must be in a
package which is exported by that module to the

java.naming

module.

Use the control factories specified in
the

LdapContext.CONTROL_FACTORIES

property of the
environment, and of the provider resource file associated with

ctx

, in that order.
The value of this property is a colon-separated list of factory
class names that are tried in order, and the first one that succeeds
in creating the control is the one used.
If none of the factories can be loaded,
return

ctl

.
If an exception is encountered while creating the control, the
exception is passed up to the caller.

Note that a control factory must be public and must have a public
constructor that accepts no arguments.
In cases where the factory is in a named module then it must be in a
package which is exported by that module to the

java.naming

module.

---

