# Class StandardMBean

**Source:** `java.management\javax\management\StandardMBean.html`

### Class Description

```java
public class
StandardMBean

extends
Object

implements
DynamicMBean
,
MBeanRegistration
```

An MBean whose management interface is determined by reflection
on a Java interface.

This class brings more flexibility to the notion of Management
Interface in the use of Standard MBeans. Straightforward use of
the patterns for Standard MBeans described in the JMX Specification
means that there is a fixed relationship between the implementation
class of an MBean and its management interface (i.e., if the
implementation class is Thing, the management interface must be
ThingMBean). This class makes it possible to keep the convenience
of specifying the management interface with a Java interface,
without requiring that there be any naming relationship between the
implementation and interface classes.

By making a DynamicMBean out of an MBean, this class makes
it possible to select any interface implemented by the MBean as its
management interface, provided that it complies with JMX patterns
(i.e., attributes defined by getter/setter etc...).

This class also provides hooks that make it possible to supply
custom descriptions and names for the

MBeanInfo

returned by
the DynamicMBean interface.

Using this class, an MBean can be created with any
implementation class name

Impl

and with a management
interface defined (as for current Standard MBeans) by any interface

Intf

, in one of two general ways:

- Using the public constructor

StandardMBean(impl,interface)

:

```java
MBeanServer mbs;
...
Impl impl = new Impl(...);
StandardMBean mbean = new StandardMBean(impl, Intf.class, false);
mbs.registerMBean(mbean, objectName);
```
- Subclassing StandardMBean:

```java
public class Impl extends StandardMBean implements Intf {
public Impl() {
super(Intf.class, false);
}
// implement methods of Intf
}

[...]

MBeanServer mbs;
....
Impl impl = new Impl();
mbs.registerMBean(impl, objectName);
```

In either case, the class

Impl

must implement the
interface

Intf

.

Standard MBeans based on the naming relationship between
implementation and interface classes are of course still
available.

This class may also be used to construct MXBeans. The usage
is exactly the same as for Standard MBeans except that in the
examples above, the

false

parameter to the constructor or

super(...)

invocation is instead

true

.

**All Implemented Interfaces:** DynamicMBean

,

MBeanRegistration

---

### Field Details

*No entries found.*

### Constructor Details

#### public StandardMBean​(T implementation,

Class
<T> mbeanInterface)
throws
NotCompliantMBeanException

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class.

**Parameters:**
- implementation

- The implementation of this MBean.
- mbeanInterface

- The Management Interface exported by this
MBean's implementation. If

null

, then this
object will use standard JMX design pattern to determine
the management interface associated with the given
implementation.

**Throws:**
- IllegalArgumentException

- if the given

implementation

is null.
- NotCompliantMBeanException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface.

**Type Parameters:**
- T

- Allows the compiler to check
that

implementation

does indeed implement the class
described by

mbeanInterface

. The compiler can only
check this if

mbeanInterface

is a class literal such
as

MyMBean.class

.

---

#### protected StandardMBean​(
Class
<?> mbeanInterface)
throws
NotCompliantMBeanException

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class.

Calls

this(this,mbeanInterface)

.
This constructor is reserved to subclasses.

**Parameters:**
- mbeanInterface

- The Management Interface exported by this
MBean.

**Throws:**
- NotCompliantMBeanException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface.

---

#### public StandardMBean​(T implementation,

Class
<T> mbeanInterface,
boolean isMXBean)

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class, and choosing whether the
resultant MBean is an MXBean. This constructor can be used
to make either Standard MBeans or MXBeans. Unlike the
constructor

StandardMBean(Object, Class)

, it
does not throw NotCompliantMBeanException.

**Parameters:**
- implementation

- The implementation of this MBean.
- mbeanInterface

- The Management Interface exported by this
MBean's implementation. If

null

, then this
object will use standard JMX design pattern to determine
the management interface associated with the given
implementation.
- isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.

**Throws:**
- IllegalArgumentException

- if the given

implementation

is null, or if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface.

**Since:**
- 1.6

**Type Parameters:**
- T

- Allows the compiler to check
that

implementation

does indeed implement the class
described by

mbeanInterface

. The compiler can only
check this if

mbeanInterface

is a class literal such
as

MyMBean.class

.

---

#### protected StandardMBean​(
Class
<?> mbeanInterface,
boolean isMXBean)

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class, and choosing whether the resulting
MBean is an MXBean. This constructor can be used
to make either Standard MBeans or MXBeans. Unlike the
constructor

StandardMBean(Object, Class)

, it
does not throw NotCompliantMBeanException.

Calls

this(this, mbeanInterface, isMXBean)

.
This constructor is reserved to subclasses.

**Parameters:**
- mbeanInterface

- The Management Interface exported by this
MBean.
- isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.

**Throws:**
- IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface.

**Since:**
- 1.6

---

### Method Details

#### public void setImplementation​(
Object
implementation)
throws
NotCompliantMBeanException

Replace the implementation object wrapped in this object.

**Parameters:**
- implementation

- The new implementation of this Standard MBean
(or MXBean). The

implementation

object must implement
the Standard MBean (or MXBean) interface that was supplied when this

StandardMBean

was constructed.

**Throws:**
- IllegalArgumentException

- if the given

implementation

is null.
- NotCompliantMBeanException

- if the given

implementation

does not implement the
Standard MBean (or MXBean) interface that was
supplied at construction.

**See Also:**
- getImplementation()

---

#### public
Object
getImplementation()

Get the implementation of this Standard MBean (or MXBean).

**Returns:**
- The implementation of this Standard MBean (or MXBean).

**See Also:**
- setImplementation(java.lang.Object)

---

#### public final
Class
<?> getMBeanInterface()

Get the Management Interface of this Standard MBean (or MXBean).

**Returns:**
- The management interface of this Standard MBean (or MXBean).

---

#### public
Class
<?> getImplementationClass()

Get the class of the implementation of this Standard MBean (or MXBean).

**Returns:**
- The class of the implementation of this Standard MBean (or MXBean).

---

#### public
MBeanInfo
getMBeanInfo()

Get the

MBeanInfo

for this MBean.

This method implements

DynamicMBean.getMBeanInfo()

.

This method first calls

getCachedMBeanInfo()

in order to
retrieve the cached MBeanInfo for this MBean, if any. If the
MBeanInfo returned by

getCachedMBeanInfo()

is not null,
then it is returned.

Otherwise, this method builds a default MBeanInfo for this MBean,
using the Management Interface specified for this MBean.

While building the MBeanInfo, this method calls the customization
hooks that make it possible for subclasses to supply their custom
descriptions, parameter names, etc...

Finally, it calls

cacheMBeanInfo()

in order to cache the new MBeanInfo.

**Specified by:**
- getMBeanInfo

in interface

DynamicMBean

**Returns:**
- The cached MBeanInfo for that MBean, if not null, or a
newly built MBeanInfo if none was cached.

---

#### protected
String
getClassName​(
MBeanInfo
info)

Customization hook:
Get the className that will be used in the MBeanInfo returned by
this MBean.

Subclasses may redefine this method in order to supply their
custom class name. The default implementation returns

info.getClassName()

.

**Parameters:**
- info

- The default MBeanInfo derived by reflection.

**Returns:**
- the class name for the new MBeanInfo.

---

#### protected
String
getDescription​(
MBeanInfo
info)

Customization hook:
Get the description that will be used in the MBeanInfo returned by
this MBean.

Subclasses may redefine this method in order to supply their
custom MBean description. The default implementation returns

info.getDescription()

.

**Parameters:**
- info

- The default MBeanInfo derived by reflection.

**Returns:**
- the description for the new MBeanInfo.

---

#### protected
String
getDescription​(
MBeanFeatureInfo
info)

Customization hook:
Get the description that will be used in the MBeanFeatureInfo
returned by this MBean.

Subclasses may redefine this method in order to supply
their custom description. The default implementation returns

info.getDescription()

.

This method is called by

getDescription(MBeanAttributeInfo)

,

getDescription(MBeanOperationInfo)

,

getDescription(MBeanConstructorInfo)

.

**Parameters:**
- info

- The default MBeanFeatureInfo derived by reflection.

**Returns:**
- the description for the given MBeanFeatureInfo.

---

#### protected
String
getDescription​(
MBeanAttributeInfo
info)

Customization hook:
Get the description that will be used in the MBeanAttributeInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

**Parameters:**
- info

- The default MBeanAttributeInfo derived by reflection.

**Returns:**
- the description for the given MBeanAttributeInfo.

---

#### protected
String
getDescription​(
MBeanConstructorInfo
info)

Customization hook:
Get the description that will be used in the MBeanConstructorInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description.
The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

**Parameters:**
- info

- The default MBeanConstructorInfo derived by reflection.

**Returns:**
- the description for the given MBeanConstructorInfo.

---

#### protected
String
getDescription​(
MBeanConstructorInfo
ctor,

MBeanParameterInfo
param,
int sequence)

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

param.getDescription()

.

**Parameters:**
- ctor

- The default MBeanConstructorInfo derived by reflection.
- param

- The default MBeanParameterInfo derived by reflection.
- sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).

**Returns:**
- the description for the given MBeanParameterInfo.

---

#### protected
String
getParameterName​(
MBeanConstructorInfo
ctor,

MBeanParameterInfo
param,
int sequence)

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom parameter name. The default implementation returns

param.getName()

.

**Parameters:**
- ctor

- The default MBeanConstructorInfo derived by reflection.
- param

- The default MBeanParameterInfo derived by reflection.
- sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).

**Returns:**
- the name for the given MBeanParameterInfo.

---

#### protected
String
getDescription​(
MBeanOperationInfo
info)

Customization hook:
Get the description that will be used in the MBeanOperationInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

**Parameters:**
- info

- The default MBeanOperationInfo derived by reflection.

**Returns:**
- the description for the given MBeanOperationInfo.

---

#### protected int getImpact​(
MBeanOperationInfo
info)

Customization hook:
Get the

impact

flag of the operation that will be used in
the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom impact flag. The default implementation returns

info.getImpact()

.

**Parameters:**
- info

- The default MBeanOperationInfo derived by reflection.

**Returns:**
- the impact flag for the given MBeanOperationInfo.

---

#### protected
String
getParameterName​(
MBeanOperationInfo
op,

MBeanParameterInfo
param,
int sequence)

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom parameter name. The default implementation returns

param.getName()

.

**Parameters:**
- op

- The default MBeanOperationInfo derived by reflection.
- param

- The default MBeanParameterInfo derived by reflection.
- sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).

**Returns:**
- the name to use for the given MBeanParameterInfo.

---

#### protected
String
getDescription​(
MBeanOperationInfo
op,

MBeanParameterInfo
param,
int sequence)

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

param.getDescription()

.

**Parameters:**
- op

- The default MBeanOperationInfo derived by reflection.
- param

- The default MBeanParameterInfo derived by reflection.
- sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).

**Returns:**
- the description for the given MBeanParameterInfo.

---

#### protected
MBeanConstructorInfo
[] getConstructors​(
MBeanConstructorInfo
[] ctors,

Object
impl)

Customization hook:
Get the MBeanConstructorInfo[] that will be used in the MBeanInfo
returned by this MBean.

By default, this method returns

null

if the wrapped
implementation is not

this

. Indeed, if the wrapped
implementation is not this object itself, it will not be possible
to recreate a wrapped implementation by calling the implementation
constructors through

MBeanServer.createMBean(...)

.

Otherwise, if the wrapped implementation is

this

,

ctors

is returned.

Subclasses may redefine this method in order to modify this
behavior, if needed.

**Parameters:**
- ctors

- The default MBeanConstructorInfo[] derived by reflection.
- impl

- The wrapped implementation. If

null

is
passed, the wrapped implementation is ignored and

ctors

is returned.

**Returns:**
- the MBeanConstructorInfo[] for the new MBeanInfo.

---

#### protected
MBeanInfo
getCachedMBeanInfo()

Customization hook:
Return the MBeanInfo cached for this object.

Subclasses may redefine this method in order to implement their
own caching policy. The default implementation stores one

MBeanInfo

object per instance.

**Returns:**
- The cached MBeanInfo, or null if no MBeanInfo is cached.

**See Also:**
- cacheMBeanInfo(MBeanInfo)

---

#### protected void cacheMBeanInfo​(
MBeanInfo
info)

Customization hook:
cache the MBeanInfo built for this object.

Subclasses may redefine this method in order to implement
their own caching policy. The default implementation stores

info

in this instance. A subclass can define
other policies, such as not saving

info

(so it is
reconstructed every time

getMBeanInfo()

is called) or
sharing a unique

MBeanInfo

object when several

StandardMBean

instances have equal

MBeanInfo

values.

**Parameters:**
- info

- the new

MBeanInfo

to cache. Any
previously cached value is discarded. This parameter may be
null, in which case there is no new cached value.

---

#### public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception

Allows the MBean to perform any operations it needs before
being registered in the MBean server. If the name of the MBean
is not specified, the MBean can provide a name for its
registration. If any exception is raised, the MBean will not be
registered in the MBean server.

The default implementation of this method returns the

name

parameter. It does nothing else for
Standard MBeans. For MXBeans, it records the

MBeanServer

and

ObjectName

parameters so they can be used to translate
inter-MXBean references.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.preRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

**Specified by:**
- preRegister

in interface

MBeanRegistration

**Parameters:**
- server

- The MBean server in which the MBean will be registered.
- name

- The object name of the MBean. This name is null if
the name parameter to one of the

createMBean

or

registerMBean

methods in the

MBeanServer

interface is null. In that case, this method must return a
non-null ObjectName for the new MBean.

**Returns:**
- The name under which the MBean is to be registered.
This value must not be null. If the

name

parameter is not null, it will usually but not necessarily be
the returned value.

**Throws:**
- IllegalArgumentException

- if this is an MXBean and

name

is null.
- InstanceAlreadyExistsException

- if this is an MXBean and
it has already been registered under another name (in this
MBean Server or another).
- Exception

- no other checked exceptions are thrown by
this method but

Exception

is declared so that subclasses
can override the method and throw their own exceptions.

**Since:**
- 1.6

---

#### public void postRegister​(
Boolean
registrationDone)

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

The default implementation of this method does nothing for
Standard MBeans. For MXBeans, it undoes any work done by

preRegister

if registration fails.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.postRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

**Specified by:**
- postRegister

in interface

MBeanRegistration

**Parameters:**
- registrationDone

- Indicates whether or not the MBean has
been successfully registered in the MBean server. The value
false means that the registration phase has failed.

**Since:**
- 1.6

---

#### public void preDeregister()
throws
Exception

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

The default implementation of this method does nothing.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.preDeregister(...)

.

**Specified by:**
- preDeregister

in interface

MBeanRegistration

**Throws:**
- Exception

- no checked exceptions are throw by this method
but

Exception

is declared so that subclasses can override
this method and throw their own exceptions.

**Since:**
- 1.6

---

#### public void postDeregister()

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

The default implementation of this method does nothing for
Standard MBeans. For MXBeans, it removes any information that
was recorded by the

preRegister

method.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.postRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

**Specified by:**
- postDeregister

in interface

MBeanRegistration

**Since:**
- 1.6

---

### Additional Sections

#### Class StandardMBean

java.lang.Object

- javax.management.StandardMBean

javax.management.StandardMBean

**All Implemented Interfaces:** DynamicMBean

,

MBeanRegistration

**Direct Known Subclasses:** StandardEmitterMBean

```java
public class
StandardMBean

extends
Object

implements
DynamicMBean
,
MBeanRegistration
```

An MBean whose management interface is determined by reflection
on a Java interface.

This class brings more flexibility to the notion of Management
Interface in the use of Standard MBeans. Straightforward use of
the patterns for Standard MBeans described in the JMX Specification
means that there is a fixed relationship between the implementation
class of an MBean and its management interface (i.e., if the
implementation class is Thing, the management interface must be
ThingMBean). This class makes it possible to keep the convenience
of specifying the management interface with a Java interface,
without requiring that there be any naming relationship between the
implementation and interface classes.

By making a DynamicMBean out of an MBean, this class makes
it possible to select any interface implemented by the MBean as its
management interface, provided that it complies with JMX patterns
(i.e., attributes defined by getter/setter etc...).

This class also provides hooks that make it possible to supply
custom descriptions and names for the

MBeanInfo

returned by
the DynamicMBean interface.

Using this class, an MBean can be created with any
implementation class name

Impl

and with a management
interface defined (as for current Standard MBeans) by any interface

Intf

, in one of two general ways:

- Using the public constructor

StandardMBean(impl,interface)

:

```java
MBeanServer mbs;
...
Impl impl = new Impl(...);
StandardMBean mbean = new StandardMBean(impl, Intf.class, false);
mbs.registerMBean(mbean, objectName);
```
- Subclassing StandardMBean:

```java
public class Impl extends StandardMBean implements Intf {
public Impl() {
super(Intf.class, false);
}
// implement methods of Intf
}

[...]

MBeanServer mbs;
....
Impl impl = new Impl();
mbs.registerMBean(impl, objectName);
```

In either case, the class

Impl

must implement the
interface

Intf

.

Standard MBeans based on the naming relationship between
implementation and interface classes are of course still
available.

This class may also be used to construct MXBeans. The usage
is exactly the same as for Standard MBeans except that in the
examples above, the

false

parameter to the constructor or

super(...)

invocation is instead

true

.

**Since:** 1.5

public class

StandardMBean

extends

Object

implements

DynamicMBean

,

MBeanRegistration

An MBean whose management interface is determined by reflection
on a Java interface.

This class brings more flexibility to the notion of Management
Interface in the use of Standard MBeans. Straightforward use of
the patterns for Standard MBeans described in the JMX Specification
means that there is a fixed relationship between the implementation
class of an MBean and its management interface (i.e., if the
implementation class is Thing, the management interface must be
ThingMBean). This class makes it possible to keep the convenience
of specifying the management interface with a Java interface,
without requiring that there be any naming relationship between the
implementation and interface classes.

By making a DynamicMBean out of an MBean, this class makes
it possible to select any interface implemented by the MBean as its
management interface, provided that it complies with JMX patterns
(i.e., attributes defined by getter/setter etc...).

This class also provides hooks that make it possible to supply
custom descriptions and names for the

MBeanInfo

returned by
the DynamicMBean interface.

Using this class, an MBean can be created with any
implementation class name

Impl

and with a management
interface defined (as for current Standard MBeans) by any interface

Intf

, in one of two general ways:

- Using the public constructor

StandardMBean(impl,interface)

:

```java
MBeanServer mbs;
...
Impl impl = new Impl(...);
StandardMBean mbean = new StandardMBean(impl, Intf.class, false);
mbs.registerMBean(mbean, objectName);
```
- Subclassing StandardMBean:

```java
public class Impl extends StandardMBean implements Intf {
public Impl() {
super(Intf.class, false);
}
// implement methods of Intf
}

[...]

MBeanServer mbs;
....
Impl impl = new Impl();
mbs.registerMBean(impl, objectName);
```

In either case, the class

Impl

must implement the
interface

Intf

.

Standard MBeans based on the naming relationship between
implementation and interface classes are of course still
available.

This class may also be used to construct MXBeans. The usage
is exactly the same as for Standard MBeans except that in the
examples above, the

false

parameter to the constructor or

super(...)

invocation is instead

true

.

An MBean whose management interface is determined by reflection
on a Java interface.

This class brings more flexibility to the notion of Management
Interface in the use of Standard MBeans. Straightforward use of
the patterns for Standard MBeans described in the JMX Specification
means that there is a fixed relationship between the implementation
class of an MBean and its management interface (i.e., if the
implementation class is Thing, the management interface must be
ThingMBean). This class makes it possible to keep the convenience
of specifying the management interface with a Java interface,
without requiring that there be any naming relationship between the
implementation and interface classes.

By making a DynamicMBean out of an MBean, this class makes
it possible to select any interface implemented by the MBean as its
management interface, provided that it complies with JMX patterns
(i.e., attributes defined by getter/setter etc...).

This class also provides hooks that make it possible to supply
custom descriptions and names for the

MBeanInfo

returned by
the DynamicMBean interface.

Using this class, an MBean can be created with any
implementation class name

Impl

and with a management
interface defined (as for current Standard MBeans) by any interface

Intf

, in one of two general ways:

Using the public constructor

StandardMBean(impl,interface)

:

```java
MBeanServer mbs;
...
Impl impl = new Impl(...);
StandardMBean mbean = new StandardMBean(impl, Intf.class, false);
mbs.registerMBean(mbean, objectName);
```

Subclassing StandardMBean:

```java
public class Impl extends StandardMBean implements Intf {
public Impl() {
super(Intf.class, false);
}
// implement methods of Intf
}

[...]

MBeanServer mbs;
....
Impl impl = new Impl();
mbs.registerMBean(impl, objectName);
```

MBeanServer mbs;
...
Impl impl = new Impl(...);
StandardMBean mbean = new StandardMBean(impl, Intf.class, false);
mbs.registerMBean(mbean, objectName);

public class Impl extends StandardMBean implements Intf {
public Impl() {
super(Intf.class, false);
}
// implement methods of Intf
}

[...]

MBeanServer mbs;
....
Impl impl = new Impl();
mbs.registerMBean(impl, objectName);

In either case, the class

Impl

must implement the
interface

Intf

.

Standard MBeans based on the naming relationship between
implementation and interface classes are of course still
available.

This class may also be used to construct MXBeans. The usage
is exactly the same as for Standard MBeans except that in the
examples above, the

false

parameter to the constructor or

super(...)

invocation is instead

true

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

StandardMBean

​(

Class

<?> mbeanInterface)

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class.

protected

StandardMBean

​(

Class

<?> mbeanInterface,
boolean isMXBean)

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class, and choosing whether the resulting
MBean is an MXBean.

StandardMBean

​(T implementation,

Class

<T> mbeanInterface)

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class.

StandardMBean

​(T implementation,

Class

<T> mbeanInterface,
boolean isMXBean)

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class, and choosing whether the
resultant MBean is an MXBean.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

cacheMBeanInfo

​(

MBeanInfo

info)

Customization hook:
cache the MBeanInfo built for this object.

protected

MBeanInfo

getCachedMBeanInfo

()

Customization hook:
Return the MBeanInfo cached for this object.

protected

String

getClassName

​(

MBeanInfo

info)

Customization hook:
Get the className that will be used in the MBeanInfo returned by
this MBean.

protected

MBeanConstructorInfo

[]

getConstructors

​(

MBeanConstructorInfo

[] ctors,

Object

impl)

Customization hook:
Get the MBeanConstructorInfo[] that will be used in the MBeanInfo
returned by this MBean.

protected

String

getDescription

​(

MBeanAttributeInfo

info)

Customization hook:
Get the description that will be used in the MBeanAttributeInfo
returned by this MBean.

protected

String

getDescription

​(

MBeanConstructorInfo

info)

Customization hook:
Get the description that will be used in the MBeanConstructorInfo
returned by this MBean.

protected

String

getDescription

​(

MBeanConstructorInfo

ctor,

MBeanParameterInfo

param,
int sequence)

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

protected

String

getDescription

​(

MBeanFeatureInfo

info)

Customization hook:
Get the description that will be used in the MBeanFeatureInfo
returned by this MBean.

protected

String

getDescription

​(

MBeanInfo

info)

Customization hook:
Get the description that will be used in the MBeanInfo returned by
this MBean.

protected

String

getDescription

​(

MBeanOperationInfo

info)

Customization hook:
Get the description that will be used in the MBeanOperationInfo
returned by this MBean.

protected

String

getDescription

​(

MBeanOperationInfo

op,

MBeanParameterInfo

param,
int sequence)

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

protected int

getImpact

​(

MBeanOperationInfo

info)

Customization hook:
Get the

impact

flag of the operation that will be used in
the MBeanOperationInfo returned by this MBean.

Object

getImplementation

()

Get the implementation of this Standard MBean (or MXBean).

Class

<?>

getImplementationClass

()

Get the class of the implementation of this Standard MBean (or MXBean).

MBeanInfo

getMBeanInfo

()

Get the

MBeanInfo

for this MBean.

Class

<?>

getMBeanInterface

()

Get the Management Interface of this Standard MBean (or MXBean).

protected

String

getParameterName

​(

MBeanConstructorInfo

ctor,

MBeanParameterInfo

param,
int sequence)

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

protected

String

getParameterName

​(

MBeanOperationInfo

op,

MBeanParameterInfo

param,
int sequence)

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

void

postDeregister

()

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

void

postRegister

​(

Boolean

registrationDone)

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

void

preDeregister

()

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

ObjectName

preRegister

​(

MBeanServer

server,

ObjectName

name)

Allows the MBean to perform any operations it needs before
being registered in the MBean server.

void

setImplementation

​(

Object

implementation)

Replace the implementation object wrapped in this object.

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

- Methods declared in interface javax.management.

DynamicMBean

getAttribute

,

getAttributes

,

invoke

,

setAttribute

,

setAttributes

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

StandardMBean

​(

Class

<?> mbeanInterface)

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class.

protected

StandardMBean

​(

Class

<?> mbeanInterface,
boolean isMXBean)

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class, and choosing whether the resulting
MBean is an MXBean.

StandardMBean

​(T implementation,

Class

<T> mbeanInterface)

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class.

StandardMBean

​(T implementation,

Class

<T> mbeanInterface,
boolean isMXBean)

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class, and choosing whether the
resultant MBean is an MXBean.

---

#### Constructor Summary

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class.

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class, and choosing whether the resulting
MBean is an MXBean.

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class.

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class, and choosing whether the
resultant MBean is an MXBean.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

cacheMBeanInfo

​(

MBeanInfo

info)

Customization hook:
cache the MBeanInfo built for this object.

protected

MBeanInfo

getCachedMBeanInfo

()

Customization hook:
Return the MBeanInfo cached for this object.

protected

String

getClassName

​(

MBeanInfo

info)

Customization hook:
Get the className that will be used in the MBeanInfo returned by
this MBean.

protected

MBeanConstructorInfo

[]

getConstructors

​(

MBeanConstructorInfo

[] ctors,

Object

impl)

Customization hook:
Get the MBeanConstructorInfo[] that will be used in the MBeanInfo
returned by this MBean.

protected

String

getDescription

​(

MBeanAttributeInfo

info)

Customization hook:
Get the description that will be used in the MBeanAttributeInfo
returned by this MBean.

protected

String

getDescription

​(

MBeanConstructorInfo

info)

Customization hook:
Get the description that will be used in the MBeanConstructorInfo
returned by this MBean.

protected

String

getDescription

​(

MBeanConstructorInfo

ctor,

MBeanParameterInfo

param,
int sequence)

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

protected

String

getDescription

​(

MBeanFeatureInfo

info)

Customization hook:
Get the description that will be used in the MBeanFeatureInfo
returned by this MBean.

protected

String

getDescription

​(

MBeanInfo

info)

Customization hook:
Get the description that will be used in the MBeanInfo returned by
this MBean.

protected

String

getDescription

​(

MBeanOperationInfo

info)

Customization hook:
Get the description that will be used in the MBeanOperationInfo
returned by this MBean.

protected

String

getDescription

​(

MBeanOperationInfo

op,

MBeanParameterInfo

param,
int sequence)

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

protected int

getImpact

​(

MBeanOperationInfo

info)

Customization hook:
Get the

impact

flag of the operation that will be used in
the MBeanOperationInfo returned by this MBean.

Object

getImplementation

()

Get the implementation of this Standard MBean (or MXBean).

Class

<?>

getImplementationClass

()

Get the class of the implementation of this Standard MBean (or MXBean).

MBeanInfo

getMBeanInfo

()

Get the

MBeanInfo

for this MBean.

Class

<?>

getMBeanInterface

()

Get the Management Interface of this Standard MBean (or MXBean).

protected

String

getParameterName

​(

MBeanConstructorInfo

ctor,

MBeanParameterInfo

param,
int sequence)

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

protected

String

getParameterName

​(

MBeanOperationInfo

op,

MBeanParameterInfo

param,
int sequence)

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

void

postDeregister

()

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

void

postRegister

​(

Boolean

registrationDone)

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

void

preDeregister

()

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

ObjectName

preRegister

​(

MBeanServer

server,

ObjectName

name)

Allows the MBean to perform any operations it needs before
being registered in the MBean server.

void

setImplementation

​(

Object

implementation)

Replace the implementation object wrapped in this object.

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

- Methods declared in interface javax.management.

DynamicMBean

getAttribute

,

getAttributes

,

invoke

,

setAttribute

,

setAttributes

---

#### Method Summary

Customization hook:
cache the MBeanInfo built for this object.

Customization hook:
Return the MBeanInfo cached for this object.

Customization hook:
Get the className that will be used in the MBeanInfo returned by
this MBean.

Customization hook:
Get the MBeanConstructorInfo[] that will be used in the MBeanInfo
returned by this MBean.

Customization hook:
Get the description that will be used in the MBeanAttributeInfo
returned by this MBean.

Customization hook:
Get the description that will be used in the MBeanConstructorInfo
returned by this MBean.

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

Customization hook:
Get the description that will be used in the MBeanFeatureInfo
returned by this MBean.

Customization hook:
Get the description that will be used in the MBeanInfo returned by
this MBean.

Customization hook:
Get the description that will be used in the MBeanOperationInfo
returned by this MBean.

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

Customization hook:
Get the

impact

flag of the operation that will be used in
the MBeanOperationInfo returned by this MBean.

Get the implementation of this Standard MBean (or MXBean).

Get the class of the implementation of this Standard MBean (or MXBean).

Get the

MBeanInfo

for this MBean.

Get the Management Interface of this Standard MBean (or MXBean).

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

Allows the MBean to perform any operations it needs before
being registered in the MBean server.

Replace the implementation object wrapped in this object.

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

Methods declared in interface javax.management.

DynamicMBean

getAttribute

,

getAttributes

,

invoke

,

setAttribute

,

setAttributes

---

#### Methods declared in interface javax.management. DynamicMBean

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StandardMBean

```java
public StandardMBean​(T implementation,

Class
<T> mbeanInterface)
throws
NotCompliantMBeanException
```

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class.

**Type Parameters:** T

- Allows the compiler to check
that

implementation

does indeed implement the class
described by

mbeanInterface

. The compiler can only
check this if

mbeanInterface

is a class literal such
as

MyMBean.class

.
**Parameters:** implementation

- The implementation of this MBean.
**Parameters:** mbeanInterface

- The Management Interface exported by this
MBean's implementation. If

null

, then this
object will use standard JMX design pattern to determine
the management interface associated with the given
implementation.
**Throws:** IllegalArgumentException

- if the given

implementation

is null.
**Throws:** NotCompliantMBeanException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface.

- StandardMBean

```java
protected StandardMBean​(
Class
<?> mbeanInterface)
throws
NotCompliantMBeanException
```

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class.

Calls

this(this,mbeanInterface)

.
This constructor is reserved to subclasses.

**Parameters:** mbeanInterface

- The Management Interface exported by this
MBean.
**Throws:** NotCompliantMBeanException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface.

- StandardMBean

```java
public StandardMBean​(T implementation,

Class
<T> mbeanInterface,
boolean isMXBean)
```

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class, and choosing whether the
resultant MBean is an MXBean. This constructor can be used
to make either Standard MBeans or MXBeans. Unlike the
constructor

StandardMBean(Object, Class)

, it
does not throw NotCompliantMBeanException.

**Type Parameters:** T

- Allows the compiler to check
that

implementation

does indeed implement the class
described by

mbeanInterface

. The compiler can only
check this if

mbeanInterface

is a class literal such
as

MyMBean.class

.
**Parameters:** implementation

- The implementation of this MBean.
**Parameters:** mbeanInterface

- The Management Interface exported by this
MBean's implementation. If

null

, then this
object will use standard JMX design pattern to determine
the management interface associated with the given
implementation.
**Parameters:** isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
**Throws:** IllegalArgumentException

- if the given

implementation

is null, or if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface.
**Since:** 1.6

- StandardMBean

```java
protected StandardMBean​(
Class
<?> mbeanInterface,
boolean isMXBean)
```

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class, and choosing whether the resulting
MBean is an MXBean. This constructor can be used
to make either Standard MBeans or MXBeans. Unlike the
constructor

StandardMBean(Object, Class)

, it
does not throw NotCompliantMBeanException.

Calls

this(this, mbeanInterface, isMXBean)

.
This constructor is reserved to subclasses.

**Parameters:** mbeanInterface

- The Management Interface exported by this
MBean.
**Parameters:** isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface.
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- setImplementation

```java
public void setImplementation​(
Object
implementation)
throws
NotCompliantMBeanException
```

Replace the implementation object wrapped in this object.

**Parameters:** implementation

- The new implementation of this Standard MBean
(or MXBean). The

implementation

object must implement
the Standard MBean (or MXBean) interface that was supplied when this

StandardMBean

was constructed.
**Throws:** IllegalArgumentException

- if the given

implementation

is null.
**Throws:** NotCompliantMBeanException

- if the given

implementation

does not implement the
Standard MBean (or MXBean) interface that was
supplied at construction.
**See Also:** getImplementation()

- getImplementation

```java
public
Object
getImplementation()
```

Get the implementation of this Standard MBean (or MXBean).

**Returns:** The implementation of this Standard MBean (or MXBean).
**See Also:** setImplementation(java.lang.Object)

- getMBeanInterface

```java
public final
Class
<?> getMBeanInterface()
```

Get the Management Interface of this Standard MBean (or MXBean).

**Returns:** The management interface of this Standard MBean (or MXBean).

- getImplementationClass

```java
public
Class
<?> getImplementationClass()
```

Get the class of the implementation of this Standard MBean (or MXBean).

**Returns:** The class of the implementation of this Standard MBean (or MXBean).

- getMBeanInfo

```java
public
MBeanInfo
getMBeanInfo()
```

Get the

MBeanInfo

for this MBean.

This method implements

DynamicMBean.getMBeanInfo()

.

This method first calls

getCachedMBeanInfo()

in order to
retrieve the cached MBeanInfo for this MBean, if any. If the
MBeanInfo returned by

getCachedMBeanInfo()

is not null,
then it is returned.

Otherwise, this method builds a default MBeanInfo for this MBean,
using the Management Interface specified for this MBean.

While building the MBeanInfo, this method calls the customization
hooks that make it possible for subclasses to supply their custom
descriptions, parameter names, etc...

Finally, it calls

cacheMBeanInfo()

in order to cache the new MBeanInfo.

**Specified by:** getMBeanInfo

in interface

DynamicMBean
**Returns:** The cached MBeanInfo for that MBean, if not null, or a
newly built MBeanInfo if none was cached.

- getClassName

```java
protected
String
getClassName​(
MBeanInfo
info)
```

Customization hook:
Get the className that will be used in the MBeanInfo returned by
this MBean.

Subclasses may redefine this method in order to supply their
custom class name. The default implementation returns

info.getClassName()

.

**Parameters:** info

- The default MBeanInfo derived by reflection.
**Returns:** the class name for the new MBeanInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanInfo returned by
this MBean.

Subclasses may redefine this method in order to supply their
custom MBean description. The default implementation returns

info.getDescription()

.

**Parameters:** info

- The default MBeanInfo derived by reflection.
**Returns:** the description for the new MBeanInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanFeatureInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanFeatureInfo
returned by this MBean.

Subclasses may redefine this method in order to supply
their custom description. The default implementation returns

info.getDescription()

.

This method is called by

getDescription(MBeanAttributeInfo)

,

getDescription(MBeanOperationInfo)

,

getDescription(MBeanConstructorInfo)

.

**Parameters:** info

- The default MBeanFeatureInfo derived by reflection.
**Returns:** the description for the given MBeanFeatureInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanAttributeInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanAttributeInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

**Parameters:** info

- The default MBeanAttributeInfo derived by reflection.
**Returns:** the description for the given MBeanAttributeInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanConstructorInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanConstructorInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description.
The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

**Parameters:** info

- The default MBeanConstructorInfo derived by reflection.
**Returns:** the description for the given MBeanConstructorInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanConstructorInfo
ctor,

MBeanParameterInfo
param,
int sequence)
```

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

param.getDescription()

.

**Parameters:** ctor

- The default MBeanConstructorInfo derived by reflection.
**Parameters:** param

- The default MBeanParameterInfo derived by reflection.
**Parameters:** sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).
**Returns:** the description for the given MBeanParameterInfo.

- getParameterName

```java
protected
String
getParameterName​(
MBeanConstructorInfo
ctor,

MBeanParameterInfo
param,
int sequence)
```

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom parameter name. The default implementation returns

param.getName()

.

**Parameters:** ctor

- The default MBeanConstructorInfo derived by reflection.
**Parameters:** param

- The default MBeanParameterInfo derived by reflection.
**Parameters:** sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).
**Returns:** the name for the given MBeanParameterInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanOperationInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanOperationInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

**Parameters:** info

- The default MBeanOperationInfo derived by reflection.
**Returns:** the description for the given MBeanOperationInfo.

- getImpact

```java
protected int getImpact​(
MBeanOperationInfo
info)
```

Customization hook:
Get the

impact

flag of the operation that will be used in
the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom impact flag. The default implementation returns

info.getImpact()

.

**Parameters:** info

- The default MBeanOperationInfo derived by reflection.
**Returns:** the impact flag for the given MBeanOperationInfo.

- getParameterName

```java
protected
String
getParameterName​(
MBeanOperationInfo
op,

MBeanParameterInfo
param,
int sequence)
```

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom parameter name. The default implementation returns

param.getName()

.

**Parameters:** op

- The default MBeanOperationInfo derived by reflection.
**Parameters:** param

- The default MBeanParameterInfo derived by reflection.
**Parameters:** sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).
**Returns:** the name to use for the given MBeanParameterInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanOperationInfo
op,

MBeanParameterInfo
param,
int sequence)
```

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

param.getDescription()

.

**Parameters:** op

- The default MBeanOperationInfo derived by reflection.
**Parameters:** param

- The default MBeanParameterInfo derived by reflection.
**Parameters:** sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).
**Returns:** the description for the given MBeanParameterInfo.

- getConstructors

```java
protected
MBeanConstructorInfo
[] getConstructors​(
MBeanConstructorInfo
[] ctors,

Object
impl)
```

Customization hook:
Get the MBeanConstructorInfo[] that will be used in the MBeanInfo
returned by this MBean.

By default, this method returns

null

if the wrapped
implementation is not

this

. Indeed, if the wrapped
implementation is not this object itself, it will not be possible
to recreate a wrapped implementation by calling the implementation
constructors through

MBeanServer.createMBean(...)

.

Otherwise, if the wrapped implementation is

this

,

ctors

is returned.

Subclasses may redefine this method in order to modify this
behavior, if needed.

**Parameters:** ctors

- The default MBeanConstructorInfo[] derived by reflection.
**Parameters:** impl

- The wrapped implementation. If

null

is
passed, the wrapped implementation is ignored and

ctors

is returned.
**Returns:** the MBeanConstructorInfo[] for the new MBeanInfo.

- getCachedMBeanInfo

```java
protected
MBeanInfo
getCachedMBeanInfo()
```

Customization hook:
Return the MBeanInfo cached for this object.

Subclasses may redefine this method in order to implement their
own caching policy. The default implementation stores one

MBeanInfo

object per instance.

**Returns:** The cached MBeanInfo, or null if no MBeanInfo is cached.
**See Also:** cacheMBeanInfo(MBeanInfo)

- cacheMBeanInfo

```java
protected void cacheMBeanInfo​(
MBeanInfo
info)
```

Customization hook:
cache the MBeanInfo built for this object.

Subclasses may redefine this method in order to implement
their own caching policy. The default implementation stores

info

in this instance. A subclass can define
other policies, such as not saving

info

(so it is
reconstructed every time

getMBeanInfo()

is called) or
sharing a unique

MBeanInfo

object when several

StandardMBean

instances have equal

MBeanInfo

values.

**Parameters:** info

- the new

MBeanInfo

to cache. Any
previously cached value is discarded. This parameter may be
null, in which case there is no new cached value.

- preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception
```

Allows the MBean to perform any operations it needs before
being registered in the MBean server. If the name of the MBean
is not specified, the MBean can provide a name for its
registration. If any exception is raised, the MBean will not be
registered in the MBean server.

The default implementation of this method returns the

name

parameter. It does nothing else for
Standard MBeans. For MXBeans, it records the

MBeanServer

and

ObjectName

parameters so they can be used to translate
inter-MXBean references.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.preRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the MBean will be registered.
**Parameters:** name

- The object name of the MBean. This name is null if
the name parameter to one of the

createMBean

or

registerMBean

methods in the

MBeanServer

interface is null. In that case, this method must return a
non-null ObjectName for the new MBean.
**Returns:** The name under which the MBean is to be registered.
This value must not be null. If the

name

parameter is not null, it will usually but not necessarily be
the returned value.
**Throws:** IllegalArgumentException

- if this is an MXBean and

name

is null.
**Throws:** InstanceAlreadyExistsException

- if this is an MXBean and
it has already been registered under another name (in this
MBean Server or another).
**Throws:** Exception

- no other checked exceptions are thrown by
this method but

Exception

is declared so that subclasses
can override the method and throw their own exceptions.
**Since:** 1.6

- postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

The default implementation of this method does nothing for
Standard MBeans. For MXBeans, it undoes any work done by

preRegister

if registration fails.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.postRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

**Specified by:** postRegister

in interface

MBeanRegistration
**Parameters:** registrationDone

- Indicates whether or not the MBean has
been successfully registered in the MBean server. The value
false means that the registration phase has failed.
**Since:** 1.6

- preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

The default implementation of this method does nothing.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.preDeregister(...)

.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- no checked exceptions are throw by this method
but

Exception

is declared so that subclasses can override
this method and throw their own exceptions.
**Since:** 1.6

- postDeregister

```java
public void postDeregister()
```

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

The default implementation of this method does nothing for
Standard MBeans. For MXBeans, it removes any information that
was recorded by the

preRegister

method.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.postRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

**Specified by:** postDeregister

in interface

MBeanRegistration
**Since:** 1.6

Constructor Detail

- StandardMBean

```java
public StandardMBean​(T implementation,

Class
<T> mbeanInterface)
throws
NotCompliantMBeanException
```

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class.

**Type Parameters:** T

- Allows the compiler to check
that

implementation

does indeed implement the class
described by

mbeanInterface

. The compiler can only
check this if

mbeanInterface

is a class literal such
as

MyMBean.class

.
**Parameters:** implementation

- The implementation of this MBean.
**Parameters:** mbeanInterface

- The Management Interface exported by this
MBean's implementation. If

null

, then this
object will use standard JMX design pattern to determine
the management interface associated with the given
implementation.
**Throws:** IllegalArgumentException

- if the given

implementation

is null.
**Throws:** NotCompliantMBeanException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface.

- StandardMBean

```java
protected StandardMBean​(
Class
<?> mbeanInterface)
throws
NotCompliantMBeanException
```

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class.

Calls

this(this,mbeanInterface)

.
This constructor is reserved to subclasses.

**Parameters:** mbeanInterface

- The Management Interface exported by this
MBean.
**Throws:** NotCompliantMBeanException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface.

- StandardMBean

```java
public StandardMBean​(T implementation,

Class
<T> mbeanInterface,
boolean isMXBean)
```

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class, and choosing whether the
resultant MBean is an MXBean. This constructor can be used
to make either Standard MBeans or MXBeans. Unlike the
constructor

StandardMBean(Object, Class)

, it
does not throw NotCompliantMBeanException.

**Type Parameters:** T

- Allows the compiler to check
that

implementation

does indeed implement the class
described by

mbeanInterface

. The compiler can only
check this if

mbeanInterface

is a class literal such
as

MyMBean.class

.
**Parameters:** implementation

- The implementation of this MBean.
**Parameters:** mbeanInterface

- The Management Interface exported by this
MBean's implementation. If

null

, then this
object will use standard JMX design pattern to determine
the management interface associated with the given
implementation.
**Parameters:** isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
**Throws:** IllegalArgumentException

- if the given

implementation

is null, or if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface.
**Since:** 1.6

- StandardMBean

```java
protected StandardMBean​(
Class
<?> mbeanInterface,
boolean isMXBean)
```

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class, and choosing whether the resulting
MBean is an MXBean. This constructor can be used
to make either Standard MBeans or MXBeans. Unlike the
constructor

StandardMBean(Object, Class)

, it
does not throw NotCompliantMBeanException.

Calls

this(this, mbeanInterface, isMXBean)

.
This constructor is reserved to subclasses.

**Parameters:** mbeanInterface

- The Management Interface exported by this
MBean.
**Parameters:** isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface.
**Since:** 1.6

---

#### Constructor Detail

StandardMBean

```java
public StandardMBean​(T implementation,

Class
<T> mbeanInterface)
throws
NotCompliantMBeanException
```

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class.

**Type Parameters:** T

- Allows the compiler to check
that

implementation

does indeed implement the class
described by

mbeanInterface

. The compiler can only
check this if

mbeanInterface

is a class literal such
as

MyMBean.class

.
**Parameters:** implementation

- The implementation of this MBean.
**Parameters:** mbeanInterface

- The Management Interface exported by this
MBean's implementation. If

null

, then this
object will use standard JMX design pattern to determine
the management interface associated with the given
implementation.
**Throws:** IllegalArgumentException

- if the given

implementation

is null.
**Throws:** NotCompliantMBeanException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface.

---

#### StandardMBean

public StandardMBean​(T implementation,

Class

<T> mbeanInterface)
throws

NotCompliantMBeanException

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class.

StandardMBean

```java
protected StandardMBean​(
Class
<?> mbeanInterface)
throws
NotCompliantMBeanException
```

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class.

Calls

this(this,mbeanInterface)

.
This constructor is reserved to subclasses.

**Parameters:** mbeanInterface

- The Management Interface exported by this
MBean.
**Throws:** NotCompliantMBeanException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface.

---

#### StandardMBean

protected StandardMBean​(

Class

<?> mbeanInterface)
throws

NotCompliantMBeanException

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class.

Calls

this(this,mbeanInterface)

.
This constructor is reserved to subclasses.

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class.

Calls

this(this,mbeanInterface)

.
This constructor is reserved to subclasses.

StandardMBean

```java
public StandardMBean​(T implementation,

Class
<T> mbeanInterface,
boolean isMXBean)
```

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class, and choosing whether the
resultant MBean is an MXBean. This constructor can be used
to make either Standard MBeans or MXBeans. Unlike the
constructor

StandardMBean(Object, Class)

, it
does not throw NotCompliantMBeanException.

**Type Parameters:** T

- Allows the compiler to check
that

implementation

does indeed implement the class
described by

mbeanInterface

. The compiler can only
check this if

mbeanInterface

is a class literal such
as

MyMBean.class

.
**Parameters:** implementation

- The implementation of this MBean.
**Parameters:** mbeanInterface

- The Management Interface exported by this
MBean's implementation. If

null

, then this
object will use standard JMX design pattern to determine
the management interface associated with the given
implementation.
**Parameters:** isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
**Throws:** IllegalArgumentException

- if the given

implementation

is null, or if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface.
**Since:** 1.6

---

#### StandardMBean

public StandardMBean​(T implementation,

Class

<T> mbeanInterface,
boolean isMXBean)

Make a DynamicMBean out of the object

implementation

, using the specified

mbeanInterface

class, and choosing whether the
resultant MBean is an MXBean. This constructor can be used
to make either Standard MBeans or MXBeans. Unlike the
constructor

StandardMBean(Object, Class)

, it
does not throw NotCompliantMBeanException.

StandardMBean

```java
protected StandardMBean​(
Class
<?> mbeanInterface,
boolean isMXBean)
```

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class, and choosing whether the resulting
MBean is an MXBean. This constructor can be used
to make either Standard MBeans or MXBeans. Unlike the
constructor

StandardMBean(Object, Class)

, it
does not throw NotCompliantMBeanException.

Calls

this(this, mbeanInterface, isMXBean)

.
This constructor is reserved to subclasses.

**Parameters:** mbeanInterface

- The Management Interface exported by this
MBean.
**Parameters:** isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface.
**Since:** 1.6

---

#### StandardMBean

protected StandardMBean​(

Class

<?> mbeanInterface,
boolean isMXBean)

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class, and choosing whether the resulting
MBean is an MXBean. This constructor can be used
to make either Standard MBeans or MXBeans. Unlike the
constructor

StandardMBean(Object, Class)

, it
does not throw NotCompliantMBeanException.

Calls

this(this, mbeanInterface, isMXBean)

.
This constructor is reserved to subclasses.

Make a DynamicMBean out of

this

, using the specified

mbeanInterface

class, and choosing whether the resulting
MBean is an MXBean. This constructor can be used
to make either Standard MBeans or MXBeans. Unlike the
constructor

StandardMBean(Object, Class)

, it
does not throw NotCompliantMBeanException.

Calls

this(this, mbeanInterface, isMXBean)

.
This constructor is reserved to subclasses.

Method Detail

- setImplementation

```java
public void setImplementation​(
Object
implementation)
throws
NotCompliantMBeanException
```

Replace the implementation object wrapped in this object.

**Parameters:** implementation

- The new implementation of this Standard MBean
(or MXBean). The

implementation

object must implement
the Standard MBean (or MXBean) interface that was supplied when this

StandardMBean

was constructed.
**Throws:** IllegalArgumentException

- if the given

implementation

is null.
**Throws:** NotCompliantMBeanException

- if the given

implementation

does not implement the
Standard MBean (or MXBean) interface that was
supplied at construction.
**See Also:** getImplementation()

- getImplementation

```java
public
Object
getImplementation()
```

Get the implementation of this Standard MBean (or MXBean).

**Returns:** The implementation of this Standard MBean (or MXBean).
**See Also:** setImplementation(java.lang.Object)

- getMBeanInterface

```java
public final
Class
<?> getMBeanInterface()
```

Get the Management Interface of this Standard MBean (or MXBean).

**Returns:** The management interface of this Standard MBean (or MXBean).

- getImplementationClass

```java
public
Class
<?> getImplementationClass()
```

Get the class of the implementation of this Standard MBean (or MXBean).

**Returns:** The class of the implementation of this Standard MBean (or MXBean).

- getMBeanInfo

```java
public
MBeanInfo
getMBeanInfo()
```

Get the

MBeanInfo

for this MBean.

This method implements

DynamicMBean.getMBeanInfo()

.

This method first calls

getCachedMBeanInfo()

in order to
retrieve the cached MBeanInfo for this MBean, if any. If the
MBeanInfo returned by

getCachedMBeanInfo()

is not null,
then it is returned.

Otherwise, this method builds a default MBeanInfo for this MBean,
using the Management Interface specified for this MBean.

While building the MBeanInfo, this method calls the customization
hooks that make it possible for subclasses to supply their custom
descriptions, parameter names, etc...

Finally, it calls

cacheMBeanInfo()

in order to cache the new MBeanInfo.

**Specified by:** getMBeanInfo

in interface

DynamicMBean
**Returns:** The cached MBeanInfo for that MBean, if not null, or a
newly built MBeanInfo if none was cached.

- getClassName

```java
protected
String
getClassName​(
MBeanInfo
info)
```

Customization hook:
Get the className that will be used in the MBeanInfo returned by
this MBean.

Subclasses may redefine this method in order to supply their
custom class name. The default implementation returns

info.getClassName()

.

**Parameters:** info

- The default MBeanInfo derived by reflection.
**Returns:** the class name for the new MBeanInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanInfo returned by
this MBean.

Subclasses may redefine this method in order to supply their
custom MBean description. The default implementation returns

info.getDescription()

.

**Parameters:** info

- The default MBeanInfo derived by reflection.
**Returns:** the description for the new MBeanInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanFeatureInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanFeatureInfo
returned by this MBean.

Subclasses may redefine this method in order to supply
their custom description. The default implementation returns

info.getDescription()

.

This method is called by

getDescription(MBeanAttributeInfo)

,

getDescription(MBeanOperationInfo)

,

getDescription(MBeanConstructorInfo)

.

**Parameters:** info

- The default MBeanFeatureInfo derived by reflection.
**Returns:** the description for the given MBeanFeatureInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanAttributeInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanAttributeInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

**Parameters:** info

- The default MBeanAttributeInfo derived by reflection.
**Returns:** the description for the given MBeanAttributeInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanConstructorInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanConstructorInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description.
The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

**Parameters:** info

- The default MBeanConstructorInfo derived by reflection.
**Returns:** the description for the given MBeanConstructorInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanConstructorInfo
ctor,

MBeanParameterInfo
param,
int sequence)
```

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

param.getDescription()

.

**Parameters:** ctor

- The default MBeanConstructorInfo derived by reflection.
**Parameters:** param

- The default MBeanParameterInfo derived by reflection.
**Parameters:** sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).
**Returns:** the description for the given MBeanParameterInfo.

- getParameterName

```java
protected
String
getParameterName​(
MBeanConstructorInfo
ctor,

MBeanParameterInfo
param,
int sequence)
```

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom parameter name. The default implementation returns

param.getName()

.

**Parameters:** ctor

- The default MBeanConstructorInfo derived by reflection.
**Parameters:** param

- The default MBeanParameterInfo derived by reflection.
**Parameters:** sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).
**Returns:** the name for the given MBeanParameterInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanOperationInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanOperationInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

**Parameters:** info

- The default MBeanOperationInfo derived by reflection.
**Returns:** the description for the given MBeanOperationInfo.

- getImpact

```java
protected int getImpact​(
MBeanOperationInfo
info)
```

Customization hook:
Get the

impact

flag of the operation that will be used in
the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom impact flag. The default implementation returns

info.getImpact()

.

**Parameters:** info

- The default MBeanOperationInfo derived by reflection.
**Returns:** the impact flag for the given MBeanOperationInfo.

- getParameterName

```java
protected
String
getParameterName​(
MBeanOperationInfo
op,

MBeanParameterInfo
param,
int sequence)
```

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom parameter name. The default implementation returns

param.getName()

.

**Parameters:** op

- The default MBeanOperationInfo derived by reflection.
**Parameters:** param

- The default MBeanParameterInfo derived by reflection.
**Parameters:** sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).
**Returns:** the name to use for the given MBeanParameterInfo.

- getDescription

```java
protected
String
getDescription​(
MBeanOperationInfo
op,

MBeanParameterInfo
param,
int sequence)
```

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

param.getDescription()

.

**Parameters:** op

- The default MBeanOperationInfo derived by reflection.
**Parameters:** param

- The default MBeanParameterInfo derived by reflection.
**Parameters:** sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).
**Returns:** the description for the given MBeanParameterInfo.

- getConstructors

```java
protected
MBeanConstructorInfo
[] getConstructors​(
MBeanConstructorInfo
[] ctors,

Object
impl)
```

Customization hook:
Get the MBeanConstructorInfo[] that will be used in the MBeanInfo
returned by this MBean.

By default, this method returns

null

if the wrapped
implementation is not

this

. Indeed, if the wrapped
implementation is not this object itself, it will not be possible
to recreate a wrapped implementation by calling the implementation
constructors through

MBeanServer.createMBean(...)

.

Otherwise, if the wrapped implementation is

this

,

ctors

is returned.

Subclasses may redefine this method in order to modify this
behavior, if needed.

**Parameters:** ctors

- The default MBeanConstructorInfo[] derived by reflection.
**Parameters:** impl

- The wrapped implementation. If

null

is
passed, the wrapped implementation is ignored and

ctors

is returned.
**Returns:** the MBeanConstructorInfo[] for the new MBeanInfo.

- getCachedMBeanInfo

```java
protected
MBeanInfo
getCachedMBeanInfo()
```

Customization hook:
Return the MBeanInfo cached for this object.

Subclasses may redefine this method in order to implement their
own caching policy. The default implementation stores one

MBeanInfo

object per instance.

**Returns:** The cached MBeanInfo, or null if no MBeanInfo is cached.
**See Also:** cacheMBeanInfo(MBeanInfo)

- cacheMBeanInfo

```java
protected void cacheMBeanInfo​(
MBeanInfo
info)
```

Customization hook:
cache the MBeanInfo built for this object.

Subclasses may redefine this method in order to implement
their own caching policy. The default implementation stores

info

in this instance. A subclass can define
other policies, such as not saving

info

(so it is
reconstructed every time

getMBeanInfo()

is called) or
sharing a unique

MBeanInfo

object when several

StandardMBean

instances have equal

MBeanInfo

values.

**Parameters:** info

- the new

MBeanInfo

to cache. Any
previously cached value is discarded. This parameter may be
null, in which case there is no new cached value.

- preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception
```

Allows the MBean to perform any operations it needs before
being registered in the MBean server. If the name of the MBean
is not specified, the MBean can provide a name for its
registration. If any exception is raised, the MBean will not be
registered in the MBean server.

The default implementation of this method returns the

name

parameter. It does nothing else for
Standard MBeans. For MXBeans, it records the

MBeanServer

and

ObjectName

parameters so they can be used to translate
inter-MXBean references.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.preRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the MBean will be registered.
**Parameters:** name

- The object name of the MBean. This name is null if
the name parameter to one of the

createMBean

or

registerMBean

methods in the

MBeanServer

interface is null. In that case, this method must return a
non-null ObjectName for the new MBean.
**Returns:** The name under which the MBean is to be registered.
This value must not be null. If the

name

parameter is not null, it will usually but not necessarily be
the returned value.
**Throws:** IllegalArgumentException

- if this is an MXBean and

name

is null.
**Throws:** InstanceAlreadyExistsException

- if this is an MXBean and
it has already been registered under another name (in this
MBean Server or another).
**Throws:** Exception

- no other checked exceptions are thrown by
this method but

Exception

is declared so that subclasses
can override the method and throw their own exceptions.
**Since:** 1.6

- postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

The default implementation of this method does nothing for
Standard MBeans. For MXBeans, it undoes any work done by

preRegister

if registration fails.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.postRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

**Specified by:** postRegister

in interface

MBeanRegistration
**Parameters:** registrationDone

- Indicates whether or not the MBean has
been successfully registered in the MBean server. The value
false means that the registration phase has failed.
**Since:** 1.6

- preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

The default implementation of this method does nothing.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.preDeregister(...)

.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- no checked exceptions are throw by this method
but

Exception

is declared so that subclasses can override
this method and throw their own exceptions.
**Since:** 1.6

- postDeregister

```java
public void postDeregister()
```

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

The default implementation of this method does nothing for
Standard MBeans. For MXBeans, it removes any information that
was recorded by the

preRegister

method.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.postRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

**Specified by:** postDeregister

in interface

MBeanRegistration
**Since:** 1.6

---

#### Method Detail

setImplementation

```java
public void setImplementation​(
Object
implementation)
throws
NotCompliantMBeanException
```

Replace the implementation object wrapped in this object.

**Parameters:** implementation

- The new implementation of this Standard MBean
(or MXBean). The

implementation

object must implement
the Standard MBean (or MXBean) interface that was supplied when this

StandardMBean

was constructed.
**Throws:** IllegalArgumentException

- if the given

implementation

is null.
**Throws:** NotCompliantMBeanException

- if the given

implementation

does not implement the
Standard MBean (or MXBean) interface that was
supplied at construction.
**See Also:** getImplementation()

---

#### setImplementation

public void setImplementation​(

Object

implementation)
throws

NotCompliantMBeanException

Replace the implementation object wrapped in this object.

getImplementation

```java
public
Object
getImplementation()
```

Get the implementation of this Standard MBean (or MXBean).

**Returns:** The implementation of this Standard MBean (or MXBean).
**See Also:** setImplementation(java.lang.Object)

---

#### getImplementation

public

Object

getImplementation()

Get the implementation of this Standard MBean (or MXBean).

getMBeanInterface

```java
public final
Class
<?> getMBeanInterface()
```

Get the Management Interface of this Standard MBean (or MXBean).

**Returns:** The management interface of this Standard MBean (or MXBean).

---

#### getMBeanInterface

public final

Class

<?> getMBeanInterface()

Get the Management Interface of this Standard MBean (or MXBean).

getImplementationClass

```java
public
Class
<?> getImplementationClass()
```

Get the class of the implementation of this Standard MBean (or MXBean).

**Returns:** The class of the implementation of this Standard MBean (or MXBean).

---

#### getImplementationClass

public

Class

<?> getImplementationClass()

Get the class of the implementation of this Standard MBean (or MXBean).

getMBeanInfo

```java
public
MBeanInfo
getMBeanInfo()
```

Get the

MBeanInfo

for this MBean.

This method implements

DynamicMBean.getMBeanInfo()

.

This method first calls

getCachedMBeanInfo()

in order to
retrieve the cached MBeanInfo for this MBean, if any. If the
MBeanInfo returned by

getCachedMBeanInfo()

is not null,
then it is returned.

Otherwise, this method builds a default MBeanInfo for this MBean,
using the Management Interface specified for this MBean.

While building the MBeanInfo, this method calls the customization
hooks that make it possible for subclasses to supply their custom
descriptions, parameter names, etc...

Finally, it calls

cacheMBeanInfo()

in order to cache the new MBeanInfo.

**Specified by:** getMBeanInfo

in interface

DynamicMBean
**Returns:** The cached MBeanInfo for that MBean, if not null, or a
newly built MBeanInfo if none was cached.

---

#### getMBeanInfo

public

MBeanInfo

getMBeanInfo()

Get the

MBeanInfo

for this MBean.

This method implements

DynamicMBean.getMBeanInfo()

.

This method first calls

getCachedMBeanInfo()

in order to
retrieve the cached MBeanInfo for this MBean, if any. If the
MBeanInfo returned by

getCachedMBeanInfo()

is not null,
then it is returned.

Otherwise, this method builds a default MBeanInfo for this MBean,
using the Management Interface specified for this MBean.

While building the MBeanInfo, this method calls the customization
hooks that make it possible for subclasses to supply their custom
descriptions, parameter names, etc...

Finally, it calls

cacheMBeanInfo()

in order to cache the new MBeanInfo.

This method implements

DynamicMBean.getMBeanInfo()

.

This method first calls

getCachedMBeanInfo()

in order to
retrieve the cached MBeanInfo for this MBean, if any. If the
MBeanInfo returned by

getCachedMBeanInfo()

is not null,
then it is returned.

Otherwise, this method builds a default MBeanInfo for this MBean,
using the Management Interface specified for this MBean.

While building the MBeanInfo, this method calls the customization
hooks that make it possible for subclasses to supply their custom
descriptions, parameter names, etc...

Finally, it calls

cacheMBeanInfo()

in order to cache the new MBeanInfo.

This method first calls

getCachedMBeanInfo()

in order to
retrieve the cached MBeanInfo for this MBean, if any. If the
MBeanInfo returned by

getCachedMBeanInfo()

is not null,
then it is returned.

Otherwise, this method builds a default MBeanInfo for this MBean,
using the Management Interface specified for this MBean.

While building the MBeanInfo, this method calls the customization
hooks that make it possible for subclasses to supply their custom
descriptions, parameter names, etc...

Finally, it calls

cacheMBeanInfo()

in order to cache the new MBeanInfo.

While building the MBeanInfo, this method calls the customization
hooks that make it possible for subclasses to supply their custom
descriptions, parameter names, etc...

Finally, it calls

cacheMBeanInfo()

in order to cache the new MBeanInfo.

getClassName

```java
protected
String
getClassName​(
MBeanInfo
info)
```

Customization hook:
Get the className that will be used in the MBeanInfo returned by
this MBean.

Subclasses may redefine this method in order to supply their
custom class name. The default implementation returns

info.getClassName()

.

**Parameters:** info

- The default MBeanInfo derived by reflection.
**Returns:** the class name for the new MBeanInfo.

---

#### getClassName

protected

String

getClassName​(

MBeanInfo

info)

Customization hook:
Get the className that will be used in the MBeanInfo returned by
this MBean.

Subclasses may redefine this method in order to supply their
custom class name. The default implementation returns

info.getClassName()

.

getDescription

```java
protected
String
getDescription​(
MBeanInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanInfo returned by
this MBean.

Subclasses may redefine this method in order to supply their
custom MBean description. The default implementation returns

info.getDescription()

.

**Parameters:** info

- The default MBeanInfo derived by reflection.
**Returns:** the description for the new MBeanInfo.

---

#### getDescription

protected

String

getDescription​(

MBeanInfo

info)

Customization hook:
Get the description that will be used in the MBeanInfo returned by
this MBean.

Subclasses may redefine this method in order to supply their
custom MBean description. The default implementation returns

info.getDescription()

.

getDescription

```java
protected
String
getDescription​(
MBeanFeatureInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanFeatureInfo
returned by this MBean.

Subclasses may redefine this method in order to supply
their custom description. The default implementation returns

info.getDescription()

.

This method is called by

getDescription(MBeanAttributeInfo)

,

getDescription(MBeanOperationInfo)

,

getDescription(MBeanConstructorInfo)

.

**Parameters:** info

- The default MBeanFeatureInfo derived by reflection.
**Returns:** the description for the given MBeanFeatureInfo.

---

#### getDescription

protected

String

getDescription​(

MBeanFeatureInfo

info)

Customization hook:
Get the description that will be used in the MBeanFeatureInfo
returned by this MBean.

Subclasses may redefine this method in order to supply
their custom description. The default implementation returns

info.getDescription()

.

This method is called by

getDescription(MBeanAttributeInfo)

,

getDescription(MBeanOperationInfo)

,

getDescription(MBeanConstructorInfo)

.

Customization hook:
Get the description that will be used in the MBeanFeatureInfo
returned by this MBean.

Subclasses may redefine this method in order to supply
their custom description. The default implementation returns

info.getDescription()

.

This method is called by

getDescription(MBeanAttributeInfo)

,

getDescription(MBeanOperationInfo)

,

getDescription(MBeanConstructorInfo)

.

getDescription

```java
protected
String
getDescription​(
MBeanAttributeInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanAttributeInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

**Parameters:** info

- The default MBeanAttributeInfo derived by reflection.
**Returns:** the description for the given MBeanAttributeInfo.

---

#### getDescription

protected

String

getDescription​(

MBeanAttributeInfo

info)

Customization hook:
Get the description that will be used in the MBeanAttributeInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

getDescription

```java
protected
String
getDescription​(
MBeanConstructorInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanConstructorInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description.
The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

**Parameters:** info

- The default MBeanConstructorInfo derived by reflection.
**Returns:** the description for the given MBeanConstructorInfo.

---

#### getDescription

protected

String

getDescription​(

MBeanConstructorInfo

info)

Customization hook:
Get the description that will be used in the MBeanConstructorInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description.
The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

getDescription

```java
protected
String
getDescription​(
MBeanConstructorInfo
ctor,

MBeanParameterInfo
param,
int sequence)
```

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

param.getDescription()

.

**Parameters:** ctor

- The default MBeanConstructorInfo derived by reflection.
**Parameters:** param

- The default MBeanParameterInfo derived by reflection.
**Parameters:** sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).
**Returns:** the description for the given MBeanParameterInfo.

---

#### getDescription

protected

String

getDescription​(

MBeanConstructorInfo

ctor,

MBeanParameterInfo

param,
int sequence)

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

param.getDescription()

.

getParameterName

```java
protected
String
getParameterName​(
MBeanConstructorInfo
ctor,

MBeanParameterInfo
param,
int sequence)
```

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom parameter name. The default implementation returns

param.getName()

.

**Parameters:** ctor

- The default MBeanConstructorInfo derived by reflection.
**Parameters:** param

- The default MBeanParameterInfo derived by reflection.
**Parameters:** sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).
**Returns:** the name for the given MBeanParameterInfo.

---

#### getParameterName

protected

String

getParameterName​(

MBeanConstructorInfo

ctor,

MBeanParameterInfo

param,
int sequence)

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanConstructorInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom parameter name. The default implementation returns

param.getName()

.

getDescription

```java
protected
String
getDescription​(
MBeanOperationInfo
info)
```

Customization hook:
Get the description that will be used in the MBeanOperationInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

**Parameters:** info

- The default MBeanOperationInfo derived by reflection.
**Returns:** the description for the given MBeanOperationInfo.

---

#### getDescription

protected

String

getDescription​(

MBeanOperationInfo

info)

Customization hook:
Get the description that will be used in the MBeanOperationInfo
returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

getDescription((MBeanFeatureInfo) info)

.

getImpact

```java
protected int getImpact​(
MBeanOperationInfo
info)
```

Customization hook:
Get the

impact

flag of the operation that will be used in
the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom impact flag. The default implementation returns

info.getImpact()

.

**Parameters:** info

- The default MBeanOperationInfo derived by reflection.
**Returns:** the impact flag for the given MBeanOperationInfo.

---

#### getImpact

protected int getImpact​(

MBeanOperationInfo

info)

Customization hook:
Get the

impact

flag of the operation that will be used in
the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom impact flag. The default implementation returns

info.getImpact()

.

getParameterName

```java
protected
String
getParameterName​(
MBeanOperationInfo
op,

MBeanParameterInfo
param,
int sequence)
```

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom parameter name. The default implementation returns

param.getName()

.

**Parameters:** op

- The default MBeanOperationInfo derived by reflection.
**Parameters:** param

- The default MBeanParameterInfo derived by reflection.
**Parameters:** sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).
**Returns:** the name to use for the given MBeanParameterInfo.

---

#### getParameterName

protected

String

getParameterName​(

MBeanOperationInfo

op,

MBeanParameterInfo

param,
int sequence)

Customization hook:
Get the name that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom parameter name. The default implementation returns

param.getName()

.

getDescription

```java
protected
String
getDescription​(
MBeanOperationInfo
op,

MBeanParameterInfo
param,
int sequence)
```

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

param.getDescription()

.

**Parameters:** op

- The default MBeanOperationInfo derived by reflection.
**Parameters:** param

- The default MBeanParameterInfo derived by reflection.
**Parameters:** sequence

- The sequence number of the parameter considered
("0" for the first parameter, "1" for the second parameter,
etc...).
**Returns:** the description for the given MBeanParameterInfo.

---

#### getDescription

protected

String

getDescription​(

MBeanOperationInfo

op,

MBeanParameterInfo

param,
int sequence)

Customization hook:
Get the description that will be used for the

sequence

MBeanParameterInfo of the MBeanOperationInfo returned by this MBean.

Subclasses may redefine this method in order to supply their
custom description. The default implementation returns

param.getDescription()

.

getConstructors

```java
protected
MBeanConstructorInfo
[] getConstructors​(
MBeanConstructorInfo
[] ctors,

Object
impl)
```

Customization hook:
Get the MBeanConstructorInfo[] that will be used in the MBeanInfo
returned by this MBean.

By default, this method returns

null

if the wrapped
implementation is not

this

. Indeed, if the wrapped
implementation is not this object itself, it will not be possible
to recreate a wrapped implementation by calling the implementation
constructors through

MBeanServer.createMBean(...)

.

Otherwise, if the wrapped implementation is

this

,

ctors

is returned.

Subclasses may redefine this method in order to modify this
behavior, if needed.

**Parameters:** ctors

- The default MBeanConstructorInfo[] derived by reflection.
**Parameters:** impl

- The wrapped implementation. If

null

is
passed, the wrapped implementation is ignored and

ctors

is returned.
**Returns:** the MBeanConstructorInfo[] for the new MBeanInfo.

---

#### getConstructors

protected

MBeanConstructorInfo

[] getConstructors​(

MBeanConstructorInfo

[] ctors,

Object

impl)

Customization hook:
Get the MBeanConstructorInfo[] that will be used in the MBeanInfo
returned by this MBean.

By default, this method returns

null

if the wrapped
implementation is not

this

. Indeed, if the wrapped
implementation is not this object itself, it will not be possible
to recreate a wrapped implementation by calling the implementation
constructors through

MBeanServer.createMBean(...)

.

Otherwise, if the wrapped implementation is

this

,

ctors

is returned.

Subclasses may redefine this method in order to modify this
behavior, if needed.

getCachedMBeanInfo

```java
protected
MBeanInfo
getCachedMBeanInfo()
```

Customization hook:
Return the MBeanInfo cached for this object.

Subclasses may redefine this method in order to implement their
own caching policy. The default implementation stores one

MBeanInfo

object per instance.

**Returns:** The cached MBeanInfo, or null if no MBeanInfo is cached.
**See Also:** cacheMBeanInfo(MBeanInfo)

---

#### getCachedMBeanInfo

protected

MBeanInfo

getCachedMBeanInfo()

Customization hook:
Return the MBeanInfo cached for this object.

Subclasses may redefine this method in order to implement their
own caching policy. The default implementation stores one

MBeanInfo

object per instance.

Subclasses may redefine this method in order to implement their
own caching policy. The default implementation stores one

MBeanInfo

object per instance.

cacheMBeanInfo

```java
protected void cacheMBeanInfo​(
MBeanInfo
info)
```

Customization hook:
cache the MBeanInfo built for this object.

Subclasses may redefine this method in order to implement
their own caching policy. The default implementation stores

info

in this instance. A subclass can define
other policies, such as not saving

info

(so it is
reconstructed every time

getMBeanInfo()

is called) or
sharing a unique

MBeanInfo

object when several

StandardMBean

instances have equal

MBeanInfo

values.

**Parameters:** info

- the new

MBeanInfo

to cache. Any
previously cached value is discarded. This parameter may be
null, in which case there is no new cached value.

---

#### cacheMBeanInfo

protected void cacheMBeanInfo​(

MBeanInfo

info)

Customization hook:
cache the MBeanInfo built for this object.

Subclasses may redefine this method in order to implement
their own caching policy. The default implementation stores

info

in this instance. A subclass can define
other policies, such as not saving

info

(so it is
reconstructed every time

getMBeanInfo()

is called) or
sharing a unique

MBeanInfo

object when several

StandardMBean

instances have equal

MBeanInfo

values.

Subclasses may redefine this method in order to implement
their own caching policy. The default implementation stores

info

in this instance. A subclass can define
other policies, such as not saving

info

(so it is
reconstructed every time

getMBeanInfo()

is called) or
sharing a unique

MBeanInfo

object when several

StandardMBean

instances have equal

MBeanInfo

values.

preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception
```

Allows the MBean to perform any operations it needs before
being registered in the MBean server. If the name of the MBean
is not specified, the MBean can provide a name for its
registration. If any exception is raised, the MBean will not be
registered in the MBean server.

The default implementation of this method returns the

name

parameter. It does nothing else for
Standard MBeans. For MXBeans, it records the

MBeanServer

and

ObjectName

parameters so they can be used to translate
inter-MXBean references.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.preRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the MBean will be registered.
**Parameters:** name

- The object name of the MBean. This name is null if
the name parameter to one of the

createMBean

or

registerMBean

methods in the

MBeanServer

interface is null. In that case, this method must return a
non-null ObjectName for the new MBean.
**Returns:** The name under which the MBean is to be registered.
This value must not be null. If the

name

parameter is not null, it will usually but not necessarily be
the returned value.
**Throws:** IllegalArgumentException

- if this is an MXBean and

name

is null.
**Throws:** InstanceAlreadyExistsException

- if this is an MXBean and
it has already been registered under another name (in this
MBean Server or another).
**Throws:** Exception

- no other checked exceptions are thrown by
this method but

Exception

is declared so that subclasses
can override the method and throw their own exceptions.
**Since:** 1.6

---

#### preRegister

public

ObjectName

preRegister​(

MBeanServer

server,

ObjectName

name)
throws

Exception

Allows the MBean to perform any operations it needs before
being registered in the MBean server. If the name of the MBean
is not specified, the MBean can provide a name for its
registration. If any exception is raised, the MBean will not be
registered in the MBean server.

The default implementation of this method returns the

name

parameter. It does nothing else for
Standard MBeans. For MXBeans, it records the

MBeanServer

and

ObjectName

parameters so they can be used to translate
inter-MXBean references.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.preRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

Allows the MBean to perform any operations it needs before
being registered in the MBean server. If the name of the MBean
is not specified, the MBean can provide a name for its
registration. If any exception is raised, the MBean will not be
registered in the MBean server.

The default implementation of this method returns the

name

parameter. It does nothing else for
Standard MBeans. For MXBeans, it records the

MBeanServer

and

ObjectName

parameters so they can be used to translate
inter-MXBean references.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.preRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

The default implementation of this method does nothing for
Standard MBeans. For MXBeans, it undoes any work done by

preRegister

if registration fails.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.postRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

**Specified by:** postRegister

in interface

MBeanRegistration
**Parameters:** registrationDone

- Indicates whether or not the MBean has
been successfully registered in the MBean server. The value
false means that the registration phase has failed.
**Since:** 1.6

---

#### postRegister

public void postRegister​(

Boolean

registrationDone)

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

The default implementation of this method does nothing for
Standard MBeans. For MXBeans, it undoes any work done by

preRegister

if registration fails.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.postRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

Allows the MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

The default implementation of this method does nothing for
Standard MBeans. For MXBeans, it undoes any work done by

preRegister

if registration fails.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.postRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

The default implementation of this method does nothing.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.preDeregister(...)

.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- no checked exceptions are throw by this method
but

Exception

is declared so that subclasses can override
this method and throw their own exceptions.
**Since:** 1.6

---

#### preDeregister

public void preDeregister()
throws

Exception

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

The default implementation of this method does nothing.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.preDeregister(...)

.

Allows the MBean to perform any operations it needs before
being unregistered by the MBean server.

The default implementation of this method does nothing.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.preDeregister(...)

.

postDeregister

```java
public void postDeregister()
```

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

The default implementation of this method does nothing for
Standard MBeans. For MXBeans, it removes any information that
was recorded by the

preRegister

method.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.postRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

**Specified by:** postDeregister

in interface

MBeanRegistration
**Since:** 1.6

---

#### postDeregister

public void postDeregister()

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

The default implementation of this method does nothing for
Standard MBeans. For MXBeans, it removes any information that
was recorded by the

preRegister

method.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.postRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

Allows the MBean to perform any operations needed after having been
unregistered in the MBean server.

The default implementation of this method does nothing for
Standard MBeans. For MXBeans, it removes any information that
was recorded by the

preRegister

method.

It is good practice for a subclass that overrides this method
to call the overridden method via

super.postRegister(...)

.
This is necessary if this object is an MXBean that is referenced
by attributes or operations in other MXBeans.

---

