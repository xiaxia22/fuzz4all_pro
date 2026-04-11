# Class MethodHandles.Lookup

**Source:** `java.base\java\lang\invoke\MethodHandles.Lookup.html`

### Class Description

```java
public static final class
MethodHandles.Lookup

extends
Object
```

A

lookup object

is a factory for creating method handles,
when the creation requires access checking.
Method handles do not perform
access checks when they are called, but rather when they are created.
Therefore, method handle access
restrictions must be enforced when a method handle is created.
The caller class against which those restrictions are enforced
is known as the

lookup class

.

A lookup class which needs to create method handles will call

MethodHandles.lookup

to create a factory for itself.
When the

Lookup

factory object is created, the identity of the lookup class is
determined, and securely stored in the

Lookup

object.
The lookup class (or its delegates) may then use factory methods
on the

Lookup

object to create method handles for access-checked members.
This includes all methods, constructors, and fields which are allowed to the lookup class,
even private ones.

Lookup Factory Methods

The factory methods on a

Lookup

object correspond to all major
use cases for methods, constructors, and fields.
Each method handle created by a factory method is the functional
equivalent of a particular

bytecode behavior

.
(Bytecode behaviors are described in section 5.4.3.5 of the Java Virtual Machine Specification.)
Here is a summary of the correspondence between these factory methods and
the behavior of the resulting method handles:

lookup method behaviors

lookup expression

member

bytecode behavior

lookup.findGetter(C.class,"f",FT.class)

FT f;

(T) this.f;

lookup.findStaticGetter(C.class,"f",FT.class)

static

FT f;

(T) C.f;

lookup.findSetter(C.class,"f",FT.class)

FT f;

this.f = x;

lookup.findStaticSetter(C.class,"f",FT.class)

static

FT f;

C.f = arg;

lookup.findVirtual(C.class,"m",MT)

T m(A*);

(T) this.m(arg*);

lookup.findStatic(C.class,"m",MT)

static

T m(A*);

(T) C.m(arg*);

lookup.findSpecial(C.class,"m",MT,this.class)

T m(A*);

(T) super.m(arg*);

lookup.findConstructor(C.class,MT)

C(A*);

new C(arg*);

lookup.unreflectGetter(aField)

(

static

)?

FT f;

(FT) aField.get(thisOrNull);

lookup.unreflectSetter(aField)

(

static

)?

FT f;

aField.set(thisOrNull, arg);

lookup.unreflect(aMethod)

(

static

)?

T m(A*);

(T) aMethod.invoke(thisOrNull, arg*);

lookup.unreflectConstructor(aConstructor)

C(A*);

(C) aConstructor.newInstance(arg*);

lookup.unreflect(aMethod)

(

static

)?

T m(A*);

(T) aMethod.invoke(thisOrNull, arg*);

lookup.findClass("C")

class C { ... }

C.class;

Here, the type

C

is the class or interface being searched for a member,
documented as a parameter named

refc

in the lookup methods.
The method type

MT

is composed from the return type

T

and the sequence of argument types

A*

.
The constructor also has a sequence of argument types

A*

and
is deemed to return the newly-created object of type

C

.
Both

MT

and the field type

FT

are documented as a parameter named

type

.
The formal parameter

this

stands for the self-reference of type

C

;
if it is present, it is always the leading argument to the method handle invocation.
(In the case of some

protected

members,

this

may be
restricted in type to the lookup class; see below.)
The name

arg

stands for all the other method handle arguments.
In the code examples for the Core Reflection API, the name

thisOrNull

stands for a null reference if the accessed method or field is static,
and

this

otherwise.
The names

aMethod

,

aField

, and

aConstructor

stand
for reflective objects corresponding to the given members.

The bytecode behavior for a

findClass

operation is a load of a constant class,
as if by

ldc CONSTANT_Class

.
The behavior is represented, not as a method handle, but directly as a

Class

constant.

In cases where the given member is of variable arity (i.e., a method or constructor)
the returned method handle will also be of

variable arity

.
In all other cases, the returned method handle will be of fixed arity.

Discussion:

The equivalence between looked-up method handles and underlying
class members and bytecode behaviors
can break down in a few ways:

- If

C

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed, even when there is no equivalent
Java expression or bytecoded constant.

Likewise, if

T

or

MT

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed.
For example, lookups for

MethodHandle.invokeExact

and

MethodHandle.invoke

will always succeed, regardless of requested type.

If there is a security manager installed, it can forbid the lookup
on various grounds (

see below

).
By contrast, the

ldc

instruction on a

CONSTANT_MethodHandle

constant is not subject to security manager checks.

If the looked-up method has a

very large arity

,
the method handle creation may fail, due to the method handle
type having too many parameters.

Access checking

Access checks are applied in the factory methods of

Lookup

,
when a method handle is created.
This is a key difference from the Core Reflection API, since

java.lang.reflect.Method.invoke

performs access checking against every caller, on every call.

All access checks start from a

Lookup

object, which
compares its recorded lookup class against all requests to
create method handles.
A single

Lookup

object can be used to create any number
of access-checked method handles, all checked against a single
lookup class.

A

Lookup

object can be shared with other trusted code,
such as a metaobject protocol.
A shared

Lookup

object delegates the capability
to create method handles on private members of the lookup class.
Even if privileged code uses the

Lookup

object,
the access checking is confined to the privileges of the
original lookup class.

A lookup can fail, because
the containing class is not accessible to the lookup class, or
because the desired class member is missing, or because the
desired class member is not accessible to the lookup class, or
because the lookup object is not trusted enough to access the member.
In any of these cases, a

ReflectiveOperationException

will be
thrown from the attempted lookup. The exact class will be one of
the following:

- NoSuchMethodException — if a method is requested but does not exist

NoSuchFieldException — if a field is requested but does not exist

IllegalAccessException — if the member exists but an access check fails

In general, the conditions under which a method handle may be
looked up for a method

M

are no more restrictive than the conditions
under which the lookup class could have compiled, verified, and resolved a call to

M

.
Where the JVM would raise exceptions like

NoSuchMethodError

,
a method handle lookup will generally raise a corresponding
checked exception, such as

NoSuchMethodException

.
And the effect of invoking the method handle resulting from the lookup
is

exactly equivalent

to executing the compiled, verified, and resolved call to

M

.
The same point is true of fields and constructors.

Discussion:

Access checks only apply to named and reflected methods,
constructors, and fields.
Other method handle creation methods, such as

MethodHandle.asType

,
do not require any access checks, and are used
independently of any

Lookup

object.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

**Enclosing class:** MethodHandles

---

### Field Details

#### public static final int PUBLIC

A single-bit mask representing

public

access,
which may contribute to the result of

lookupModes

.
The value,

0x01

, happens to be the same as the value of the

public

modifier bit

.

**See Also:**
- Constant Field Values

---

#### public static final int PRIVATE

A single-bit mask representing

private

access,
which may contribute to the result of

lookupModes

.
The value,

0x02

, happens to be the same as the value of the

private

modifier bit

.

**See Also:**
- Constant Field Values

---

#### public static final int PROTECTED

A single-bit mask representing

protected

access,
which may contribute to the result of

lookupModes

.
The value,

0x04

, happens to be the same as the value of the

protected

modifier bit

.

**See Also:**
- Constant Field Values

---

#### public static final int PACKAGE

A single-bit mask representing

package

access (default access),
which may contribute to the result of

lookupModes

.
The value is

0x08

, which does not correspond meaningfully to
any particular

modifier bit

.

**See Also:**
- Constant Field Values

---

#### public static final int MODULE

A single-bit mask representing

module

access (default access),
which may contribute to the result of

lookupModes

.
The value is

0x10

, which does not correspond meaningfully to
any particular

modifier bit

.
In conjunction with the

PUBLIC

modifier bit, a

Lookup

with this lookup mode can access all public types in the module of the
lookup class and public types in packages exported by other modules
to the module of the lookup class.

**See Also:**
- Constant Field Values

**Since:**
- 9

---

#### public static final int UNCONDITIONAL

A single-bit mask representing

unconditional

access
which may contribute to the result of

lookupModes

.
The value is

0x20

, which does not correspond meaningfully to
any particular

modifier bit

.
A

Lookup

with this lookup mode assumes

readability

.
In conjunction with the

PUBLIC

modifier bit, a

Lookup

with this lookup mode can access all public members of public types
of all modules where the type is in a package that is

exported unconditionally

.

**See Also:**
- MethodHandles.publicLookup()

,

Constant Field Values

**Since:**
- 9

---

### Constructor Details

*No entries found.*

### Method Details

#### public
Class
<?> lookupClass()

Tells which class is performing the lookup. It is this class against
which checks are performed for visibility and access permissions.

The class implies a maximum level of access permission,
but the permissions may be additionally limited by the bitmask

lookupModes

, which controls whether non-public members
can be accessed.

**Returns:**
- the lookup class, on behalf of which this lookup object finds members

---

#### public int lookupModes()

Tells which access-protection classes of members this lookup object can produce.
The result is a bit-mask of the bits

PUBLIC (0x01)

,

PRIVATE (0x02)

,

PROTECTED (0x04)

,

PACKAGE (0x08)

,

MODULE (0x10)

,
and

UNCONDITIONAL (0x20)

.

A freshly-created lookup object
on the

caller's class

has
all possible bits set, except

UNCONDITIONAL

.
A lookup object on a new lookup class

created from a previous lookup object

may have some mode bits set to zero.
Mode bits can also be

directly cleared

.
Once cleared, mode bits cannot be restored from the downgraded lookup object.
The purpose of this is to restrict access via the new lookup object,
so that it can access only names which can be reached by the original
lookup object, and also by the new lookup class.

**Returns:**
- the lookup modes, which limit the kinds of access performed by this lookup object

**See Also:**
- in(java.lang.Class<?>)

,

dropLookupMode(int)

---

#### public
MethodHandles.Lookup
in​(
Class
<?> requestedLookupClass)

Creates a lookup on the specified new lookup class.
The resulting object will report the specified
class as its own

lookupClass

.

However, the resulting

Lookup

object is guaranteed
to have no more access capabilities than the original.
In particular, access capabilities can be lost as follows:

- If the old lookup class is in a

named

module, and
the new lookup class is in a different module

M

, then no members, not
even public members in

M

's exported packages, will be accessible.
The exception to this is when this lookup is

publicLookup

, in which case

PUBLIC

access is not lost.

If the old lookup class is in an unnamed module, and the new lookup class
is a different module then

MODULE

access is lost.

If the new lookup class differs from the old one then

UNCONDITIONAL

is lost.

If the new lookup class is in a different package
than the old one, protected and default (package) members will not be accessible.

If the new lookup class is not within the same package member
as the old one, private members will not be accessible, and protected members
will not be accessible by virtue of inheritance.
(Protected members may continue to be accessible because of package sharing.)

If the new lookup class is not accessible to the old lookup class,
then no members, not even public members, will be accessible.
(In all other cases, public members will continue to be accessible.)

The resulting lookup's capabilities for loading classes
(used during

findClass(java.lang.String)

invocations)
are determined by the lookup class' loader,
which may change due to this operation.

**Parameters:**
- requestedLookupClass

- the desired lookup class for the new lookup object

**Returns:**
- a lookup object which reports the desired lookup class, or the same object
if there is no change

**Throws:**
- NullPointerException

- if the argument is null

---

#### public
MethodHandles.Lookup
dropLookupMode​(int modeToDrop)

Creates a lookup on the same lookup class which this lookup object
finds members, but with a lookup mode that has lost the given lookup mode.
The lookup mode to drop is one of

PUBLIC

,

MODULE

,

PACKAGE

,

PROTECTED

or

PRIVATE

.

PROTECTED

and

UNCONDITIONAL

are always
dropped and so the resulting lookup mode will never have these access capabilities.
When dropping

PACKAGE

then the resulting lookup will not have

PACKAGE

or

PRIVATE

access. When dropping

MODULE

then the resulting lookup will
not have

MODULE

,

PACKAGE

, or

PRIVATE

access. If

PUBLIC

is dropped then the resulting lookup has no access.

**Parameters:**
- modeToDrop

- the lookup mode to drop

**Returns:**
- a lookup object which lacks the indicated mode, or the same object if there is no change

**Throws:**
- IllegalArgumentException

- if

modeToDrop

is not one of

PUBLIC

,

MODULE

,

PACKAGE

,

PROTECTED

,

PRIVATE

or

UNCONDITIONAL

**See Also:**
- MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

**Since:**
- 9

---

#### public
Class
<?> defineClass​(byte[] bytes)
throws
IllegalAccessException

Defines a class to the same class loader and in the same runtime package and

protection domain

as this lookup's

lookup class

.

The

lookup modes

for this lookup must include

PACKAGE

access as default (package) members will be
accessible to the class. The

PACKAGE

lookup mode serves to authenticate
that the lookup object was created by a caller in the runtime package (or derived
from a lookup originally created by suitably privileged code to a target class in
the runtime package).

The

bytes

parameter is the class bytes of a valid class file (as defined
by the

The Java Virtual Machine Specification

) with a class name in the
same package as the lookup class.

This method does not run the class initializer. The class initializer may
run at a later time, as detailed in section 12.4 of the

The Java Language
Specification

.

If there is a security manager, its

checkPermission

method is first called
to check

RuntimePermission("defineClass")

.

**Parameters:**
- bytes

- the class bytes

**Returns:**
- the

Class

object for the class

**Throws:**
- IllegalArgumentException

- the bytes are for a class in a different package
to the lookup class
- IllegalAccessException

- if this lookup does not have

PACKAGE

access
- LinkageError

- if the class is malformed (

ClassFormatError

), cannot be
verified (

VerifyError

), is already defined, or another linkage error occurs
- SecurityException

- if denied by the security manager
- NullPointerException

- if

bytes

is

null

**See Also:**
- MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

,

dropLookupMode(int)

,

ClassLoader.defineClass(String,byte[],int,int,ProtectionDomain)

**Since:**
- 9

---

#### public
String
toString()

Displays the name of the class from which lookups are to be made.
(The name is the one reported by

Class.getName

.)
If there are restrictions on the access permitted to this lookup,
this is indicated by adding a suffix to the class name, consisting
of a slash and a keyword. The keyword represents the strongest
allowed access, and is chosen as follows:

- If no access is allowed, the suffix is "/noaccess".

If only public access to types in exported packages is allowed, the suffix is "/public".

If only public access and unconditional access are allowed, the suffix is "/publicLookup".

If only public and module access are allowed, the suffix is "/module".

If only public, module and package access are allowed, the suffix is "/package".

If only public, module, package, and private access are allowed, the suffix is "/private".

If none of the above cases apply, it is the case that full
access (public, module, package, private, and protected) is allowed.
In this case, no suffix is added.
This is true only of an object obtained originally from

MethodHandles.lookup

.
Objects created by

Lookup.in

always have restricted access, and will display a suffix.

(It may seem strange that protected access should be
stronger than private access. Viewed independently from
package access, protected access is the first to be lost,
because it requires a direct subclass relationship between
caller and callee.)

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

**See Also:**
- in(java.lang.Class<?>)

---

#### public
MethodHandle
findStatic​(
Class
<?> refc,

String
name,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException

Produces a method handle for a static method.
The type of the method handle will be that of the method.
(Since static methods do not take receivers, there is no
additional receiver argument inserted into the method handle type,
as there would be with

findVirtual

or

findSpecial

.)
The method and all its argument types must be accessible to the lookup object.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_asList = publicLookup().findStatic(Arrays.class,
"asList", methodType(List.class, Object[].class));
assertEquals("[x, y]", MH_asList.invoke("x", "y").toString());
```

**Parameters:**
- refc

- the class from which the method is accessed
- name

- the name of the method
- type

- the type of the method

**Returns:**
- the desired method handle

**Throws:**
- NoSuchMethodException

- if the method does not exist
- IllegalAccessException

- if access checking fails,
or if the method is not

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
- SecurityException

- if a security manager is present and it

refuses access
- NullPointerException

- if any argument is null

---

#### public
MethodHandle
findVirtual​(
Class
<?> refc,

String
name,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException

Produces a method handle for a virtual method.
The type of the method handle will be that of the method,
with the receiver type (usually

refc

) prepended.
The method and all its argument types must be accessible to the lookup object.

When called, the handle will treat the first argument as a receiver
and, for non-private methods, dispatch on the receiver's type to determine which method
implementation to enter.
For private methods the named method in

refc

will be invoked on the receiver.
(The dispatching action is identical with that performed by an

invokevirtual

or

invokeinterface

instruction.)

The first argument will be of type

refc

if the lookup
class has full privileges to access the member. Otherwise
the member must be

protected

and the first argument
will be restricted in type to the lookup class.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

Because of the general

equivalence

between

invokevirtual

instructions and method handles produced by

findVirtual

,
if the class is

MethodHandle

and the name string is

invokeExact

or

invoke

, the resulting
method handle is equivalent to one produced by

MethodHandles.exactInvoker

or

MethodHandles.invoker

with the same

type

argument.

If the class is

VarHandle

and the name string corresponds to
the name of a signature-polymorphic access mode method, the resulting
method handle is equivalent to one produced by

MethodHandles.varHandleInvoker(java.lang.invoke.VarHandle.AccessMode, java.lang.invoke.MethodType)

with
the access mode corresponding to the name string and with the same

type

arguments.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_concat = publicLookup().findVirtual(String.class,
"concat", methodType(String.class, String.class));
MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
"hashCode", methodType(int.class));
MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
"hashCode", methodType(int.class));
assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
// interface method:
MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
"subSequence", methodType(CharSequence.class, int.class, int.class));
assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
// constructor "internal method" must be accessed differently:
MethodType MT_newString = methodType(void.class); //()V for new String()
try { assertEquals("impossible", lookup()
.findVirtual(String.class, "<init>", MT_newString));
} catch (NoSuchMethodException ex) { } // OK
MethodHandle MH_newString = publicLookup()
.findConstructor(String.class, MT_newString);
assertEquals("", (String) MH_newString.invokeExact());
```

**Parameters:**
- refc

- the class or interface from which the method is accessed
- name

- the name of the method
- type

- the type of the method, with the receiver argument omitted

**Returns:**
- the desired method handle

**Throws:**
- NoSuchMethodException

- if the method does not exist
- IllegalAccessException

- if access checking fails,
or if the method is

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
- SecurityException

- if a security manager is present and it

refuses access
- NullPointerException

- if any argument is null

---

#### public
MethodHandle
findConstructor​(
Class
<?> refc,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException

Produces a method handle which creates an object and initializes it, using
the constructor of the specified type.
The parameter types of the method handle will be those of the constructor,
while the return type will be a reference to the constructor's class.
The constructor and all its argument types must be accessible to the lookup object.

The requested type must have a return type of

void

.
(This is consistent with the JVM's treatment of constructor type descriptors.)

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_newArrayList = publicLookup().findConstructor(
ArrayList.class, methodType(void.class, Collection.class));
Collection orig = Arrays.asList("x", "y");
Collection copy = (ArrayList) MH_newArrayList.invokeExact(orig);
assert(orig != copy);
assertEquals(orig, copy);
// a variable-arity constructor:
MethodHandle MH_newProcessBuilder = publicLookup().findConstructor(
ProcessBuilder.class, methodType(void.class, String[].class));
ProcessBuilder pb = (ProcessBuilder)
MH_newProcessBuilder.invoke("x", "y", "z");
assertEquals("[x, y, z]", pb.command().toString());
```

**Parameters:**
- refc

- the class or interface from which the method is accessed
- type

- the type of the method, with the receiver argument omitted, and a void return type

**Returns:**
- the desired method handle

**Throws:**
- NoSuchMethodException

- if the constructor does not exist
- IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
- SecurityException

- if a security manager is present and it

refuses access
- NullPointerException

- if any argument is null

---

#### public
Class
<?> findClass​(
String
targetName)
throws
ClassNotFoundException
,

IllegalAccessException

Looks up a class by name from the lookup context defined by this

Lookup

object. The static
initializer of the class is not run.

The lookup context here is determined by the

lookup class

, its class
loader, and the

lookup modes

. In particular, the method first attempts to
load the requested class, and then determines whether the class is accessible to this lookup object.

**Parameters:**
- targetName

- the fully qualified name of the class to be looked up.

**Returns:**
- the requested class.

**Throws:**
- SecurityException

- if a security manager is present and it

refuses access
- LinkageError

- if the linkage fails
- ClassNotFoundException

- if the class cannot be loaded by the lookup class' loader.
- IllegalAccessException

- if the class is not accessible, using the allowed access
modes.
- SecurityException

- if a security manager is present and it

refuses access

**Since:**
- 9

---

#### public
Class
<?> accessClass​(
Class
<?> targetClass)
throws
IllegalAccessException

Determines if a class can be accessed from the lookup context defined by this

Lookup

object. The
static initializer of the class is not run.

The lookup context here is determined by the

lookup class

and the

lookup modes

.

**Parameters:**
- targetClass

- the class to be access-checked

**Returns:**
- the class that has been access-checked

**Throws:**
- IllegalAccessException

- if the class is not accessible from the lookup class, using the allowed access
modes.
- SecurityException

- if a security manager is present and it

refuses access

**Since:**
- 9

---

#### public
MethodHandle
findSpecial​(
Class
<?> refc,

String
name,

MethodType
type,

Class
<?> specialCaller)
throws
NoSuchMethodException
,

IllegalAccessException

Produces an early-bound method handle for a virtual method.
It will bypass checks for overriding methods on the receiver,

as if called

from an

invokespecial

instruction from within the explicitly specified

specialCaller

.
The type of the method handle will be that of the method,
with a suitably restricted receiver type prepended.
(The receiver type will be

specialCaller

or a subtype.)
The method and all its argument types must be accessible
to the lookup object.

Before method resolution,
if the explicitly specified caller class is not identical with the
lookup class, or if this lookup object does not have

private access

privileges, the access fails.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

(Note: JVM internal methods named

"<init>"

are not visible to this API,
even though the

invokespecial

instruction can refer to them
in special circumstances. Use

findConstructor

to access instance initialization methods in a safe manner.)

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
static class Listie extends ArrayList {
public String toString() { return "[wee Listie]"; }
static Lookup lookup() { return MethodHandles.lookup(); }
}
...
// no access to constructor via invokeSpecial:
MethodHandle MH_newListie = Listie.lookup()
.findConstructor(Listie.class, methodType(void.class));
Listie l = (Listie) MH_newListie.invokeExact();
try { assertEquals("impossible", Listie.lookup().findSpecial(
Listie.class, "<init>", methodType(void.class), Listie.class));
} catch (NoSuchMethodException ex) { } // OK
// access to super and self methods via invokeSpecial:
MethodHandle MH_super = Listie.lookup().findSpecial(
ArrayList.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_this = Listie.lookup().findSpecial(
Listie.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_duper = Listie.lookup().findSpecial(
Object.class, "toString" , methodType(String.class), Listie.class);
assertEquals("[]", (String) MH_super.invokeExact(l));
assertEquals(""+l, (String) MH_this.invokeExact(l));
assertEquals("[]", (String) MH_duper.invokeExact(l)); // ArrayList method
try { assertEquals("inaccessible", Listie.lookup().findSpecial(
String.class, "toString", methodType(String.class), Listie.class));
} catch (IllegalAccessException ex) { } // OK
Listie subl = new Listie() { public String toString() { return "[subclass]"; } };
assertEquals(""+l, (String) MH_this.invokeExact(subl)); // Listie method
```

**Parameters:**
- refc

- the class or interface from which the method is accessed
- name

- the name of the method (which must not be "<init>")
- type

- the type of the method, with the receiver argument omitted
- specialCaller

- the proposed calling class to perform the

invokespecial

**Returns:**
- the desired method handle

**Throws:**
- NoSuchMethodException

- if the method does not exist
- IllegalAccessException

- if access checking fails,
or if the method is

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
- SecurityException

- if a security manager is present and it

refuses access
- NullPointerException

- if any argument is null

---

#### public
MethodHandle
findGetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException

Produces a method handle giving read access to a non-static field.
The type of the method handle will have a return type of the field's
value type.
The method handle's single argument will be the instance containing
the field.
Access checking is performed immediately on behalf of the lookup class.

**Parameters:**
- refc

- the class or interface from which the method is accessed
- name

- the field's name
- type

- the field's type

**Returns:**
- a method handle which can load values from the field

**Throws:**
- NoSuchFieldException

- if the field does not exist
- IllegalAccessException

- if access checking fails, or if the field is

static
- SecurityException

- if a security manager is present and it

refuses access
- NullPointerException

- if any argument is null

**See Also:**
- findVarHandle(Class, String, Class)

---

#### public
MethodHandle
findSetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException

Produces a method handle giving write access to a non-static field.
The type of the method handle will have a void return type.
The method handle will take two arguments, the instance containing
the field, and the value to be stored.
The second argument will be of the field's value type.
Access checking is performed immediately on behalf of the lookup class.

**Parameters:**
- refc

- the class or interface from which the method is accessed
- name

- the field's name
- type

- the field's type

**Returns:**
- a method handle which can store values into the field

**Throws:**
- NoSuchFieldException

- if the field does not exist
- IllegalAccessException

- if access checking fails, or if the field is

static
- SecurityException

- if a security manager is present and it

refuses access
- NullPointerException

- if any argument is null

**See Also:**
- findVarHandle(Class, String, Class)

---

#### public
VarHandle
findVarHandle​(
Class
<?> recv,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException

Produces a VarHandle giving access to a non-static field

name

of type

type

declared in a class of type

recv

.
The VarHandle's variable type is

type

and it has one
coordinate type,

recv

.

Access checking is performed immediately on behalf of the lookup
class.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

**Parameters:**
- recv

- the receiver class, of type

R

, that declares the
non-static field
- name

- the field's name
- type

- the field's type, of type

T

**Returns:**
- a VarHandle giving access to non-static fields.

**Throws:**
- NoSuchFieldException

- if the field does not exist
- IllegalAccessException

- if access checking fails, or if the field is

static
- SecurityException

- if a security manager is present and it

refuses access
- NullPointerException

- if any argument is null

**Since:**
- 9

**API Note:**
- Bitwise comparison of

float

values or

double

values,
as performed by the numeric and atomic update access modes, differ
from the primitive

==

operator and the

Float.equals(java.lang.Object)

and

Double.equals(java.lang.Object)

methods, specifically with respect to
comparing NaN values or comparing

-0.0

with

+0.0

.
Care should be taken when performing a compare and set or a compare
and exchange operation with such values since the operation may
unexpectedly fail.
There are many possible NaN values that are considered to be

NaN

in Java, although no IEEE 754 floating-point operation
provided by Java can distinguish between them. Operation failure can
occur if the expected or witness value is a NaN value and it is
transformed (perhaps in a platform specific manner) into another NaN
value, and thus has a different bitwise representation (see

Float.intBitsToFloat(int)

or

Double.longBitsToDouble(long)

for more
details).
The values

-0.0

and

+0.0

have different bitwise
representations but are considered equal when using the primitive

==

operator. Operation failure can occur if, for example, a
numeric algorithm computes an expected value to be say

-0.0

and previously computed the witness value to be say

+0.0

.

---

#### public
MethodHandle
findStaticGetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException

Produces a method handle giving read access to a static field.
The type of the method handle will have a return type of the field's
value type.
The method handle will take no arguments.
Access checking is performed immediately on behalf of the lookup class.

If the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:**
- refc

- the class or interface from which the method is accessed
- name

- the field's name
- type

- the field's type

**Returns:**
- a method handle which can load values from the field

**Throws:**
- NoSuchFieldException

- if the field does not exist
- IllegalAccessException

- if access checking fails, or if the field is not

static
- SecurityException

- if a security manager is present and it

refuses access
- NullPointerException

- if any argument is null

---

#### public
MethodHandle
findStaticSetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException

Produces a method handle giving write access to a static field.
The type of the method handle will have a void return type.
The method handle will take a single
argument, of the field's value type, the value to be stored.
Access checking is performed immediately on behalf of the lookup class.

If the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:**
- refc

- the class or interface from which the method is accessed
- name

- the field's name
- type

- the field's type

**Returns:**
- a method handle which can store values into the field

**Throws:**
- NoSuchFieldException

- if the field does not exist
- IllegalAccessException

- if access checking fails, or if the field is not

static
- SecurityException

- if a security manager is present and it

refuses access
- NullPointerException

- if any argument is null

---

#### public
VarHandle
findStaticVarHandle​(
Class
<?> decl,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException

Produces a VarHandle giving access to a static field

name

of
type

type

declared in a class of type

decl

.
The VarHandle's variable type is

type

and it has no
coordinate types.

Access checking is performed immediately on behalf of the lookup
class.

If the returned VarHandle is operated on, the declaring class will be
initialized, if it has not already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

, then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

**Parameters:**
- decl

- the class that declares the static field
- name

- the field's name
- type

- the field's type, of type

T

**Returns:**
- a VarHandle giving access to a static field

**Throws:**
- NoSuchFieldException

- if the field does not exist
- IllegalAccessException

- if access checking fails, or if the field is not

static
- SecurityException

- if a security manager is present and it

refuses access
- NullPointerException

- if any argument is null

**Since:**
- 9

**API Note:**
- Bitwise comparison of

float

values or

double

values,
as performed by the numeric and atomic update access modes, differ
from the primitive

==

operator and the

Float.equals(java.lang.Object)

and

Double.equals(java.lang.Object)

methods, specifically with respect to
comparing NaN values or comparing

-0.0

with

+0.0

.
Care should be taken when performing a compare and set or a compare
and exchange operation with such values since the operation may
unexpectedly fail.
There are many possible NaN values that are considered to be

NaN

in Java, although no IEEE 754 floating-point operation
provided by Java can distinguish between them. Operation failure can
occur if the expected or witness value is a NaN value and it is
transformed (perhaps in a platform specific manner) into another NaN
value, and thus has a different bitwise representation (see

Float.intBitsToFloat(int)

or

Double.longBitsToDouble(long)

for more
details).
The values

-0.0

and

+0.0

have different bitwise
representations but are considered equal when using the primitive

==

operator. Operation failure can occur if, for example, a
numeric algorithm computes an expected value to be say

-0.0

and previously computed the witness value to be say

+0.0

.

---

#### public
MethodHandle
bind​(
Object
receiver,

String
name,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException

Produces an early-bound method handle for a non-static method.
The receiver must have a supertype

defc

in which a method
of the given name and type is accessible to the lookup class.
The method and all its argument types must be accessible to the lookup object.
The type of the method handle will be that of the method,
without any insertion of an additional receiver parameter.
The given receiver will be bound into the method handle,
so that every call to the method handle will invoke the
requested method on the given receiver.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set

and

the trailing array argument is not the only argument.
(If the trailing array argument is the only argument,
the given receiver value will be bound to it.)

This is almost equivalent to the following code, with some differences noted below:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle mh0 = lookup().findVirtual(defc, name, type);
MethodHandle mh1 = mh0.bindTo(receiver);
mh1 = mh1.withVarargs(mh0.isVarargsCollector());
return mh1;
```

where

defc

is either

receiver.getClass()

or a super
type of that class, in which the requested method is accessible
to the lookup class.
(Unlike

bind

,

bindTo

does not preserve variable arity.
Also,

bindTo

may throw a

ClassCastException

in instances where

bind

would
throw an

IllegalAccessException

, as in the case where the member is

protected

and
the receiver is restricted by

findVirtual

to the lookup class.)

**Parameters:**
- receiver

- the object from which the method is accessed
- name

- the name of the method
- type

- the type of the method, with the receiver argument omitted

**Returns:**
- the desired method handle

**Throws:**
- NoSuchMethodException

- if the method does not exist
- IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
- SecurityException

- if a security manager is present and it

refuses access
- NullPointerException

- if any argument is null

**See Also:**
- MethodHandle.bindTo(java.lang.Object)

,

findVirtual(java.lang.Class<?>, java.lang.String, java.lang.invoke.MethodType)

---

#### public
MethodHandle
unreflect​(
Method
m)
throws
IllegalAccessException

Makes a

direct method handle

to

m

, if the lookup class has permission.
If

m

is non-static, the receiver argument is treated as an initial argument.
If

m

is virtual, overriding is respected on every call.
Unlike the Core Reflection API, exceptions are

not

wrapped.
The type of the method handle will be that of the method,
with the receiver type prepended (but only if it is non-static).
If the method's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.
If

m

is not public, do not share the resulting handle with untrusted parties.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

If

m

is static, and
if the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

**Parameters:**
- m

- the reflected method

**Returns:**
- a method handle which can invoke the reflected method

**Throws:**
- IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
- NullPointerException

- if the argument is null

---

#### public
MethodHandle
unreflectSpecial​(
Method
m,

Class
<?> specialCaller)
throws
IllegalAccessException

Produces a method handle for a reflected method.
It will bypass checks for overriding methods on the receiver,

as if called

from an

invokespecial

instruction from within the explicitly specified

specialCaller

.
The type of the method handle will be that of the method,
with a suitably restricted receiver type prepended.
(The receiver type will be

specialCaller

or a subtype.)
If the method's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class,
as if

invokespecial

instruction were being linked.

Before method resolution,
if the explicitly specified caller class is not identical with the
lookup class, or if this lookup object does not have

private access

privileges, the access fails.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

**Parameters:**
- m

- the reflected method
- specialCaller

- the class nominally calling the method

**Returns:**
- a method handle which can invoke the reflected method

**Throws:**
- IllegalAccessException

- if access checking fails,
or if the method is

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
- NullPointerException

- if any argument is null

---

#### public
MethodHandle
unreflectConstructor​(
Constructor
<?> c)
throws
IllegalAccessException

Produces a method handle for a reflected constructor.
The type of the method handle will be that of the constructor,
with the return type changed to the declaring class.
The method handle will perform a

newInstance

operation,
creating a new instance of the constructor's class on the
arguments passed to the method handle.

If the constructor's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

**Parameters:**
- c

- the reflected constructor

**Returns:**
- a method handle which can invoke the reflected constructor

**Throws:**
- IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
- NullPointerException

- if the argument is null

---

#### public
MethodHandle
unreflectGetter​(
Field
f)
throws
IllegalAccessException

Produces a method handle giving read access to a reflected field.
The type of the method handle will have a return type of the field's
value type.
If the field is static, the method handle will take no arguments.
Otherwise, its single argument will be the instance containing
the field.
If the field's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

If the field is static, and
if the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:**
- f

- the reflected field

**Returns:**
- a method handle which can load values from the reflected field

**Throws:**
- IllegalAccessException

- if access checking fails
- NullPointerException

- if the argument is null

---

#### public
MethodHandle
unreflectSetter​(
Field
f)
throws
IllegalAccessException

Produces a method handle giving write access to a reflected field.
The type of the method handle will have a void return type.
If the field is static, the method handle will take a single
argument, of the field's value type, the value to be stored.
Otherwise, the two arguments will be the instance containing
the field, and the value to be stored.
If the field's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

If the field is static, and
if the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:**
- f

- the reflected field

**Returns:**
- a method handle which can store values into the reflected field

**Throws:**
- IllegalAccessException

- if access checking fails
- NullPointerException

- if the argument is null

---

#### public
VarHandle
unreflectVarHandle​(
Field
f)
throws
IllegalAccessException

Produces a VarHandle giving access to a reflected field

f

of type

T

declared in a class of type

R

.
The VarHandle's variable type is

T

.
If the field is non-static the VarHandle has one coordinate type,

R

. Otherwise, the field is static, and the VarHandle has no
coordinate types.

Access checking is performed immediately on behalf of the lookup
class, regardless of the value of the field's

accessible

flag.

If the field is static, and if the returned VarHandle is operated
on, the field's declaring class will be initialized, if it has not
already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

**Parameters:**
- f

- the reflected field, with a field of type

T

, and
a declaring class of type

R

**Returns:**
- a VarHandle giving access to non-static fields or a static
field

**Throws:**
- IllegalAccessException

- if access checking fails
- NullPointerException

- if the argument is null

**Since:**
- 9

**API Note:**
- Bitwise comparison of

float

values or

double

values,
as performed by the numeric and atomic update access modes, differ
from the primitive

==

operator and the

Float.equals(java.lang.Object)

and

Double.equals(java.lang.Object)

methods, specifically with respect to
comparing NaN values or comparing

-0.0

with

+0.0

.
Care should be taken when performing a compare and set or a compare
and exchange operation with such values since the operation may
unexpectedly fail.
There are many possible NaN values that are considered to be

NaN

in Java, although no IEEE 754 floating-point operation
provided by Java can distinguish between them. Operation failure can
occur if the expected or witness value is a NaN value and it is
transformed (perhaps in a platform specific manner) into another NaN
value, and thus has a different bitwise representation (see

Float.intBitsToFloat(int)

or

Double.longBitsToDouble(long)

for more
details).
The values

-0.0

and

+0.0

have different bitwise
representations but are considered equal when using the primitive

==

operator. Operation failure can occur if, for example, a
numeric algorithm computes an expected value to be say

-0.0

and previously computed the witness value to be say

+0.0

.

---

#### public
MethodHandleInfo
revealDirect​(
MethodHandle
target)

Cracks a

direct method handle

created by this lookup object or a similar one.
Security and access checks are performed to ensure that this lookup object
is capable of reproducing the target method handle.
This means that the cracking may fail if target is a direct method handle
but was created by an unrelated lookup object.
This can happen if the method handle is

caller sensitive

and was created by a lookup object for a different class.

**Parameters:**
- target

- a direct method handle to crack into symbolic reference components

**Returns:**
- a symbolic reference which can be used to reconstruct this method handle from this lookup object

**Throws:**
- SecurityException

- if a security manager is present and it

refuses access
- IllegalArgumentException

- if the target is not a direct method handle or if access checking fails
- NullPointerException

- if the target is

null

**See Also:**
- MethodHandleInfo

**Since:**
- 1.8

---

#### public boolean hasPrivateAccess()

Returns

true

if this lookup has

PRIVATE

access.

**Returns:**
- true

if this lookup has

PRIVATE

access.

**Since:**
- 9

---

### Additional Sections

#### Class MethodHandles.Lookup

java.lang.Object

- java.lang.invoke.MethodHandles.Lookup

java.lang.invoke.MethodHandles.Lookup

**Enclosing class:** MethodHandles

```java
public static final class
MethodHandles.Lookup

extends
Object
```

A

lookup object

is a factory for creating method handles,
when the creation requires access checking.
Method handles do not perform
access checks when they are called, but rather when they are created.
Therefore, method handle access
restrictions must be enforced when a method handle is created.
The caller class against which those restrictions are enforced
is known as the

lookup class

.

A lookup class which needs to create method handles will call

MethodHandles.lookup

to create a factory for itself.
When the

Lookup

factory object is created, the identity of the lookup class is
determined, and securely stored in the

Lookup

object.
The lookup class (or its delegates) may then use factory methods
on the

Lookup

object to create method handles for access-checked members.
This includes all methods, constructors, and fields which are allowed to the lookup class,
even private ones.

Lookup Factory Methods

The factory methods on a

Lookup

object correspond to all major
use cases for methods, constructors, and fields.
Each method handle created by a factory method is the functional
equivalent of a particular

bytecode behavior

.
(Bytecode behaviors are described in section 5.4.3.5 of the Java Virtual Machine Specification.)
Here is a summary of the correspondence between these factory methods and
the behavior of the resulting method handles:

lookup method behaviors

lookup expression

member

bytecode behavior

lookup.findGetter(C.class,"f",FT.class)

FT f;

(T) this.f;

lookup.findStaticGetter(C.class,"f",FT.class)

static

FT f;

(T) C.f;

lookup.findSetter(C.class,"f",FT.class)

FT f;

this.f = x;

lookup.findStaticSetter(C.class,"f",FT.class)

static

FT f;

C.f = arg;

lookup.findVirtual(C.class,"m",MT)

T m(A*);

(T) this.m(arg*);

lookup.findStatic(C.class,"m",MT)

static

T m(A*);

(T) C.m(arg*);

lookup.findSpecial(C.class,"m",MT,this.class)

T m(A*);

(T) super.m(arg*);

lookup.findConstructor(C.class,MT)

C(A*);

new C(arg*);

lookup.unreflectGetter(aField)

(

static

)?

FT f;

(FT) aField.get(thisOrNull);

lookup.unreflectSetter(aField)

(

static

)?

FT f;

aField.set(thisOrNull, arg);

lookup.unreflect(aMethod)

(

static

)?

T m(A*);

(T) aMethod.invoke(thisOrNull, arg*);

lookup.unreflectConstructor(aConstructor)

C(A*);

(C) aConstructor.newInstance(arg*);

lookup.unreflect(aMethod)

(

static

)?

T m(A*);

(T) aMethod.invoke(thisOrNull, arg*);

lookup.findClass("C")

class C { ... }

C.class;

Here, the type

C

is the class or interface being searched for a member,
documented as a parameter named

refc

in the lookup methods.
The method type

MT

is composed from the return type

T

and the sequence of argument types

A*

.
The constructor also has a sequence of argument types

A*

and
is deemed to return the newly-created object of type

C

.
Both

MT

and the field type

FT

are documented as a parameter named

type

.
The formal parameter

this

stands for the self-reference of type

C

;
if it is present, it is always the leading argument to the method handle invocation.
(In the case of some

protected

members,

this

may be
restricted in type to the lookup class; see below.)
The name

arg

stands for all the other method handle arguments.
In the code examples for the Core Reflection API, the name

thisOrNull

stands for a null reference if the accessed method or field is static,
and

this

otherwise.
The names

aMethod

,

aField

, and

aConstructor

stand
for reflective objects corresponding to the given members.

The bytecode behavior for a

findClass

operation is a load of a constant class,
as if by

ldc CONSTANT_Class

.
The behavior is represented, not as a method handle, but directly as a

Class

constant.

In cases where the given member is of variable arity (i.e., a method or constructor)
the returned method handle will also be of

variable arity

.
In all other cases, the returned method handle will be of fixed arity.

Discussion:

The equivalence between looked-up method handles and underlying
class members and bytecode behaviors
can break down in a few ways:

- If

C

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed, even when there is no equivalent
Java expression or bytecoded constant.

Likewise, if

T

or

MT

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed.
For example, lookups for

MethodHandle.invokeExact

and

MethodHandle.invoke

will always succeed, regardless of requested type.

If there is a security manager installed, it can forbid the lookup
on various grounds (

see below

).
By contrast, the

ldc

instruction on a

CONSTANT_MethodHandle

constant is not subject to security manager checks.

If the looked-up method has a

very large arity

,
the method handle creation may fail, due to the method handle
type having too many parameters.

Access checking

Access checks are applied in the factory methods of

Lookup

,
when a method handle is created.
This is a key difference from the Core Reflection API, since

java.lang.reflect.Method.invoke

performs access checking against every caller, on every call.

All access checks start from a

Lookup

object, which
compares its recorded lookup class against all requests to
create method handles.
A single

Lookup

object can be used to create any number
of access-checked method handles, all checked against a single
lookup class.

A

Lookup

object can be shared with other trusted code,
such as a metaobject protocol.
A shared

Lookup

object delegates the capability
to create method handles on private members of the lookup class.
Even if privileged code uses the

Lookup

object,
the access checking is confined to the privileges of the
original lookup class.

A lookup can fail, because
the containing class is not accessible to the lookup class, or
because the desired class member is missing, or because the
desired class member is not accessible to the lookup class, or
because the lookup object is not trusted enough to access the member.
In any of these cases, a

ReflectiveOperationException

will be
thrown from the attempted lookup. The exact class will be one of
the following:

- NoSuchMethodException — if a method is requested but does not exist

NoSuchFieldException — if a field is requested but does not exist

IllegalAccessException — if the member exists but an access check fails

In general, the conditions under which a method handle may be
looked up for a method

M

are no more restrictive than the conditions
under which the lookup class could have compiled, verified, and resolved a call to

M

.
Where the JVM would raise exceptions like

NoSuchMethodError

,
a method handle lookup will generally raise a corresponding
checked exception, such as

NoSuchMethodException

.
And the effect of invoking the method handle resulting from the lookup
is

exactly equivalent

to executing the compiled, verified, and resolved call to

M

.
The same point is true of fields and constructors.

Discussion:

Access checks only apply to named and reflected methods,
constructors, and fields.
Other method handle creation methods, such as

MethodHandle.asType

,
do not require any access checks, and are used
independently of any

Lookup

object.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

public static final class

MethodHandles.Lookup

extends

Object

A

lookup object

is a factory for creating method handles,
when the creation requires access checking.
Method handles do not perform
access checks when they are called, but rather when they are created.
Therefore, method handle access
restrictions must be enforced when a method handle is created.
The caller class against which those restrictions are enforced
is known as the

lookup class

.

A lookup class which needs to create method handles will call

MethodHandles.lookup

to create a factory for itself.
When the

Lookup

factory object is created, the identity of the lookup class is
determined, and securely stored in the

Lookup

object.
The lookup class (or its delegates) may then use factory methods
on the

Lookup

object to create method handles for access-checked members.
This includes all methods, constructors, and fields which are allowed to the lookup class,
even private ones.

Lookup Factory Methods

The factory methods on a

Lookup

object correspond to all major
use cases for methods, constructors, and fields.
Each method handle created by a factory method is the functional
equivalent of a particular

bytecode behavior

.
(Bytecode behaviors are described in section 5.4.3.5 of the Java Virtual Machine Specification.)
Here is a summary of the correspondence between these factory methods and
the behavior of the resulting method handles:

lookup method behaviors

lookup expression

member

bytecode behavior

lookup.findGetter(C.class,"f",FT.class)

FT f;

(T) this.f;

lookup.findStaticGetter(C.class,"f",FT.class)

static

FT f;

(T) C.f;

lookup.findSetter(C.class,"f",FT.class)

FT f;

this.f = x;

lookup.findStaticSetter(C.class,"f",FT.class)

static

FT f;

C.f = arg;

lookup.findVirtual(C.class,"m",MT)

T m(A*);

(T) this.m(arg*);

lookup.findStatic(C.class,"m",MT)

static

T m(A*);

(T) C.m(arg*);

lookup.findSpecial(C.class,"m",MT,this.class)

T m(A*);

(T) super.m(arg*);

lookup.findConstructor(C.class,MT)

C(A*);

new C(arg*);

lookup.unreflectGetter(aField)

(

static

)?

FT f;

(FT) aField.get(thisOrNull);

lookup.unreflectSetter(aField)

(

static

)?

FT f;

aField.set(thisOrNull, arg);

lookup.unreflect(aMethod)

(

static

)?

T m(A*);

(T) aMethod.invoke(thisOrNull, arg*);

lookup.unreflectConstructor(aConstructor)

C(A*);

(C) aConstructor.newInstance(arg*);

lookup.unreflect(aMethod)

(

static

)?

T m(A*);

(T) aMethod.invoke(thisOrNull, arg*);

lookup.findClass("C")

class C { ... }

C.class;

Here, the type

C

is the class or interface being searched for a member,
documented as a parameter named

refc

in the lookup methods.
The method type

MT

is composed from the return type

T

and the sequence of argument types

A*

.
The constructor also has a sequence of argument types

A*

and
is deemed to return the newly-created object of type

C

.
Both

MT

and the field type

FT

are documented as a parameter named

type

.
The formal parameter

this

stands for the self-reference of type

C

;
if it is present, it is always the leading argument to the method handle invocation.
(In the case of some

protected

members,

this

may be
restricted in type to the lookup class; see below.)
The name

arg

stands for all the other method handle arguments.
In the code examples for the Core Reflection API, the name

thisOrNull

stands for a null reference if the accessed method or field is static,
and

this

otherwise.
The names

aMethod

,

aField

, and

aConstructor

stand
for reflective objects corresponding to the given members.

The bytecode behavior for a

findClass

operation is a load of a constant class,
as if by

ldc CONSTANT_Class

.
The behavior is represented, not as a method handle, but directly as a

Class

constant.

In cases where the given member is of variable arity (i.e., a method or constructor)
the returned method handle will also be of

variable arity

.
In all other cases, the returned method handle will be of fixed arity.

Discussion:

The equivalence between looked-up method handles and underlying
class members and bytecode behaviors
can break down in a few ways:

- If

C

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed, even when there is no equivalent
Java expression or bytecoded constant.

Likewise, if

T

or

MT

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed.
For example, lookups for

MethodHandle.invokeExact

and

MethodHandle.invoke

will always succeed, regardless of requested type.

If there is a security manager installed, it can forbid the lookup
on various grounds (

see below

).
By contrast, the

ldc

instruction on a

CONSTANT_MethodHandle

constant is not subject to security manager checks.

If the looked-up method has a

very large arity

,
the method handle creation may fail, due to the method handle
type having too many parameters.

Access checking

Access checks are applied in the factory methods of

Lookup

,
when a method handle is created.
This is a key difference from the Core Reflection API, since

java.lang.reflect.Method.invoke

performs access checking against every caller, on every call.

All access checks start from a

Lookup

object, which
compares its recorded lookup class against all requests to
create method handles.
A single

Lookup

object can be used to create any number
of access-checked method handles, all checked against a single
lookup class.

A

Lookup

object can be shared with other trusted code,
such as a metaobject protocol.
A shared

Lookup

object delegates the capability
to create method handles on private members of the lookup class.
Even if privileged code uses the

Lookup

object,
the access checking is confined to the privileges of the
original lookup class.

A lookup can fail, because
the containing class is not accessible to the lookup class, or
because the desired class member is missing, or because the
desired class member is not accessible to the lookup class, or
because the lookup object is not trusted enough to access the member.
In any of these cases, a

ReflectiveOperationException

will be
thrown from the attempted lookup. The exact class will be one of
the following:

- NoSuchMethodException — if a method is requested but does not exist

NoSuchFieldException — if a field is requested but does not exist

IllegalAccessException — if the member exists but an access check fails

In general, the conditions under which a method handle may be
looked up for a method

M

are no more restrictive than the conditions
under which the lookup class could have compiled, verified, and resolved a call to

M

.
Where the JVM would raise exceptions like

NoSuchMethodError

,
a method handle lookup will generally raise a corresponding
checked exception, such as

NoSuchMethodException

.
And the effect of invoking the method handle resulting from the lookup
is

exactly equivalent

to executing the compiled, verified, and resolved call to

M

.
The same point is true of fields and constructors.

Discussion:

Access checks only apply to named and reflected methods,
constructors, and fields.
Other method handle creation methods, such as

MethodHandle.asType

,
do not require any access checks, and are used
independently of any

Lookup

object.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

A lookup class which needs to create method handles will call

MethodHandles.lookup

to create a factory for itself.
When the

Lookup

factory object is created, the identity of the lookup class is
determined, and securely stored in the

Lookup

object.
The lookup class (or its delegates) may then use factory methods
on the

Lookup

object to create method handles for access-checked members.
This includes all methods, constructors, and fields which are allowed to the lookup class,
even private ones.

Lookup Factory Methods

The factory methods on a

Lookup

object correspond to all major
use cases for methods, constructors, and fields.
Each method handle created by a factory method is the functional
equivalent of a particular

bytecode behavior

.
(Bytecode behaviors are described in section 5.4.3.5 of the Java Virtual Machine Specification.)
Here is a summary of the correspondence between these factory methods and
the behavior of the resulting method handles:

lookup method behaviors

lookup expression

member

bytecode behavior

lookup.findGetter(C.class,"f",FT.class)

FT f;

(T) this.f;

lookup.findStaticGetter(C.class,"f",FT.class)

static

FT f;

(T) C.f;

lookup.findSetter(C.class,"f",FT.class)

FT f;

this.f = x;

lookup.findStaticSetter(C.class,"f",FT.class)

static

FT f;

C.f = arg;

lookup.findVirtual(C.class,"m",MT)

T m(A*);

(T) this.m(arg*);

lookup.findStatic(C.class,"m",MT)

static

T m(A*);

(T) C.m(arg*);

lookup.findSpecial(C.class,"m",MT,this.class)

T m(A*);

(T) super.m(arg*);

lookup.findConstructor(C.class,MT)

C(A*);

new C(arg*);

lookup.unreflectGetter(aField)

(

static

)?

FT f;

(FT) aField.get(thisOrNull);

lookup.unreflectSetter(aField)

(

static

)?

FT f;

aField.set(thisOrNull, arg);

lookup.unreflect(aMethod)

(

static

)?

T m(A*);

(T) aMethod.invoke(thisOrNull, arg*);

lookup.unreflectConstructor(aConstructor)

C(A*);

(C) aConstructor.newInstance(arg*);

lookup.unreflect(aMethod)

(

static

)?

T m(A*);

(T) aMethod.invoke(thisOrNull, arg*);

lookup.findClass("C")

class C { ... }

C.class;

Here, the type

C

is the class or interface being searched for a member,
documented as a parameter named

refc

in the lookup methods.
The method type

MT

is composed from the return type

T

and the sequence of argument types

A*

.
The constructor also has a sequence of argument types

A*

and
is deemed to return the newly-created object of type

C

.
Both

MT

and the field type

FT

are documented as a parameter named

type

.
The formal parameter

this

stands for the self-reference of type

C

;
if it is present, it is always the leading argument to the method handle invocation.
(In the case of some

protected

members,

this

may be
restricted in type to the lookup class; see below.)
The name

arg

stands for all the other method handle arguments.
In the code examples for the Core Reflection API, the name

thisOrNull

stands for a null reference if the accessed method or field is static,
and

this

otherwise.
The names

aMethod

,

aField

, and

aConstructor

stand
for reflective objects corresponding to the given members.

The bytecode behavior for a

findClass

operation is a load of a constant class,
as if by

ldc CONSTANT_Class

.
The behavior is represented, not as a method handle, but directly as a

Class

constant.

In cases where the given member is of variable arity (i.e., a method or constructor)
the returned method handle will also be of

variable arity

.
In all other cases, the returned method handle will be of fixed arity.

Discussion:

The equivalence between looked-up method handles and underlying
class members and bytecode behaviors
can break down in a few ways:

- If

C

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed, even when there is no equivalent
Java expression or bytecoded constant.

Likewise, if

T

or

MT

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed.
For example, lookups for

MethodHandle.invokeExact

and

MethodHandle.invoke

will always succeed, regardless of requested type.

If there is a security manager installed, it can forbid the lookup
on various grounds (

see below

).
By contrast, the

ldc

instruction on a

CONSTANT_MethodHandle

constant is not subject to security manager checks.

If the looked-up method has a

very large arity

,
the method handle creation may fail, due to the method handle
type having too many parameters.

Access checking

Access checks are applied in the factory methods of

Lookup

,
when a method handle is created.
This is a key difference from the Core Reflection API, since

java.lang.reflect.Method.invoke

performs access checking against every caller, on every call.

All access checks start from a

Lookup

object, which
compares its recorded lookup class against all requests to
create method handles.
A single

Lookup

object can be used to create any number
of access-checked method handles, all checked against a single
lookup class.

A

Lookup

object can be shared with other trusted code,
such as a metaobject protocol.
A shared

Lookup

object delegates the capability
to create method handles on private members of the lookup class.
Even if privileged code uses the

Lookup

object,
the access checking is confined to the privileges of the
original lookup class.

A lookup can fail, because
the containing class is not accessible to the lookup class, or
because the desired class member is missing, or because the
desired class member is not accessible to the lookup class, or
because the lookup object is not trusted enough to access the member.
In any of these cases, a

ReflectiveOperationException

will be
thrown from the attempted lookup. The exact class will be one of
the following:

- NoSuchMethodException — if a method is requested but does not exist

NoSuchFieldException — if a field is requested but does not exist

IllegalAccessException — if the member exists but an access check fails

In general, the conditions under which a method handle may be
looked up for a method

M

are no more restrictive than the conditions
under which the lookup class could have compiled, verified, and resolved a call to

M

.
Where the JVM would raise exceptions like

NoSuchMethodError

,
a method handle lookup will generally raise a corresponding
checked exception, such as

NoSuchMethodException

.
And the effect of invoking the method handle resulting from the lookup
is

exactly equivalent

to executing the compiled, verified, and resolved call to

M

.
The same point is true of fields and constructors.

Discussion:

Access checks only apply to named and reflected methods,
constructors, and fields.
Other method handle creation methods, such as

MethodHandle.asType

,
do not require any access checks, and are used
independently of any

Lookup

object.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

---

#### Lookup Factory Methods

The bytecode behavior for a

findClass

operation is a load of a constant class,
as if by

ldc CONSTANT_Class

.
The behavior is represented, not as a method handle, but directly as a

Class

constant.

In cases where the given member is of variable arity (i.e., a method or constructor)
the returned method handle will also be of

variable arity

.
In all other cases, the returned method handle will be of fixed arity.

Discussion:

The equivalence between looked-up method handles and underlying
class members and bytecode behaviors
can break down in a few ways:

- If

C

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed, even when there is no equivalent
Java expression or bytecoded constant.

Likewise, if

T

or

MT

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed.
For example, lookups for

MethodHandle.invokeExact

and

MethodHandle.invoke

will always succeed, regardless of requested type.

If there is a security manager installed, it can forbid the lookup
on various grounds (

see below

).
By contrast, the

ldc

instruction on a

CONSTANT_MethodHandle

constant is not subject to security manager checks.

If the looked-up method has a

very large arity

,
the method handle creation may fail, due to the method handle
type having too many parameters.

Access checking

Access checks are applied in the factory methods of

Lookup

,
when a method handle is created.
This is a key difference from the Core Reflection API, since

java.lang.reflect.Method.invoke

performs access checking against every caller, on every call.

All access checks start from a

Lookup

object, which
compares its recorded lookup class against all requests to
create method handles.
A single

Lookup

object can be used to create any number
of access-checked method handles, all checked against a single
lookup class.

A

Lookup

object can be shared with other trusted code,
such as a metaobject protocol.
A shared

Lookup

object delegates the capability
to create method handles on private members of the lookup class.
Even if privileged code uses the

Lookup

object,
the access checking is confined to the privileges of the
original lookup class.

A lookup can fail, because
the containing class is not accessible to the lookup class, or
because the desired class member is missing, or because the
desired class member is not accessible to the lookup class, or
because the lookup object is not trusted enough to access the member.
In any of these cases, a

ReflectiveOperationException

will be
thrown from the attempted lookup. The exact class will be one of
the following:

- NoSuchMethodException — if a method is requested but does not exist

NoSuchFieldException — if a field is requested but does not exist

IllegalAccessException — if the member exists but an access check fails

In general, the conditions under which a method handle may be
looked up for a method

M

are no more restrictive than the conditions
under which the lookup class could have compiled, verified, and resolved a call to

M

.
Where the JVM would raise exceptions like

NoSuchMethodError

,
a method handle lookup will generally raise a corresponding
checked exception, such as

NoSuchMethodException

.
And the effect of invoking the method handle resulting from the lookup
is

exactly equivalent

to executing the compiled, verified, and resolved call to

M

.
The same point is true of fields and constructors.

Discussion:

Access checks only apply to named and reflected methods,
constructors, and fields.
Other method handle creation methods, such as

MethodHandle.asType

,
do not require any access checks, and are used
independently of any

Lookup

object.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

In cases where the given member is of variable arity (i.e., a method or constructor)
the returned method handle will also be of

variable arity

.
In all other cases, the returned method handle will be of fixed arity.

Discussion:

The equivalence between looked-up method handles and underlying
class members and bytecode behaviors
can break down in a few ways:

- If

C

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed, even when there is no equivalent
Java expression or bytecoded constant.

Likewise, if

T

or

MT

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed.
For example, lookups for

MethodHandle.invokeExact

and

MethodHandle.invoke

will always succeed, regardless of requested type.

If there is a security manager installed, it can forbid the lookup
on various grounds (

see below

).
By contrast, the

ldc

instruction on a

CONSTANT_MethodHandle

constant is not subject to security manager checks.

If the looked-up method has a

very large arity

,
the method handle creation may fail, due to the method handle
type having too many parameters.

Access checking

Access checks are applied in the factory methods of

Lookup

,
when a method handle is created.
This is a key difference from the Core Reflection API, since

java.lang.reflect.Method.invoke

performs access checking against every caller, on every call.

All access checks start from a

Lookup

object, which
compares its recorded lookup class against all requests to
create method handles.
A single

Lookup

object can be used to create any number
of access-checked method handles, all checked against a single
lookup class.

A

Lookup

object can be shared with other trusted code,
such as a metaobject protocol.
A shared

Lookup

object delegates the capability
to create method handles on private members of the lookup class.
Even if privileged code uses the

Lookup

object,
the access checking is confined to the privileges of the
original lookup class.

A lookup can fail, because
the containing class is not accessible to the lookup class, or
because the desired class member is missing, or because the
desired class member is not accessible to the lookup class, or
because the lookup object is not trusted enough to access the member.
In any of these cases, a

ReflectiveOperationException

will be
thrown from the attempted lookup. The exact class will be one of
the following:

- NoSuchMethodException — if a method is requested but does not exist

NoSuchFieldException — if a field is requested but does not exist

IllegalAccessException — if the member exists but an access check fails

In general, the conditions under which a method handle may be
looked up for a method

M

are no more restrictive than the conditions
under which the lookup class could have compiled, verified, and resolved a call to

M

.
Where the JVM would raise exceptions like

NoSuchMethodError

,
a method handle lookup will generally raise a corresponding
checked exception, such as

NoSuchMethodException

.
And the effect of invoking the method handle resulting from the lookup
is

exactly equivalent

to executing the compiled, verified, and resolved call to

M

.
The same point is true of fields and constructors.

Discussion:

Access checks only apply to named and reflected methods,
constructors, and fields.
Other method handle creation methods, such as

MethodHandle.asType

,
do not require any access checks, and are used
independently of any

Lookup

object.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

Discussion:

The equivalence between looked-up method handles and underlying
class members and bytecode behaviors
can break down in a few ways:

- If

C

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed, even when there is no equivalent
Java expression or bytecoded constant.

Likewise, if

T

or

MT

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed.
For example, lookups for

MethodHandle.invokeExact

and

MethodHandle.invoke

will always succeed, regardless of requested type.

If there is a security manager installed, it can forbid the lookup
on various grounds (

see below

).
By contrast, the

ldc

instruction on a

CONSTANT_MethodHandle

constant is not subject to security manager checks.

If the looked-up method has a

very large arity

,
the method handle creation may fail, due to the method handle
type having too many parameters.

Access checking

Access checks are applied in the factory methods of

Lookup

,
when a method handle is created.
This is a key difference from the Core Reflection API, since

java.lang.reflect.Method.invoke

performs access checking against every caller, on every call.

All access checks start from a

Lookup

object, which
compares its recorded lookup class against all requests to
create method handles.
A single

Lookup

object can be used to create any number
of access-checked method handles, all checked against a single
lookup class.

A

Lookup

object can be shared with other trusted code,
such as a metaobject protocol.
A shared

Lookup

object delegates the capability
to create method handles on private members of the lookup class.
Even if privileged code uses the

Lookup

object,
the access checking is confined to the privileges of the
original lookup class.

A lookup can fail, because
the containing class is not accessible to the lookup class, or
because the desired class member is missing, or because the
desired class member is not accessible to the lookup class, or
because the lookup object is not trusted enough to access the member.
In any of these cases, a

ReflectiveOperationException

will be
thrown from the attempted lookup. The exact class will be one of
the following:

- NoSuchMethodException — if a method is requested but does not exist

NoSuchFieldException — if a field is requested but does not exist

IllegalAccessException — if the member exists but an access check fails

In general, the conditions under which a method handle may be
looked up for a method

M

are no more restrictive than the conditions
under which the lookup class could have compiled, verified, and resolved a call to

M

.
Where the JVM would raise exceptions like

NoSuchMethodError

,
a method handle lookup will generally raise a corresponding
checked exception, such as

NoSuchMethodException

.
And the effect of invoking the method handle resulting from the lookup
is

exactly equivalent

to executing the compiled, verified, and resolved call to

M

.
The same point is true of fields and constructors.

Discussion:

Access checks only apply to named and reflected methods,
constructors, and fields.
Other method handle creation methods, such as

MethodHandle.asType

,
do not require any access checks, and are used
independently of any

Lookup

object.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

If

C

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed, even when there is no equivalent
Java expression or bytecoded constant.

Likewise, if

T

or

MT

is not symbolically accessible from the lookup class's loader,
the lookup can still succeed.
For example, lookups for

MethodHandle.invokeExact

and

MethodHandle.invoke

will always succeed, regardless of requested type.

If there is a security manager installed, it can forbid the lookup
on various grounds (

see below

).
By contrast, the

ldc

instruction on a

CONSTANT_MethodHandle

constant is not subject to security manager checks.

If the looked-up method has a

very large arity

,
the method handle creation may fail, due to the method handle
type having too many parameters.

---

#### Access checking

All access checks start from a

Lookup

object, which
compares its recorded lookup class against all requests to
create method handles.
A single

Lookup

object can be used to create any number
of access-checked method handles, all checked against a single
lookup class.

A

Lookup

object can be shared with other trusted code,
such as a metaobject protocol.
A shared

Lookup

object delegates the capability
to create method handles on private members of the lookup class.
Even if privileged code uses the

Lookup

object,
the access checking is confined to the privileges of the
original lookup class.

A lookup can fail, because
the containing class is not accessible to the lookup class, or
because the desired class member is missing, or because the
desired class member is not accessible to the lookup class, or
because the lookup object is not trusted enough to access the member.
In any of these cases, a

ReflectiveOperationException

will be
thrown from the attempted lookup. The exact class will be one of
the following:

- NoSuchMethodException — if a method is requested but does not exist

NoSuchFieldException — if a field is requested but does not exist

IllegalAccessException — if the member exists but an access check fails

In general, the conditions under which a method handle may be
looked up for a method

M

are no more restrictive than the conditions
under which the lookup class could have compiled, verified, and resolved a call to

M

.
Where the JVM would raise exceptions like

NoSuchMethodError

,
a method handle lookup will generally raise a corresponding
checked exception, such as

NoSuchMethodException

.
And the effect of invoking the method handle resulting from the lookup
is

exactly equivalent

to executing the compiled, verified, and resolved call to

M

.
The same point is true of fields and constructors.

Discussion:

Access checks only apply to named and reflected methods,
constructors, and fields.
Other method handle creation methods, such as

MethodHandle.asType

,
do not require any access checks, and are used
independently of any

Lookup

object.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

A

Lookup

object can be shared with other trusted code,
such as a metaobject protocol.
A shared

Lookup

object delegates the capability
to create method handles on private members of the lookup class.
Even if privileged code uses the

Lookup

object,
the access checking is confined to the privileges of the
original lookup class.

A lookup can fail, because
the containing class is not accessible to the lookup class, or
because the desired class member is missing, or because the
desired class member is not accessible to the lookup class, or
because the lookup object is not trusted enough to access the member.
In any of these cases, a

ReflectiveOperationException

will be
thrown from the attempted lookup. The exact class will be one of
the following:

- NoSuchMethodException — if a method is requested but does not exist

NoSuchFieldException — if a field is requested but does not exist

IllegalAccessException — if the member exists but an access check fails

In general, the conditions under which a method handle may be
looked up for a method

M

are no more restrictive than the conditions
under which the lookup class could have compiled, verified, and resolved a call to

M

.
Where the JVM would raise exceptions like

NoSuchMethodError

,
a method handle lookup will generally raise a corresponding
checked exception, such as

NoSuchMethodException

.
And the effect of invoking the method handle resulting from the lookup
is

exactly equivalent

to executing the compiled, verified, and resolved call to

M

.
The same point is true of fields and constructors.

Discussion:

Access checks only apply to named and reflected methods,
constructors, and fields.
Other method handle creation methods, such as

MethodHandle.asType

,
do not require any access checks, and are used
independently of any

Lookup

object.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

A lookup can fail, because
the containing class is not accessible to the lookup class, or
because the desired class member is missing, or because the
desired class member is not accessible to the lookup class, or
because the lookup object is not trusted enough to access the member.
In any of these cases, a

ReflectiveOperationException

will be
thrown from the attempted lookup. The exact class will be one of
the following:

- NoSuchMethodException — if a method is requested but does not exist

NoSuchFieldException — if a field is requested but does not exist

IllegalAccessException — if the member exists but an access check fails

In general, the conditions under which a method handle may be
looked up for a method

M

are no more restrictive than the conditions
under which the lookup class could have compiled, verified, and resolved a call to

M

.
Where the JVM would raise exceptions like

NoSuchMethodError

,
a method handle lookup will generally raise a corresponding
checked exception, such as

NoSuchMethodException

.
And the effect of invoking the method handle resulting from the lookup
is

exactly equivalent

to executing the compiled, verified, and resolved call to

M

.
The same point is true of fields and constructors.

Discussion:

Access checks only apply to named and reflected methods,
constructors, and fields.
Other method handle creation methods, such as

MethodHandle.asType

,
do not require any access checks, and are used
independently of any

Lookup

object.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

NoSuchMethodException — if a method is requested but does not exist

NoSuchFieldException — if a field is requested but does not exist

IllegalAccessException — if the member exists but an access check fails

In general, the conditions under which a method handle may be
looked up for a method

M

are no more restrictive than the conditions
under which the lookup class could have compiled, verified, and resolved a call to

M

.
Where the JVM would raise exceptions like

NoSuchMethodError

,
a method handle lookup will generally raise a corresponding
checked exception, such as

NoSuchMethodException

.
And the effect of invoking the method handle resulting from the lookup
is

exactly equivalent

to executing the compiled, verified, and resolved call to

M

.
The same point is true of fields and constructors.

Discussion:

Access checks only apply to named and reflected methods,
constructors, and fields.
Other method handle creation methods, such as

MethodHandle.asType

,
do not require any access checks, and are used
independently of any

Lookup

object.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

Discussion:

Access checks only apply to named and reflected methods,
constructors, and fields.
Other method handle creation methods, such as

MethodHandle.asType

,
do not require any access checks, and are used
independently of any

Lookup

object.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

If the desired member is

protected

, the usual JVM rules apply,
including the requirement that the lookup class must be either be in the
same package as the desired member, or must inherit that member.
(See the Java Virtual Machine Specification, sections 4.9.2, 5.4.3.5, and 6.4.)
In addition, if the desired member is a non-static field or method
in a different package, the resulting method handle may only be applied
to objects of the lookup class or one of its subclasses.
This requirement is enforced by narrowing the type of the leading

this

parameter from

C

(which will necessarily be a superclass of the lookup class)
to the lookup class itself.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

The JVM imposes a similar requirement on

invokespecial

instruction,
that the receiver argument must match both the resolved method

and

the current class. Again, this requirement is enforced by narrowing the
type of the leading parameter to the resulting method handle.
(See the Java Virtual Machine Specification, section 4.10.1.9.)

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

The JVM represents constructors and static initializer blocks as internal methods
with special names (

"<init>"

and

"<clinit>"

).
The internal syntax of invocation instructions allows them to refer to such internal
methods as if they were normal methods, but the JVM bytecode verifier rejects them.
A lookup of such an internal method will produce a

NoSuchMethodException

.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

If the relationship between nested types is expressed directly through the

NestHost

and

NestMembers

attributes
(see the Java Virtual Machine Specification, sections 4.7.28 and 4.7.29),
then the associated

Lookup

object provides direct access to
the lookup class and all of its nestmates
(see

Class.getNestHost

).
Otherwise, access between nested classes is obtained by the Java compiler creating
a wrapper method to access a private method of another class in the same nest.
For example, a nested class

C.D

can access private members within other related classes such as

C

,

C.D.E

, or

C.B

,
but the Java compiler may need to generate wrapper methods in
those related classes. In such cases, a

Lookup

object on

C.E

would be unable to access those private members.
A workaround for this limitation is the

Lookup.in

method,
which can transform a lookup on

C.E

into one on any of those other
classes, without special elevation of privilege.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

The accesses permitted to a given lookup object may be limited,
according to its set of

lookupModes

,
to a subset of members normally accessible to the lookup class.
For example, the

publicLookup

method produces a lookup object which is only allowed to access
public members in public classes of exported packages.
The caller sensitive method

lookup

produces a lookup object with full capabilities relative to
its caller class, to emulate all supported bytecode behaviors.
Also, the

Lookup.in

method may produce a lookup object
with fewer access modes than the original lookup object.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

Discussion of private access:

We say that a lookup has

private access

if its

lookup modes

include the possibility of accessing

private

members
(which includes the private members of nestmates).
As documented in the relevant methods elsewhere,
only lookups with private access possess the following capabilities:

- access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

access private fields, methods, and constructors of the lookup class and its nestmates

create method handles which invoke

caller sensitive

methods,
such as

Class.forName

create method handles which

emulate invokespecial

instructions

avoid

package access checks

for classes accessible to the lookup class

create

delegated lookup objects

which have private access to other classes
within the same package member

Each of these permissions is a consequence of the fact that a lookup object
with private access can be securely traced back to an originating class,
whose

bytecode behaviors

and Java language access permissions
can be reliably determined and emulated by method handles.

Security manager interactions

Although bytecode instructions can only refer to classes in
a related class loader, this API can search for methods in any
class, as long as a reference to its

Class

object is
available. Such cross-loader references are also possible with the
Core Reflection API, and are impossible to bytecode instructions
such as

invokestatic

or

getfield

.
There is a

security manager API

to allow applications to check such cross-loader references.
These checks apply to both the

MethodHandles.Lookup

API
and the Core Reflection API
(as found on

Class

).

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

---

#### Security manager interactions

If a security manager is present, member and class lookups are subject to
additional checks.
From one to three calls are made to the security manager.
Any of these calls can refuse access by throwing a

SecurityException

.
Define

smgr

as the security manager,

lookc

as the lookup class of the current lookup object,

refc

as the containing class in which the member
is being sought, and

defc

as the class in which the
member is actually defined.
(If a class or other type is being accessed,
the

refc

and

defc

values are the class itself.)
The value

lookc

is defined as

not present

if the current lookup object does not have

private access

.
The calls are made according to the following rules:

- Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

Security checks are performed after other access checks have passed.
Therefore, the above rules presuppose a member or class that is public,
or else that is being accessed from a lookup class that has
rights to access the member or class.

Caller sensitive methods

A small number of Java methods have a special property called caller sensitivity.
A

caller-sensitive

method can behave differently depending on the
identity of its immediate caller.

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

Step 1:

If

lookc

is not present, or if its class loader is not
the same as or an ancestor of the class loader of

refc

,
then

smgr.checkPackageAccess(refcPkg)

is called,
where

refcPkg

is the package of

refc

.

Step 2a:

If the retrieved member is not public and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("accessDeclaredMembers")

is called.

Step 2b:

If the retrieved class has a

null

class loader,
and

lookc

is not present, then

smgr.checkPermission

with

RuntimePermission("getClassLoader")

is called.

Step 3:

If the retrieved member is not public,
and if

lookc

is not present,
and if

defc

and

refc

are different,
then

smgr.checkPackageAccess(defcPkg)

is called,
where

defcPkg

is the package of

defc

.

---

#### Caller sensitive methods

If a method handle for a caller-sensitive method is requested,
the general rules for

bytecode behaviors

apply,
but they take account of the lookup class in a special way.
The resulting method handle behaves as if it were called
from an instruction contained in the lookup class,
so that the caller-sensitive method detects the lookup class.
(By contrast, the invoker of the method handle is disregarded.)
Thus, in the case of caller-sensitive methods,
different lookup classes may give rise to
differently behaving method handles.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

In cases where the lookup object is

publicLookup()

,
or some other lookup object without

private access

,
the lookup class is disregarded.
In such cases, no caller-sensitive method handle can be created,
access is forbidden, and the lookup fails with an

IllegalAccessException

.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

Discussion:

For example, the caller-sensitive method

Class.forName(x)

can return varying classes or throw varying exceptions,
depending on the class loader of the class that calls it.
A public lookup of

Class.forName

will fail, because
there is no reasonable way to determine its bytecode behavior.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

If an application caches method handles for broad sharing,
it should use

publicLookup()

to create them.
If there is a lookup of

Class.forName

, it will fail,
and the application must take appropriate action in that case.
It may be that a later lookup, perhaps during the invocation of a
bootstrap method, can incorporate the specific identity
of the caller, making the method accessible.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

The function

MethodHandles.lookup

is caller sensitive
so that there can be a secure foundation for lookups.
Nearly all other methods in the JSR 292 API rely on lookup
objects to check access requests.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

MODULE

A single-bit mask representing

module

access (default access),
which may contribute to the result of

lookupModes

.

static int

PACKAGE

A single-bit mask representing

package

access (default access),
which may contribute to the result of

lookupModes

.

static int

PRIVATE

A single-bit mask representing

private

access,
which may contribute to the result of

lookupModes

.

static int

PROTECTED

A single-bit mask representing

protected

access,
which may contribute to the result of

lookupModes

.

static int

PUBLIC

A single-bit mask representing

public

access,
which may contribute to the result of

lookupModes

.

static int

UNCONDITIONAL

A single-bit mask representing

unconditional

access
which may contribute to the result of

lookupModes

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

accessClass

​(

Class

<?> targetClass)

Determines if a class can be accessed from the lookup context defined by this

Lookup

object.

MethodHandle

bind

​(

Object

receiver,

String

name,

MethodType

type)

Produces an early-bound method handle for a non-static method.

Class

<?>

defineClass

​(byte[] bytes)

Defines a class to the same class loader and in the same runtime package and

protection domain

as this lookup's

lookup class

.

MethodHandles.Lookup

dropLookupMode

​(int modeToDrop)

Creates a lookup on the same lookup class which this lookup object
finds members, but with a lookup mode that has lost the given lookup mode.

Class

<?>

findClass

​(

String

targetName)

Looks up a class by name from the lookup context defined by this

Lookup

object.

MethodHandle

findConstructor

​(

Class

<?> refc,

MethodType

type)

Produces a method handle which creates an object and initializes it, using
the constructor of the specified type.

MethodHandle

findGetter

​(

Class

<?> refc,

String

name,

Class

<?> type)

Produces a method handle giving read access to a non-static field.

MethodHandle

findSetter

​(

Class

<?> refc,

String

name,

Class

<?> type)

Produces a method handle giving write access to a non-static field.

MethodHandle

findSpecial

​(

Class

<?> refc,

String

name,

MethodType

type,

Class

<?> specialCaller)

Produces an early-bound method handle for a virtual method.

MethodHandle

findStatic

​(

Class

<?> refc,

String

name,

MethodType

type)

Produces a method handle for a static method.

MethodHandle

findStaticGetter

​(

Class

<?> refc,

String

name,

Class

<?> type)

Produces a method handle giving read access to a static field.

MethodHandle

findStaticSetter

​(

Class

<?> refc,

String

name,

Class

<?> type)

Produces a method handle giving write access to a static field.

VarHandle

findStaticVarHandle

​(

Class

<?> decl,

String

name,

Class

<?> type)

Produces a VarHandle giving access to a static field

name

of
type

type

declared in a class of type

decl

.

VarHandle

findVarHandle

​(

Class

<?> recv,

String

name,

Class

<?> type)

Produces a VarHandle giving access to a non-static field

name

of type

type

declared in a class of type

recv

.

MethodHandle

findVirtual

​(

Class

<?> refc,

String

name,

MethodType

type)

Produces a method handle for a virtual method.

boolean

hasPrivateAccess

()

Returns

true

if this lookup has

PRIVATE

access.

MethodHandles.Lookup

in

​(

Class

<?> requestedLookupClass)

Creates a lookup on the specified new lookup class.

Class

<?>

lookupClass

()

Tells which class is performing the lookup.

int

lookupModes

()

Tells which access-protection classes of members this lookup object can produce.

MethodHandleInfo

revealDirect

​(

MethodHandle

target)

Cracks a

direct method handle

created by this lookup object or a similar one.

String

toString

()

Displays the name of the class from which lookups are to be made.

MethodHandle

unreflect

​(

Method

m)

Makes a

direct method handle

to

m

, if the lookup class has permission.

MethodHandle

unreflectConstructor

​(

Constructor

<?> c)

Produces a method handle for a reflected constructor.

MethodHandle

unreflectGetter

​(

Field

f)

Produces a method handle giving read access to a reflected field.

MethodHandle

unreflectSetter

​(

Field

f)

Produces a method handle giving write access to a reflected field.

MethodHandle

unreflectSpecial

​(

Method

m,

Class

<?> specialCaller)

Produces a method handle for a reflected method.

VarHandle

unreflectVarHandle

​(

Field

f)

Produces a VarHandle giving access to a reflected field

f

of type

T

declared in a class of type

R

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

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

static int

MODULE

A single-bit mask representing

module

access (default access),
which may contribute to the result of

lookupModes

.

static int

PACKAGE

A single-bit mask representing

package

access (default access),
which may contribute to the result of

lookupModes

.

static int

PRIVATE

A single-bit mask representing

private

access,
which may contribute to the result of

lookupModes

.

static int

PROTECTED

A single-bit mask representing

protected

access,
which may contribute to the result of

lookupModes

.

static int

PUBLIC

A single-bit mask representing

public

access,
which may contribute to the result of

lookupModes

.

static int

UNCONDITIONAL

A single-bit mask representing

unconditional

access
which may contribute to the result of

lookupModes

.

---

#### Field Summary

A single-bit mask representing

module

access (default access),
which may contribute to the result of

lookupModes

.

A single-bit mask representing

package

access (default access),
which may contribute to the result of

lookupModes

.

A single-bit mask representing

private

access,
which may contribute to the result of

lookupModes

.

A single-bit mask representing

protected

access,
which may contribute to the result of

lookupModes

.

A single-bit mask representing

public

access,
which may contribute to the result of

lookupModes

.

A single-bit mask representing

unconditional

access
which may contribute to the result of

lookupModes

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

accessClass

​(

Class

<?> targetClass)

Determines if a class can be accessed from the lookup context defined by this

Lookup

object.

MethodHandle

bind

​(

Object

receiver,

String

name,

MethodType

type)

Produces an early-bound method handle for a non-static method.

Class

<?>

defineClass

​(byte[] bytes)

Defines a class to the same class loader and in the same runtime package and

protection domain

as this lookup's

lookup class

.

MethodHandles.Lookup

dropLookupMode

​(int modeToDrop)

Creates a lookup on the same lookup class which this lookup object
finds members, but with a lookup mode that has lost the given lookup mode.

Class

<?>

findClass

​(

String

targetName)

Looks up a class by name from the lookup context defined by this

Lookup

object.

MethodHandle

findConstructor

​(

Class

<?> refc,

MethodType

type)

Produces a method handle which creates an object and initializes it, using
the constructor of the specified type.

MethodHandle

findGetter

​(

Class

<?> refc,

String

name,

Class

<?> type)

Produces a method handle giving read access to a non-static field.

MethodHandle

findSetter

​(

Class

<?> refc,

String

name,

Class

<?> type)

Produces a method handle giving write access to a non-static field.

MethodHandle

findSpecial

​(

Class

<?> refc,

String

name,

MethodType

type,

Class

<?> specialCaller)

Produces an early-bound method handle for a virtual method.

MethodHandle

findStatic

​(

Class

<?> refc,

String

name,

MethodType

type)

Produces a method handle for a static method.

MethodHandle

findStaticGetter

​(

Class

<?> refc,

String

name,

Class

<?> type)

Produces a method handle giving read access to a static field.

MethodHandle

findStaticSetter

​(

Class

<?> refc,

String

name,

Class

<?> type)

Produces a method handle giving write access to a static field.

VarHandle

findStaticVarHandle

​(

Class

<?> decl,

String

name,

Class

<?> type)

Produces a VarHandle giving access to a static field

name

of
type

type

declared in a class of type

decl

.

VarHandle

findVarHandle

​(

Class

<?> recv,

String

name,

Class

<?> type)

Produces a VarHandle giving access to a non-static field

name

of type

type

declared in a class of type

recv

.

MethodHandle

findVirtual

​(

Class

<?> refc,

String

name,

MethodType

type)

Produces a method handle for a virtual method.

boolean

hasPrivateAccess

()

Returns

true

if this lookup has

PRIVATE

access.

MethodHandles.Lookup

in

​(

Class

<?> requestedLookupClass)

Creates a lookup on the specified new lookup class.

Class

<?>

lookupClass

()

Tells which class is performing the lookup.

int

lookupModes

()

Tells which access-protection classes of members this lookup object can produce.

MethodHandleInfo

revealDirect

​(

MethodHandle

target)

Cracks a

direct method handle

created by this lookup object or a similar one.

String

toString

()

Displays the name of the class from which lookups are to be made.

MethodHandle

unreflect

​(

Method

m)

Makes a

direct method handle

to

m

, if the lookup class has permission.

MethodHandle

unreflectConstructor

​(

Constructor

<?> c)

Produces a method handle for a reflected constructor.

MethodHandle

unreflectGetter

​(

Field

f)

Produces a method handle giving read access to a reflected field.

MethodHandle

unreflectSetter

​(

Field

f)

Produces a method handle giving write access to a reflected field.

MethodHandle

unreflectSpecial

​(

Method

m,

Class

<?> specialCaller)

Produces a method handle for a reflected method.

VarHandle

unreflectVarHandle

​(

Field

f)

Produces a VarHandle giving access to a reflected field

f

of type

T

declared in a class of type

R

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

wait

,

wait

,

wait

---

#### Method Summary

Determines if a class can be accessed from the lookup context defined by this

Lookup

object.

Produces an early-bound method handle for a non-static method.

Defines a class to the same class loader and in the same runtime package and

protection domain

as this lookup's

lookup class

.

Creates a lookup on the same lookup class which this lookup object
finds members, but with a lookup mode that has lost the given lookup mode.

Looks up a class by name from the lookup context defined by this

Lookup

object.

Produces a method handle which creates an object and initializes it, using
the constructor of the specified type.

Produces a method handle giving read access to a non-static field.

Produces a method handle giving write access to a non-static field.

Produces an early-bound method handle for a virtual method.

Produces a method handle for a static method.

Produces a method handle giving read access to a static field.

Produces a method handle giving write access to a static field.

Produces a VarHandle giving access to a static field

name

of
type

type

declared in a class of type

decl

.

Produces a VarHandle giving access to a non-static field

name

of type

type

declared in a class of type

recv

.

Produces a method handle for a virtual method.

Returns

true

if this lookup has

PRIVATE

access.

Creates a lookup on the specified new lookup class.

Tells which class is performing the lookup.

Tells which access-protection classes of members this lookup object can produce.

Cracks a

direct method handle

created by this lookup object or a similar one.

Displays the name of the class from which lookups are to be made.

Makes a

direct method handle

to

m

, if the lookup class has permission.

Produces a method handle for a reflected constructor.

Produces a method handle giving read access to a reflected field.

Produces a method handle giving write access to a reflected field.

Produces a method handle for a reflected method.

Produces a VarHandle giving access to a reflected field

f

of type

T

declared in a class of type

R

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- PUBLIC

```java
public static final int PUBLIC
```

A single-bit mask representing

public

access,
which may contribute to the result of

lookupModes

.
The value,

0x01

, happens to be the same as the value of the

public

modifier bit

.

**See Also:** Constant Field Values

- PRIVATE

```java
public static final int PRIVATE
```

A single-bit mask representing

private

access,
which may contribute to the result of

lookupModes

.
The value,

0x02

, happens to be the same as the value of the

private

modifier bit

.

**See Also:** Constant Field Values

- PROTECTED

```java
public static final int PROTECTED
```

A single-bit mask representing

protected

access,
which may contribute to the result of

lookupModes

.
The value,

0x04

, happens to be the same as the value of the

protected

modifier bit

.

**See Also:** Constant Field Values

- PACKAGE

```java
public static final int PACKAGE
```

A single-bit mask representing

package

access (default access),
which may contribute to the result of

lookupModes

.
The value is

0x08

, which does not correspond meaningfully to
any particular

modifier bit

.

**See Also:** Constant Field Values

- MODULE

```java
public static final int MODULE
```

A single-bit mask representing

module

access (default access),
which may contribute to the result of

lookupModes

.
The value is

0x10

, which does not correspond meaningfully to
any particular

modifier bit

.
In conjunction with the

PUBLIC

modifier bit, a

Lookup

with this lookup mode can access all public types in the module of the
lookup class and public types in packages exported by other modules
to the module of the lookup class.

**Since:** 9
**See Also:** Constant Field Values

- UNCONDITIONAL

```java
public static final int UNCONDITIONAL
```

A single-bit mask representing

unconditional

access
which may contribute to the result of

lookupModes

.
The value is

0x20

, which does not correspond meaningfully to
any particular

modifier bit

.
A

Lookup

with this lookup mode assumes

readability

.
In conjunction with the

PUBLIC

modifier bit, a

Lookup

with this lookup mode can access all public members of public types
of all modules where the type is in a package that is

exported unconditionally

.

**Since:** 9
**See Also:** MethodHandles.publicLookup()

,

Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- lookupClass

```java
public
Class
<?> lookupClass()
```

Tells which class is performing the lookup. It is this class against
which checks are performed for visibility and access permissions.

The class implies a maximum level of access permission,
but the permissions may be additionally limited by the bitmask

lookupModes

, which controls whether non-public members
can be accessed.

**Returns:** the lookup class, on behalf of which this lookup object finds members

- lookupModes

```java
public int lookupModes()
```

Tells which access-protection classes of members this lookup object can produce.
The result is a bit-mask of the bits

PUBLIC (0x01)

,

PRIVATE (0x02)

,

PROTECTED (0x04)

,

PACKAGE (0x08)

,

MODULE (0x10)

,
and

UNCONDITIONAL (0x20)

.

A freshly-created lookup object
on the

caller's class

has
all possible bits set, except

UNCONDITIONAL

.
A lookup object on a new lookup class

created from a previous lookup object

may have some mode bits set to zero.
Mode bits can also be

directly cleared

.
Once cleared, mode bits cannot be restored from the downgraded lookup object.
The purpose of this is to restrict access via the new lookup object,
so that it can access only names which can be reached by the original
lookup object, and also by the new lookup class.

**Returns:** the lookup modes, which limit the kinds of access performed by this lookup object
**See Also:** in(java.lang.Class<?>)

,

dropLookupMode(int)

- in

```java
public
MethodHandles.Lookup
in​(
Class
<?> requestedLookupClass)
```

Creates a lookup on the specified new lookup class.
The resulting object will report the specified
class as its own

lookupClass

.

However, the resulting

Lookup

object is guaranteed
to have no more access capabilities than the original.
In particular, access capabilities can be lost as follows:

- If the old lookup class is in a

named

module, and
the new lookup class is in a different module

M

, then no members, not
even public members in

M

's exported packages, will be accessible.
The exception to this is when this lookup is

publicLookup

, in which case

PUBLIC

access is not lost.

If the old lookup class is in an unnamed module, and the new lookup class
is a different module then

MODULE

access is lost.

If the new lookup class differs from the old one then

UNCONDITIONAL

is lost.

If the new lookup class is in a different package
than the old one, protected and default (package) members will not be accessible.

If the new lookup class is not within the same package member
as the old one, private members will not be accessible, and protected members
will not be accessible by virtue of inheritance.
(Protected members may continue to be accessible because of package sharing.)

If the new lookup class is not accessible to the old lookup class,
then no members, not even public members, will be accessible.
(In all other cases, public members will continue to be accessible.)

The resulting lookup's capabilities for loading classes
(used during

findClass(java.lang.String)

invocations)
are determined by the lookup class' loader,
which may change due to this operation.

**Parameters:** requestedLookupClass

- the desired lookup class for the new lookup object
**Returns:** a lookup object which reports the desired lookup class, or the same object
if there is no change
**Throws:** NullPointerException

- if the argument is null

- dropLookupMode

```java
public
MethodHandles.Lookup
dropLookupMode​(int modeToDrop)
```

Creates a lookup on the same lookup class which this lookup object
finds members, but with a lookup mode that has lost the given lookup mode.
The lookup mode to drop is one of

PUBLIC

,

MODULE

,

PACKAGE

,

PROTECTED

or

PRIVATE

.

PROTECTED

and

UNCONDITIONAL

are always
dropped and so the resulting lookup mode will never have these access capabilities.
When dropping

PACKAGE

then the resulting lookup will not have

PACKAGE

or

PRIVATE

access. When dropping

MODULE

then the resulting lookup will
not have

MODULE

,

PACKAGE

, or

PRIVATE

access. If

PUBLIC

is dropped then the resulting lookup has no access.

**Parameters:** modeToDrop

- the lookup mode to drop
**Returns:** a lookup object which lacks the indicated mode, or the same object if there is no change
**Throws:** IllegalArgumentException

- if

modeToDrop

is not one of

PUBLIC

,

MODULE

,

PACKAGE

,

PROTECTED

,

PRIVATE

or

UNCONDITIONAL
**Since:** 9
**See Also:** MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

- defineClass

```java
public
Class
<?> defineClass​(byte[] bytes)
throws
IllegalAccessException
```

Defines a class to the same class loader and in the same runtime package and

protection domain

as this lookup's

lookup class

.

The

lookup modes

for this lookup must include

PACKAGE

access as default (package) members will be
accessible to the class. The

PACKAGE

lookup mode serves to authenticate
that the lookup object was created by a caller in the runtime package (or derived
from a lookup originally created by suitably privileged code to a target class in
the runtime package).

The

bytes

parameter is the class bytes of a valid class file (as defined
by the

The Java Virtual Machine Specification

) with a class name in the
same package as the lookup class.

This method does not run the class initializer. The class initializer may
run at a later time, as detailed in section 12.4 of the

The Java Language
Specification

.

If there is a security manager, its

checkPermission

method is first called
to check

RuntimePermission("defineClass")

.

**Parameters:** bytes

- the class bytes
**Returns:** the

Class

object for the class
**Throws:** IllegalArgumentException

- the bytes are for a class in a different package
to the lookup class
**Throws:** IllegalAccessException

- if this lookup does not have

PACKAGE

access
**Throws:** LinkageError

- if the class is malformed (

ClassFormatError

), cannot be
verified (

VerifyError

), is already defined, or another linkage error occurs
**Throws:** SecurityException

- if denied by the security manager
**Throws:** NullPointerException

- if

bytes

is

null
**Since:** 9
**See Also:** MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

,

dropLookupMode(int)

,

ClassLoader.defineClass(String,byte[],int,int,ProtectionDomain)

- toString

```java
public
String
toString()
```

Displays the name of the class from which lookups are to be made.
(The name is the one reported by

Class.getName

.)
If there are restrictions on the access permitted to this lookup,
this is indicated by adding a suffix to the class name, consisting
of a slash and a keyword. The keyword represents the strongest
allowed access, and is chosen as follows:

- If no access is allowed, the suffix is "/noaccess".

If only public access to types in exported packages is allowed, the suffix is "/public".

If only public access and unconditional access are allowed, the suffix is "/publicLookup".

If only public and module access are allowed, the suffix is "/module".

If only public, module and package access are allowed, the suffix is "/package".

If only public, module, package, and private access are allowed, the suffix is "/private".

If none of the above cases apply, it is the case that full
access (public, module, package, private, and protected) is allowed.
In this case, no suffix is added.
This is true only of an object obtained originally from

MethodHandles.lookup

.
Objects created by

Lookup.in

always have restricted access, and will display a suffix.

(It may seem strange that protected access should be
stronger than private access. Viewed independently from
package access, protected access is the first to be lost,
because it requires a direct subclass relationship between
caller and callee.)

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.
**See Also:** in(java.lang.Class<?>)

- findStatic

```java
public
MethodHandle
findStatic​(
Class
<?> refc,

String
name,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces a method handle for a static method.
The type of the method handle will be that of the method.
(Since static methods do not take receivers, there is no
additional receiver argument inserted into the method handle type,
as there would be with

findVirtual

or

findSpecial

.)
The method and all its argument types must be accessible to the lookup object.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_asList = publicLookup().findStatic(Arrays.class,
"asList", methodType(List.class, Object[].class));
assertEquals("[x, y]", MH_asList.invoke("x", "y").toString());
```

**Parameters:** refc

- the class from which the method is accessed
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the method does not exist
**Throws:** IllegalAccessException

- if access checking fails,
or if the method is not

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

- findVirtual

```java
public
MethodHandle
findVirtual​(
Class
<?> refc,

String
name,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces a method handle for a virtual method.
The type of the method handle will be that of the method,
with the receiver type (usually

refc

) prepended.
The method and all its argument types must be accessible to the lookup object.

When called, the handle will treat the first argument as a receiver
and, for non-private methods, dispatch on the receiver's type to determine which method
implementation to enter.
For private methods the named method in

refc

will be invoked on the receiver.
(The dispatching action is identical with that performed by an

invokevirtual

or

invokeinterface

instruction.)

The first argument will be of type

refc

if the lookup
class has full privileges to access the member. Otherwise
the member must be

protected

and the first argument
will be restricted in type to the lookup class.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

Because of the general

equivalence

between

invokevirtual

instructions and method handles produced by

findVirtual

,
if the class is

MethodHandle

and the name string is

invokeExact

or

invoke

, the resulting
method handle is equivalent to one produced by

MethodHandles.exactInvoker

or

MethodHandles.invoker

with the same

type

argument.

If the class is

VarHandle

and the name string corresponds to
the name of a signature-polymorphic access mode method, the resulting
method handle is equivalent to one produced by

MethodHandles.varHandleInvoker(java.lang.invoke.VarHandle.AccessMode, java.lang.invoke.MethodType)

with
the access mode corresponding to the name string and with the same

type

arguments.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_concat = publicLookup().findVirtual(String.class,
"concat", methodType(String.class, String.class));
MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
"hashCode", methodType(int.class));
MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
"hashCode", methodType(int.class));
assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
// interface method:
MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
"subSequence", methodType(CharSequence.class, int.class, int.class));
assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
// constructor "internal method" must be accessed differently:
MethodType MT_newString = methodType(void.class); //()V for new String()
try { assertEquals("impossible", lookup()
.findVirtual(String.class, "<init>", MT_newString));
} catch (NoSuchMethodException ex) { } // OK
MethodHandle MH_newString = publicLookup()
.findConstructor(String.class, MT_newString);
assertEquals("", (String) MH_newString.invokeExact());
```

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method, with the receiver argument omitted
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the method does not exist
**Throws:** IllegalAccessException

- if access checking fails,
or if the method is

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

- findConstructor

```java
public
MethodHandle
findConstructor​(
Class
<?> refc,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces a method handle which creates an object and initializes it, using
the constructor of the specified type.
The parameter types of the method handle will be those of the constructor,
while the return type will be a reference to the constructor's class.
The constructor and all its argument types must be accessible to the lookup object.

The requested type must have a return type of

void

.
(This is consistent with the JVM's treatment of constructor type descriptors.)

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_newArrayList = publicLookup().findConstructor(
ArrayList.class, methodType(void.class, Collection.class));
Collection orig = Arrays.asList("x", "y");
Collection copy = (ArrayList) MH_newArrayList.invokeExact(orig);
assert(orig != copy);
assertEquals(orig, copy);
// a variable-arity constructor:
MethodHandle MH_newProcessBuilder = publicLookup().findConstructor(
ProcessBuilder.class, methodType(void.class, String[].class));
ProcessBuilder pb = (ProcessBuilder)
MH_newProcessBuilder.invoke("x", "y", "z");
assertEquals("[x, y, z]", pb.command().toString());
```

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** type

- the type of the method, with the receiver argument omitted, and a void return type
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the constructor does not exist
**Throws:** IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

- findClass

```java
public
Class
<?> findClass​(
String
targetName)
throws
ClassNotFoundException
,

IllegalAccessException
```

Looks up a class by name from the lookup context defined by this

Lookup

object. The static
initializer of the class is not run.

The lookup context here is determined by the

lookup class

, its class
loader, and the

lookup modes

. In particular, the method first attempts to
load the requested class, and then determines whether the class is accessible to this lookup object.

**Parameters:** targetName

- the fully qualified name of the class to be looked up.
**Returns:** the requested class.
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** LinkageError

- if the linkage fails
**Throws:** ClassNotFoundException

- if the class cannot be loaded by the lookup class' loader.
**Throws:** IllegalAccessException

- if the class is not accessible, using the allowed access
modes.
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Since:** 9

- accessClass

```java
public
Class
<?> accessClass​(
Class
<?> targetClass)
throws
IllegalAccessException
```

Determines if a class can be accessed from the lookup context defined by this

Lookup

object. The
static initializer of the class is not run.

The lookup context here is determined by the

lookup class

and the

lookup modes

.

**Parameters:** targetClass

- the class to be access-checked
**Returns:** the class that has been access-checked
**Throws:** IllegalAccessException

- if the class is not accessible from the lookup class, using the allowed access
modes.
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Since:** 9

- findSpecial

```java
public
MethodHandle
findSpecial​(
Class
<?> refc,

String
name,

MethodType
type,

Class
<?> specialCaller)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces an early-bound method handle for a virtual method.
It will bypass checks for overriding methods on the receiver,

as if called

from an

invokespecial

instruction from within the explicitly specified

specialCaller

.
The type of the method handle will be that of the method,
with a suitably restricted receiver type prepended.
(The receiver type will be

specialCaller

or a subtype.)
The method and all its argument types must be accessible
to the lookup object.

Before method resolution,
if the explicitly specified caller class is not identical with the
lookup class, or if this lookup object does not have

private access

privileges, the access fails.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

(Note: JVM internal methods named

"<init>"

are not visible to this API,
even though the

invokespecial

instruction can refer to them
in special circumstances. Use

findConstructor

to access instance initialization methods in a safe manner.)

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
static class Listie extends ArrayList {
public String toString() { return "[wee Listie]"; }
static Lookup lookup() { return MethodHandles.lookup(); }
}
...
// no access to constructor via invokeSpecial:
MethodHandle MH_newListie = Listie.lookup()
.findConstructor(Listie.class, methodType(void.class));
Listie l = (Listie) MH_newListie.invokeExact();
try { assertEquals("impossible", Listie.lookup().findSpecial(
Listie.class, "<init>", methodType(void.class), Listie.class));
} catch (NoSuchMethodException ex) { } // OK
// access to super and self methods via invokeSpecial:
MethodHandle MH_super = Listie.lookup().findSpecial(
ArrayList.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_this = Listie.lookup().findSpecial(
Listie.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_duper = Listie.lookup().findSpecial(
Object.class, "toString" , methodType(String.class), Listie.class);
assertEquals("[]", (String) MH_super.invokeExact(l));
assertEquals(""+l, (String) MH_this.invokeExact(l));
assertEquals("[]", (String) MH_duper.invokeExact(l)); // ArrayList method
try { assertEquals("inaccessible", Listie.lookup().findSpecial(
String.class, "toString", methodType(String.class), Listie.class));
} catch (IllegalAccessException ex) { } // OK
Listie subl = new Listie() { public String toString() { return "[subclass]"; } };
assertEquals(""+l, (String) MH_this.invokeExact(subl)); // Listie method
```

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the name of the method (which must not be "<init>")
**Parameters:** type

- the type of the method, with the receiver argument omitted
**Parameters:** specialCaller

- the proposed calling class to perform the

invokespecial
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the method does not exist
**Throws:** IllegalAccessException

- if access checking fails,
or if the method is

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

- findGetter

```java
public
MethodHandle
findGetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a method handle giving read access to a non-static field.
The type of the method handle will have a return type of the field's
value type.
The method handle's single argument will be the instance containing
the field.
Access checking is performed immediately on behalf of the lookup class.

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type
**Returns:** a method handle which can load values from the field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**See Also:** findVarHandle(Class, String, Class)

- findSetter

```java
public
MethodHandle
findSetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a method handle giving write access to a non-static field.
The type of the method handle will have a void return type.
The method handle will take two arguments, the instance containing
the field, and the value to be stored.
The second argument will be of the field's value type.
Access checking is performed immediately on behalf of the lookup class.

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type
**Returns:** a method handle which can store values into the field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**See Also:** findVarHandle(Class, String, Class)

- findVarHandle

```java
public
VarHandle
findVarHandle​(
Class
<?> recv,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a VarHandle giving access to a non-static field

name

of type

type

declared in a class of type

recv

.
The VarHandle's variable type is

type

and it has one
coordinate type,

recv

.

Access checking is performed immediately on behalf of the lookup
class.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

**API Note:** Bitwise comparison of

float

values or

double

values,
as performed by the numeric and atomic update access modes, differ
from the primitive

==

operator and the

Float.equals(java.lang.Object)

and

Double.equals(java.lang.Object)

methods, specifically with respect to
comparing NaN values or comparing

-0.0

with

+0.0

.
Care should be taken when performing a compare and set or a compare
and exchange operation with such values since the operation may
unexpectedly fail.
There are many possible NaN values that are considered to be

NaN

in Java, although no IEEE 754 floating-point operation
provided by Java can distinguish between them. Operation failure can
occur if the expected or witness value is a NaN value and it is
transformed (perhaps in a platform specific manner) into another NaN
value, and thus has a different bitwise representation (see

Float.intBitsToFloat(int)

or

Double.longBitsToDouble(long)

for more
details).
The values

-0.0

and

+0.0

have different bitwise
representations but are considered equal when using the primitive

==

operator. Operation failure can occur if, for example, a
numeric algorithm computes an expected value to be say

-0.0

and previously computed the witness value to be say

+0.0

.
**Parameters:** recv

- the receiver class, of type

R

, that declares the
non-static field
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type, of type

T
**Returns:** a VarHandle giving access to non-static fields.
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**Since:** 9

- findStaticGetter

```java
public
MethodHandle
findStaticGetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a method handle giving read access to a static field.
The type of the method handle will have a return type of the field's
value type.
The method handle will take no arguments.
Access checking is performed immediately on behalf of the lookup class.

If the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type
**Returns:** a method handle which can load values from the field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is not

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

- findStaticSetter

```java
public
MethodHandle
findStaticSetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a method handle giving write access to a static field.
The type of the method handle will have a void return type.
The method handle will take a single
argument, of the field's value type, the value to be stored.
Access checking is performed immediately on behalf of the lookup class.

If the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type
**Returns:** a method handle which can store values into the field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is not

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

- findStaticVarHandle

```java
public
VarHandle
findStaticVarHandle​(
Class
<?> decl,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a VarHandle giving access to a static field

name

of
type

type

declared in a class of type

decl

.
The VarHandle's variable type is

type

and it has no
coordinate types.

Access checking is performed immediately on behalf of the lookup
class.

If the returned VarHandle is operated on, the declaring class will be
initialized, if it has not already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

, then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

**API Note:** Bitwise comparison of

float

values or

double

values,
as performed by the numeric and atomic update access modes, differ
from the primitive

==

operator and the

Float.equals(java.lang.Object)

and

Double.equals(java.lang.Object)

methods, specifically with respect to
comparing NaN values or comparing

-0.0

with

+0.0

.
Care should be taken when performing a compare and set or a compare
and exchange operation with such values since the operation may
unexpectedly fail.
There are many possible NaN values that are considered to be

NaN

in Java, although no IEEE 754 floating-point operation
provided by Java can distinguish between them. Operation failure can
occur if the expected or witness value is a NaN value and it is
transformed (perhaps in a platform specific manner) into another NaN
value, and thus has a different bitwise representation (see

Float.intBitsToFloat(int)

or

Double.longBitsToDouble(long)

for more
details).
The values

-0.0

and

+0.0

have different bitwise
representations but are considered equal when using the primitive

==

operator. Operation failure can occur if, for example, a
numeric algorithm computes an expected value to be say

-0.0

and previously computed the witness value to be say

+0.0

.
**Parameters:** decl

- the class that declares the static field
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type, of type

T
**Returns:** a VarHandle giving access to a static field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is not

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**Since:** 9

- bind

```java
public
MethodHandle
bind​(
Object
receiver,

String
name,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces an early-bound method handle for a non-static method.
The receiver must have a supertype

defc

in which a method
of the given name and type is accessible to the lookup class.
The method and all its argument types must be accessible to the lookup object.
The type of the method handle will be that of the method,
without any insertion of an additional receiver parameter.
The given receiver will be bound into the method handle,
so that every call to the method handle will invoke the
requested method on the given receiver.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set

and

the trailing array argument is not the only argument.
(If the trailing array argument is the only argument,
the given receiver value will be bound to it.)

This is almost equivalent to the following code, with some differences noted below:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle mh0 = lookup().findVirtual(defc, name, type);
MethodHandle mh1 = mh0.bindTo(receiver);
mh1 = mh1.withVarargs(mh0.isVarargsCollector());
return mh1;
```

where

defc

is either

receiver.getClass()

or a super
type of that class, in which the requested method is accessible
to the lookup class.
(Unlike

bind

,

bindTo

does not preserve variable arity.
Also,

bindTo

may throw a

ClassCastException

in instances where

bind

would
throw an

IllegalAccessException

, as in the case where the member is

protected

and
the receiver is restricted by

findVirtual

to the lookup class.)

**Parameters:** receiver

- the object from which the method is accessed
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method, with the receiver argument omitted
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the method does not exist
**Throws:** IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**See Also:** MethodHandle.bindTo(java.lang.Object)

,

findVirtual(java.lang.Class<?>, java.lang.String, java.lang.invoke.MethodType)

- unreflect

```java
public
MethodHandle
unreflect​(
Method
m)
throws
IllegalAccessException
```

Makes a

direct method handle

to

m

, if the lookup class has permission.
If

m

is non-static, the receiver argument is treated as an initial argument.
If

m

is virtual, overriding is respected on every call.
Unlike the Core Reflection API, exceptions are

not

wrapped.
The type of the method handle will be that of the method,
with the receiver type prepended (but only if it is non-static).
If the method's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.
If

m

is not public, do not share the resulting handle with untrusted parties.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

If

m

is static, and
if the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

**Parameters:** m

- the reflected method
**Returns:** a method handle which can invoke the reflected method
**Throws:** IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** NullPointerException

- if the argument is null

- unreflectSpecial

```java
public
MethodHandle
unreflectSpecial​(
Method
m,

Class
<?> specialCaller)
throws
IllegalAccessException
```

Produces a method handle for a reflected method.
It will bypass checks for overriding methods on the receiver,

as if called

from an

invokespecial

instruction from within the explicitly specified

specialCaller

.
The type of the method handle will be that of the method,
with a suitably restricted receiver type prepended.
(The receiver type will be

specialCaller

or a subtype.)
If the method's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class,
as if

invokespecial

instruction were being linked.

Before method resolution,
if the explicitly specified caller class is not identical with the
lookup class, or if this lookup object does not have

private access

privileges, the access fails.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

**Parameters:** m

- the reflected method
**Parameters:** specialCaller

- the class nominally calling the method
**Returns:** a method handle which can invoke the reflected method
**Throws:** IllegalAccessException

- if access checking fails,
or if the method is

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** NullPointerException

- if any argument is null

- unreflectConstructor

```java
public
MethodHandle
unreflectConstructor​(
Constructor
<?> c)
throws
IllegalAccessException
```

Produces a method handle for a reflected constructor.
The type of the method handle will be that of the constructor,
with the return type changed to the declaring class.
The method handle will perform a

newInstance

operation,
creating a new instance of the constructor's class on the
arguments passed to the method handle.

If the constructor's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

**Parameters:** c

- the reflected constructor
**Returns:** a method handle which can invoke the reflected constructor
**Throws:** IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** NullPointerException

- if the argument is null

- unreflectGetter

```java
public
MethodHandle
unreflectGetter​(
Field
f)
throws
IllegalAccessException
```

Produces a method handle giving read access to a reflected field.
The type of the method handle will have a return type of the field's
value type.
If the field is static, the method handle will take no arguments.
Otherwise, its single argument will be the instance containing
the field.
If the field's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

If the field is static, and
if the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:** f

- the reflected field
**Returns:** a method handle which can load values from the reflected field
**Throws:** IllegalAccessException

- if access checking fails
**Throws:** NullPointerException

- if the argument is null

- unreflectSetter

```java
public
MethodHandle
unreflectSetter​(
Field
f)
throws
IllegalAccessException
```

Produces a method handle giving write access to a reflected field.
The type of the method handle will have a void return type.
If the field is static, the method handle will take a single
argument, of the field's value type, the value to be stored.
Otherwise, the two arguments will be the instance containing
the field, and the value to be stored.
If the field's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

If the field is static, and
if the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:** f

- the reflected field
**Returns:** a method handle which can store values into the reflected field
**Throws:** IllegalAccessException

- if access checking fails
**Throws:** NullPointerException

- if the argument is null

- unreflectVarHandle

```java
public
VarHandle
unreflectVarHandle​(
Field
f)
throws
IllegalAccessException
```

Produces a VarHandle giving access to a reflected field

f

of type

T

declared in a class of type

R

.
The VarHandle's variable type is

T

.
If the field is non-static the VarHandle has one coordinate type,

R

. Otherwise, the field is static, and the VarHandle has no
coordinate types.

Access checking is performed immediately on behalf of the lookup
class, regardless of the value of the field's

accessible

flag.

If the field is static, and if the returned VarHandle is operated
on, the field's declaring class will be initialized, if it has not
already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

**API Note:** Bitwise comparison of

float

values or

double

values,
as performed by the numeric and atomic update access modes, differ
from the primitive

==

operator and the

Float.equals(java.lang.Object)

and

Double.equals(java.lang.Object)

methods, specifically with respect to
comparing NaN values or comparing

-0.0

with

+0.0

.
Care should be taken when performing a compare and set or a compare
and exchange operation with such values since the operation may
unexpectedly fail.
There are many possible NaN values that are considered to be

NaN

in Java, although no IEEE 754 floating-point operation
provided by Java can distinguish between them. Operation failure can
occur if the expected or witness value is a NaN value and it is
transformed (perhaps in a platform specific manner) into another NaN
value, and thus has a different bitwise representation (see

Float.intBitsToFloat(int)

or

Double.longBitsToDouble(long)

for more
details).
The values

-0.0

and

+0.0

have different bitwise
representations but are considered equal when using the primitive

==

operator. Operation failure can occur if, for example, a
numeric algorithm computes an expected value to be say

-0.0

and previously computed the witness value to be say

+0.0

.
**Parameters:** f

- the reflected field, with a field of type

T

, and
a declaring class of type

R
**Returns:** a VarHandle giving access to non-static fields or a static
field
**Throws:** IllegalAccessException

- if access checking fails
**Throws:** NullPointerException

- if the argument is null
**Since:** 9

- revealDirect

```java
public
MethodHandleInfo
revealDirect​(
MethodHandle
target)
```

Cracks a

direct method handle

created by this lookup object or a similar one.
Security and access checks are performed to ensure that this lookup object
is capable of reproducing the target method handle.
This means that the cracking may fail if target is a direct method handle
but was created by an unrelated lookup object.
This can happen if the method handle is

caller sensitive

and was created by a lookup object for a different class.

**Parameters:** target

- a direct method handle to crack into symbolic reference components
**Returns:** a symbolic reference which can be used to reconstruct this method handle from this lookup object
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** IllegalArgumentException

- if the target is not a direct method handle or if access checking fails
**Throws:** NullPointerException

- if the target is

null
**Since:** 1.8
**See Also:** MethodHandleInfo

- hasPrivateAccess

```java
public boolean hasPrivateAccess()
```

Returns

true

if this lookup has

PRIVATE

access.

**Returns:** true

if this lookup has

PRIVATE

access.
**Since:** 9

Field Detail

- PUBLIC

```java
public static final int PUBLIC
```

A single-bit mask representing

public

access,
which may contribute to the result of

lookupModes

.
The value,

0x01

, happens to be the same as the value of the

public

modifier bit

.

**See Also:** Constant Field Values

- PRIVATE

```java
public static final int PRIVATE
```

A single-bit mask representing

private

access,
which may contribute to the result of

lookupModes

.
The value,

0x02

, happens to be the same as the value of the

private

modifier bit

.

**See Also:** Constant Field Values

- PROTECTED

```java
public static final int PROTECTED
```

A single-bit mask representing

protected

access,
which may contribute to the result of

lookupModes

.
The value,

0x04

, happens to be the same as the value of the

protected

modifier bit

.

**See Also:** Constant Field Values

- PACKAGE

```java
public static final int PACKAGE
```

A single-bit mask representing

package

access (default access),
which may contribute to the result of

lookupModes

.
The value is

0x08

, which does not correspond meaningfully to
any particular

modifier bit

.

**See Also:** Constant Field Values

- MODULE

```java
public static final int MODULE
```

A single-bit mask representing

module

access (default access),
which may contribute to the result of

lookupModes

.
The value is

0x10

, which does not correspond meaningfully to
any particular

modifier bit

.
In conjunction with the

PUBLIC

modifier bit, a

Lookup

with this lookup mode can access all public types in the module of the
lookup class and public types in packages exported by other modules
to the module of the lookup class.

**Since:** 9
**See Also:** Constant Field Values

- UNCONDITIONAL

```java
public static final int UNCONDITIONAL
```

A single-bit mask representing

unconditional

access
which may contribute to the result of

lookupModes

.
The value is

0x20

, which does not correspond meaningfully to
any particular

modifier bit

.
A

Lookup

with this lookup mode assumes

readability

.
In conjunction with the

PUBLIC

modifier bit, a

Lookup

with this lookup mode can access all public members of public types
of all modules where the type is in a package that is

exported unconditionally

.

**Since:** 9
**See Also:** MethodHandles.publicLookup()

,

Constant Field Values

---

#### Field Detail

PUBLIC

```java
public static final int PUBLIC
```

A single-bit mask representing

public

access,
which may contribute to the result of

lookupModes

.
The value,

0x01

, happens to be the same as the value of the

public

modifier bit

.

**See Also:** Constant Field Values

---

#### PUBLIC

public static final int PUBLIC

A single-bit mask representing

public

access,
which may contribute to the result of

lookupModes

.
The value,

0x01

, happens to be the same as the value of the

public

modifier bit

.

PRIVATE

```java
public static final int PRIVATE
```

A single-bit mask representing

private

access,
which may contribute to the result of

lookupModes

.
The value,

0x02

, happens to be the same as the value of the

private

modifier bit

.

**See Also:** Constant Field Values

---

#### PRIVATE

public static final int PRIVATE

A single-bit mask representing

private

access,
which may contribute to the result of

lookupModes

.
The value,

0x02

, happens to be the same as the value of the

private

modifier bit

.

PROTECTED

```java
public static final int PROTECTED
```

A single-bit mask representing

protected

access,
which may contribute to the result of

lookupModes

.
The value,

0x04

, happens to be the same as the value of the

protected

modifier bit

.

**See Also:** Constant Field Values

---

#### PROTECTED

public static final int PROTECTED

A single-bit mask representing

protected

access,
which may contribute to the result of

lookupModes

.
The value,

0x04

, happens to be the same as the value of the

protected

modifier bit

.

PACKAGE

```java
public static final int PACKAGE
```

A single-bit mask representing

package

access (default access),
which may contribute to the result of

lookupModes

.
The value is

0x08

, which does not correspond meaningfully to
any particular

modifier bit

.

**See Also:** Constant Field Values

---

#### PACKAGE

public static final int PACKAGE

A single-bit mask representing

package

access (default access),
which may contribute to the result of

lookupModes

.
The value is

0x08

, which does not correspond meaningfully to
any particular

modifier bit

.

MODULE

```java
public static final int MODULE
```

A single-bit mask representing

module

access (default access),
which may contribute to the result of

lookupModes

.
The value is

0x10

, which does not correspond meaningfully to
any particular

modifier bit

.
In conjunction with the

PUBLIC

modifier bit, a

Lookup

with this lookup mode can access all public types in the module of the
lookup class and public types in packages exported by other modules
to the module of the lookup class.

**Since:** 9
**See Also:** Constant Field Values

---

#### MODULE

public static final int MODULE

A single-bit mask representing

module

access (default access),
which may contribute to the result of

lookupModes

.
The value is

0x10

, which does not correspond meaningfully to
any particular

modifier bit

.
In conjunction with the

PUBLIC

modifier bit, a

Lookup

with this lookup mode can access all public types in the module of the
lookup class and public types in packages exported by other modules
to the module of the lookup class.

UNCONDITIONAL

```java
public static final int UNCONDITIONAL
```

A single-bit mask representing

unconditional

access
which may contribute to the result of

lookupModes

.
The value is

0x20

, which does not correspond meaningfully to
any particular

modifier bit

.
A

Lookup

with this lookup mode assumes

readability

.
In conjunction with the

PUBLIC

modifier bit, a

Lookup

with this lookup mode can access all public members of public types
of all modules where the type is in a package that is

exported unconditionally

.

**Since:** 9
**See Also:** MethodHandles.publicLookup()

,

Constant Field Values

---

#### UNCONDITIONAL

public static final int UNCONDITIONAL

A single-bit mask representing

unconditional

access
which may contribute to the result of

lookupModes

.
The value is

0x20

, which does not correspond meaningfully to
any particular

modifier bit

.
A

Lookup

with this lookup mode assumes

readability

.
In conjunction with the

PUBLIC

modifier bit, a

Lookup

with this lookup mode can access all public members of public types
of all modules where the type is in a package that is

exported unconditionally

.

Method Detail

- lookupClass

```java
public
Class
<?> lookupClass()
```

Tells which class is performing the lookup. It is this class against
which checks are performed for visibility and access permissions.

The class implies a maximum level of access permission,
but the permissions may be additionally limited by the bitmask

lookupModes

, which controls whether non-public members
can be accessed.

**Returns:** the lookup class, on behalf of which this lookup object finds members

- lookupModes

```java
public int lookupModes()
```

Tells which access-protection classes of members this lookup object can produce.
The result is a bit-mask of the bits

PUBLIC (0x01)

,

PRIVATE (0x02)

,

PROTECTED (0x04)

,

PACKAGE (0x08)

,

MODULE (0x10)

,
and

UNCONDITIONAL (0x20)

.

A freshly-created lookup object
on the

caller's class

has
all possible bits set, except

UNCONDITIONAL

.
A lookup object on a new lookup class

created from a previous lookup object

may have some mode bits set to zero.
Mode bits can also be

directly cleared

.
Once cleared, mode bits cannot be restored from the downgraded lookup object.
The purpose of this is to restrict access via the new lookup object,
so that it can access only names which can be reached by the original
lookup object, and also by the new lookup class.

**Returns:** the lookup modes, which limit the kinds of access performed by this lookup object
**See Also:** in(java.lang.Class<?>)

,

dropLookupMode(int)

- in

```java
public
MethodHandles.Lookup
in​(
Class
<?> requestedLookupClass)
```

Creates a lookup on the specified new lookup class.
The resulting object will report the specified
class as its own

lookupClass

.

However, the resulting

Lookup

object is guaranteed
to have no more access capabilities than the original.
In particular, access capabilities can be lost as follows:

- If the old lookup class is in a

named

module, and
the new lookup class is in a different module

M

, then no members, not
even public members in

M

's exported packages, will be accessible.
The exception to this is when this lookup is

publicLookup

, in which case

PUBLIC

access is not lost.

If the old lookup class is in an unnamed module, and the new lookup class
is a different module then

MODULE

access is lost.

If the new lookup class differs from the old one then

UNCONDITIONAL

is lost.

If the new lookup class is in a different package
than the old one, protected and default (package) members will not be accessible.

If the new lookup class is not within the same package member
as the old one, private members will not be accessible, and protected members
will not be accessible by virtue of inheritance.
(Protected members may continue to be accessible because of package sharing.)

If the new lookup class is not accessible to the old lookup class,
then no members, not even public members, will be accessible.
(In all other cases, public members will continue to be accessible.)

The resulting lookup's capabilities for loading classes
(used during

findClass(java.lang.String)

invocations)
are determined by the lookup class' loader,
which may change due to this operation.

**Parameters:** requestedLookupClass

- the desired lookup class for the new lookup object
**Returns:** a lookup object which reports the desired lookup class, or the same object
if there is no change
**Throws:** NullPointerException

- if the argument is null

- dropLookupMode

```java
public
MethodHandles.Lookup
dropLookupMode​(int modeToDrop)
```

Creates a lookup on the same lookup class which this lookup object
finds members, but with a lookup mode that has lost the given lookup mode.
The lookup mode to drop is one of

PUBLIC

,

MODULE

,

PACKAGE

,

PROTECTED

or

PRIVATE

.

PROTECTED

and

UNCONDITIONAL

are always
dropped and so the resulting lookup mode will never have these access capabilities.
When dropping

PACKAGE

then the resulting lookup will not have

PACKAGE

or

PRIVATE

access. When dropping

MODULE

then the resulting lookup will
not have

MODULE

,

PACKAGE

, or

PRIVATE

access. If

PUBLIC

is dropped then the resulting lookup has no access.

**Parameters:** modeToDrop

- the lookup mode to drop
**Returns:** a lookup object which lacks the indicated mode, or the same object if there is no change
**Throws:** IllegalArgumentException

- if

modeToDrop

is not one of

PUBLIC

,

MODULE

,

PACKAGE

,

PROTECTED

,

PRIVATE

or

UNCONDITIONAL
**Since:** 9
**See Also:** MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

- defineClass

```java
public
Class
<?> defineClass​(byte[] bytes)
throws
IllegalAccessException
```

Defines a class to the same class loader and in the same runtime package and

protection domain

as this lookup's

lookup class

.

The

lookup modes

for this lookup must include

PACKAGE

access as default (package) members will be
accessible to the class. The

PACKAGE

lookup mode serves to authenticate
that the lookup object was created by a caller in the runtime package (or derived
from a lookup originally created by suitably privileged code to a target class in
the runtime package).

The

bytes

parameter is the class bytes of a valid class file (as defined
by the

The Java Virtual Machine Specification

) with a class name in the
same package as the lookup class.

This method does not run the class initializer. The class initializer may
run at a later time, as detailed in section 12.4 of the

The Java Language
Specification

.

If there is a security manager, its

checkPermission

method is first called
to check

RuntimePermission("defineClass")

.

**Parameters:** bytes

- the class bytes
**Returns:** the

Class

object for the class
**Throws:** IllegalArgumentException

- the bytes are for a class in a different package
to the lookup class
**Throws:** IllegalAccessException

- if this lookup does not have

PACKAGE

access
**Throws:** LinkageError

- if the class is malformed (

ClassFormatError

), cannot be
verified (

VerifyError

), is already defined, or another linkage error occurs
**Throws:** SecurityException

- if denied by the security manager
**Throws:** NullPointerException

- if

bytes

is

null
**Since:** 9
**See Also:** MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

,

dropLookupMode(int)

,

ClassLoader.defineClass(String,byte[],int,int,ProtectionDomain)

- toString

```java
public
String
toString()
```

Displays the name of the class from which lookups are to be made.
(The name is the one reported by

Class.getName

.)
If there are restrictions on the access permitted to this lookup,
this is indicated by adding a suffix to the class name, consisting
of a slash and a keyword. The keyword represents the strongest
allowed access, and is chosen as follows:

- If no access is allowed, the suffix is "/noaccess".

If only public access to types in exported packages is allowed, the suffix is "/public".

If only public access and unconditional access are allowed, the suffix is "/publicLookup".

If only public and module access are allowed, the suffix is "/module".

If only public, module and package access are allowed, the suffix is "/package".

If only public, module, package, and private access are allowed, the suffix is "/private".

If none of the above cases apply, it is the case that full
access (public, module, package, private, and protected) is allowed.
In this case, no suffix is added.
This is true only of an object obtained originally from

MethodHandles.lookup

.
Objects created by

Lookup.in

always have restricted access, and will display a suffix.

(It may seem strange that protected access should be
stronger than private access. Viewed independently from
package access, protected access is the first to be lost,
because it requires a direct subclass relationship between
caller and callee.)

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.
**See Also:** in(java.lang.Class<?>)

- findStatic

```java
public
MethodHandle
findStatic​(
Class
<?> refc,

String
name,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces a method handle for a static method.
The type of the method handle will be that of the method.
(Since static methods do not take receivers, there is no
additional receiver argument inserted into the method handle type,
as there would be with

findVirtual

or

findSpecial

.)
The method and all its argument types must be accessible to the lookup object.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_asList = publicLookup().findStatic(Arrays.class,
"asList", methodType(List.class, Object[].class));
assertEquals("[x, y]", MH_asList.invoke("x", "y").toString());
```

**Parameters:** refc

- the class from which the method is accessed
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the method does not exist
**Throws:** IllegalAccessException

- if access checking fails,
or if the method is not

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

- findVirtual

```java
public
MethodHandle
findVirtual​(
Class
<?> refc,

String
name,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces a method handle for a virtual method.
The type of the method handle will be that of the method,
with the receiver type (usually

refc

) prepended.
The method and all its argument types must be accessible to the lookup object.

When called, the handle will treat the first argument as a receiver
and, for non-private methods, dispatch on the receiver's type to determine which method
implementation to enter.
For private methods the named method in

refc

will be invoked on the receiver.
(The dispatching action is identical with that performed by an

invokevirtual

or

invokeinterface

instruction.)

The first argument will be of type

refc

if the lookup
class has full privileges to access the member. Otherwise
the member must be

protected

and the first argument
will be restricted in type to the lookup class.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

Because of the general

equivalence

between

invokevirtual

instructions and method handles produced by

findVirtual

,
if the class is

MethodHandle

and the name string is

invokeExact

or

invoke

, the resulting
method handle is equivalent to one produced by

MethodHandles.exactInvoker

or

MethodHandles.invoker

with the same

type

argument.

If the class is

VarHandle

and the name string corresponds to
the name of a signature-polymorphic access mode method, the resulting
method handle is equivalent to one produced by

MethodHandles.varHandleInvoker(java.lang.invoke.VarHandle.AccessMode, java.lang.invoke.MethodType)

with
the access mode corresponding to the name string and with the same

type

arguments.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_concat = publicLookup().findVirtual(String.class,
"concat", methodType(String.class, String.class));
MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
"hashCode", methodType(int.class));
MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
"hashCode", methodType(int.class));
assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
// interface method:
MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
"subSequence", methodType(CharSequence.class, int.class, int.class));
assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
// constructor "internal method" must be accessed differently:
MethodType MT_newString = methodType(void.class); //()V for new String()
try { assertEquals("impossible", lookup()
.findVirtual(String.class, "<init>", MT_newString));
} catch (NoSuchMethodException ex) { } // OK
MethodHandle MH_newString = publicLookup()
.findConstructor(String.class, MT_newString);
assertEquals("", (String) MH_newString.invokeExact());
```

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method, with the receiver argument omitted
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the method does not exist
**Throws:** IllegalAccessException

- if access checking fails,
or if the method is

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

- findConstructor

```java
public
MethodHandle
findConstructor​(
Class
<?> refc,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces a method handle which creates an object and initializes it, using
the constructor of the specified type.
The parameter types of the method handle will be those of the constructor,
while the return type will be a reference to the constructor's class.
The constructor and all its argument types must be accessible to the lookup object.

The requested type must have a return type of

void

.
(This is consistent with the JVM's treatment of constructor type descriptors.)

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_newArrayList = publicLookup().findConstructor(
ArrayList.class, methodType(void.class, Collection.class));
Collection orig = Arrays.asList("x", "y");
Collection copy = (ArrayList) MH_newArrayList.invokeExact(orig);
assert(orig != copy);
assertEquals(orig, copy);
// a variable-arity constructor:
MethodHandle MH_newProcessBuilder = publicLookup().findConstructor(
ProcessBuilder.class, methodType(void.class, String[].class));
ProcessBuilder pb = (ProcessBuilder)
MH_newProcessBuilder.invoke("x", "y", "z");
assertEquals("[x, y, z]", pb.command().toString());
```

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** type

- the type of the method, with the receiver argument omitted, and a void return type
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the constructor does not exist
**Throws:** IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

- findClass

```java
public
Class
<?> findClass​(
String
targetName)
throws
ClassNotFoundException
,

IllegalAccessException
```

Looks up a class by name from the lookup context defined by this

Lookup

object. The static
initializer of the class is not run.

The lookup context here is determined by the

lookup class

, its class
loader, and the

lookup modes

. In particular, the method first attempts to
load the requested class, and then determines whether the class is accessible to this lookup object.

**Parameters:** targetName

- the fully qualified name of the class to be looked up.
**Returns:** the requested class.
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** LinkageError

- if the linkage fails
**Throws:** ClassNotFoundException

- if the class cannot be loaded by the lookup class' loader.
**Throws:** IllegalAccessException

- if the class is not accessible, using the allowed access
modes.
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Since:** 9

- accessClass

```java
public
Class
<?> accessClass​(
Class
<?> targetClass)
throws
IllegalAccessException
```

Determines if a class can be accessed from the lookup context defined by this

Lookup

object. The
static initializer of the class is not run.

The lookup context here is determined by the

lookup class

and the

lookup modes

.

**Parameters:** targetClass

- the class to be access-checked
**Returns:** the class that has been access-checked
**Throws:** IllegalAccessException

- if the class is not accessible from the lookup class, using the allowed access
modes.
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Since:** 9

- findSpecial

```java
public
MethodHandle
findSpecial​(
Class
<?> refc,

String
name,

MethodType
type,

Class
<?> specialCaller)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces an early-bound method handle for a virtual method.
It will bypass checks for overriding methods on the receiver,

as if called

from an

invokespecial

instruction from within the explicitly specified

specialCaller

.
The type of the method handle will be that of the method,
with a suitably restricted receiver type prepended.
(The receiver type will be

specialCaller

or a subtype.)
The method and all its argument types must be accessible
to the lookup object.

Before method resolution,
if the explicitly specified caller class is not identical with the
lookup class, or if this lookup object does not have

private access

privileges, the access fails.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

(Note: JVM internal methods named

"<init>"

are not visible to this API,
even though the

invokespecial

instruction can refer to them
in special circumstances. Use

findConstructor

to access instance initialization methods in a safe manner.)

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
static class Listie extends ArrayList {
public String toString() { return "[wee Listie]"; }
static Lookup lookup() { return MethodHandles.lookup(); }
}
...
// no access to constructor via invokeSpecial:
MethodHandle MH_newListie = Listie.lookup()
.findConstructor(Listie.class, methodType(void.class));
Listie l = (Listie) MH_newListie.invokeExact();
try { assertEquals("impossible", Listie.lookup().findSpecial(
Listie.class, "<init>", methodType(void.class), Listie.class));
} catch (NoSuchMethodException ex) { } // OK
// access to super and self methods via invokeSpecial:
MethodHandle MH_super = Listie.lookup().findSpecial(
ArrayList.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_this = Listie.lookup().findSpecial(
Listie.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_duper = Listie.lookup().findSpecial(
Object.class, "toString" , methodType(String.class), Listie.class);
assertEquals("[]", (String) MH_super.invokeExact(l));
assertEquals(""+l, (String) MH_this.invokeExact(l));
assertEquals("[]", (String) MH_duper.invokeExact(l)); // ArrayList method
try { assertEquals("inaccessible", Listie.lookup().findSpecial(
String.class, "toString", methodType(String.class), Listie.class));
} catch (IllegalAccessException ex) { } // OK
Listie subl = new Listie() { public String toString() { return "[subclass]"; } };
assertEquals(""+l, (String) MH_this.invokeExact(subl)); // Listie method
```

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the name of the method (which must not be "<init>")
**Parameters:** type

- the type of the method, with the receiver argument omitted
**Parameters:** specialCaller

- the proposed calling class to perform the

invokespecial
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the method does not exist
**Throws:** IllegalAccessException

- if access checking fails,
or if the method is

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

- findGetter

```java
public
MethodHandle
findGetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a method handle giving read access to a non-static field.
The type of the method handle will have a return type of the field's
value type.
The method handle's single argument will be the instance containing
the field.
Access checking is performed immediately on behalf of the lookup class.

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type
**Returns:** a method handle which can load values from the field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**See Also:** findVarHandle(Class, String, Class)

- findSetter

```java
public
MethodHandle
findSetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a method handle giving write access to a non-static field.
The type of the method handle will have a void return type.
The method handle will take two arguments, the instance containing
the field, and the value to be stored.
The second argument will be of the field's value type.
Access checking is performed immediately on behalf of the lookup class.

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type
**Returns:** a method handle which can store values into the field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**See Also:** findVarHandle(Class, String, Class)

- findVarHandle

```java
public
VarHandle
findVarHandle​(
Class
<?> recv,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a VarHandle giving access to a non-static field

name

of type

type

declared in a class of type

recv

.
The VarHandle's variable type is

type

and it has one
coordinate type,

recv

.

Access checking is performed immediately on behalf of the lookup
class.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

**API Note:** Bitwise comparison of

float

values or

double

values,
as performed by the numeric and atomic update access modes, differ
from the primitive

==

operator and the

Float.equals(java.lang.Object)

and

Double.equals(java.lang.Object)

methods, specifically with respect to
comparing NaN values or comparing

-0.0

with

+0.0

.
Care should be taken when performing a compare and set or a compare
and exchange operation with such values since the operation may
unexpectedly fail.
There are many possible NaN values that are considered to be

NaN

in Java, although no IEEE 754 floating-point operation
provided by Java can distinguish between them. Operation failure can
occur if the expected or witness value is a NaN value and it is
transformed (perhaps in a platform specific manner) into another NaN
value, and thus has a different bitwise representation (see

Float.intBitsToFloat(int)

or

Double.longBitsToDouble(long)

for more
details).
The values

-0.0

and

+0.0

have different bitwise
representations but are considered equal when using the primitive

==

operator. Operation failure can occur if, for example, a
numeric algorithm computes an expected value to be say

-0.0

and previously computed the witness value to be say

+0.0

.
**Parameters:** recv

- the receiver class, of type

R

, that declares the
non-static field
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type, of type

T
**Returns:** a VarHandle giving access to non-static fields.
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**Since:** 9

- findStaticGetter

```java
public
MethodHandle
findStaticGetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a method handle giving read access to a static field.
The type of the method handle will have a return type of the field's
value type.
The method handle will take no arguments.
Access checking is performed immediately on behalf of the lookup class.

If the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type
**Returns:** a method handle which can load values from the field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is not

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

- findStaticSetter

```java
public
MethodHandle
findStaticSetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a method handle giving write access to a static field.
The type of the method handle will have a void return type.
The method handle will take a single
argument, of the field's value type, the value to be stored.
Access checking is performed immediately on behalf of the lookup class.

If the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type
**Returns:** a method handle which can store values into the field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is not

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

- findStaticVarHandle

```java
public
VarHandle
findStaticVarHandle​(
Class
<?> decl,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a VarHandle giving access to a static field

name

of
type

type

declared in a class of type

decl

.
The VarHandle's variable type is

type

and it has no
coordinate types.

Access checking is performed immediately on behalf of the lookup
class.

If the returned VarHandle is operated on, the declaring class will be
initialized, if it has not already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

, then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

**API Note:** Bitwise comparison of

float

values or

double

values,
as performed by the numeric and atomic update access modes, differ
from the primitive

==

operator and the

Float.equals(java.lang.Object)

and

Double.equals(java.lang.Object)

methods, specifically with respect to
comparing NaN values or comparing

-0.0

with

+0.0

.
Care should be taken when performing a compare and set or a compare
and exchange operation with such values since the operation may
unexpectedly fail.
There are many possible NaN values that are considered to be

NaN

in Java, although no IEEE 754 floating-point operation
provided by Java can distinguish between them. Operation failure can
occur if the expected or witness value is a NaN value and it is
transformed (perhaps in a platform specific manner) into another NaN
value, and thus has a different bitwise representation (see

Float.intBitsToFloat(int)

or

Double.longBitsToDouble(long)

for more
details).
The values

-0.0

and

+0.0

have different bitwise
representations but are considered equal when using the primitive

==

operator. Operation failure can occur if, for example, a
numeric algorithm computes an expected value to be say

-0.0

and previously computed the witness value to be say

+0.0

.
**Parameters:** decl

- the class that declares the static field
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type, of type

T
**Returns:** a VarHandle giving access to a static field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is not

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**Since:** 9

- bind

```java
public
MethodHandle
bind​(
Object
receiver,

String
name,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces an early-bound method handle for a non-static method.
The receiver must have a supertype

defc

in which a method
of the given name and type is accessible to the lookup class.
The method and all its argument types must be accessible to the lookup object.
The type of the method handle will be that of the method,
without any insertion of an additional receiver parameter.
The given receiver will be bound into the method handle,
so that every call to the method handle will invoke the
requested method on the given receiver.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set

and

the trailing array argument is not the only argument.
(If the trailing array argument is the only argument,
the given receiver value will be bound to it.)

This is almost equivalent to the following code, with some differences noted below:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle mh0 = lookup().findVirtual(defc, name, type);
MethodHandle mh1 = mh0.bindTo(receiver);
mh1 = mh1.withVarargs(mh0.isVarargsCollector());
return mh1;
```

where

defc

is either

receiver.getClass()

or a super
type of that class, in which the requested method is accessible
to the lookup class.
(Unlike

bind

,

bindTo

does not preserve variable arity.
Also,

bindTo

may throw a

ClassCastException

in instances where

bind

would
throw an

IllegalAccessException

, as in the case where the member is

protected

and
the receiver is restricted by

findVirtual

to the lookup class.)

**Parameters:** receiver

- the object from which the method is accessed
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method, with the receiver argument omitted
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the method does not exist
**Throws:** IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**See Also:** MethodHandle.bindTo(java.lang.Object)

,

findVirtual(java.lang.Class<?>, java.lang.String, java.lang.invoke.MethodType)

- unreflect

```java
public
MethodHandle
unreflect​(
Method
m)
throws
IllegalAccessException
```

Makes a

direct method handle

to

m

, if the lookup class has permission.
If

m

is non-static, the receiver argument is treated as an initial argument.
If

m

is virtual, overriding is respected on every call.
Unlike the Core Reflection API, exceptions are

not

wrapped.
The type of the method handle will be that of the method,
with the receiver type prepended (but only if it is non-static).
If the method's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.
If

m

is not public, do not share the resulting handle with untrusted parties.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

If

m

is static, and
if the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

**Parameters:** m

- the reflected method
**Returns:** a method handle which can invoke the reflected method
**Throws:** IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** NullPointerException

- if the argument is null

- unreflectSpecial

```java
public
MethodHandle
unreflectSpecial​(
Method
m,

Class
<?> specialCaller)
throws
IllegalAccessException
```

Produces a method handle for a reflected method.
It will bypass checks for overriding methods on the receiver,

as if called

from an

invokespecial

instruction from within the explicitly specified

specialCaller

.
The type of the method handle will be that of the method,
with a suitably restricted receiver type prepended.
(The receiver type will be

specialCaller

or a subtype.)
If the method's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class,
as if

invokespecial

instruction were being linked.

Before method resolution,
if the explicitly specified caller class is not identical with the
lookup class, or if this lookup object does not have

private access

privileges, the access fails.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

**Parameters:** m

- the reflected method
**Parameters:** specialCaller

- the class nominally calling the method
**Returns:** a method handle which can invoke the reflected method
**Throws:** IllegalAccessException

- if access checking fails,
or if the method is

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** NullPointerException

- if any argument is null

- unreflectConstructor

```java
public
MethodHandle
unreflectConstructor​(
Constructor
<?> c)
throws
IllegalAccessException
```

Produces a method handle for a reflected constructor.
The type of the method handle will be that of the constructor,
with the return type changed to the declaring class.
The method handle will perform a

newInstance

operation,
creating a new instance of the constructor's class on the
arguments passed to the method handle.

If the constructor's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

**Parameters:** c

- the reflected constructor
**Returns:** a method handle which can invoke the reflected constructor
**Throws:** IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** NullPointerException

- if the argument is null

- unreflectGetter

```java
public
MethodHandle
unreflectGetter​(
Field
f)
throws
IllegalAccessException
```

Produces a method handle giving read access to a reflected field.
The type of the method handle will have a return type of the field's
value type.
If the field is static, the method handle will take no arguments.
Otherwise, its single argument will be the instance containing
the field.
If the field's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

If the field is static, and
if the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:** f

- the reflected field
**Returns:** a method handle which can load values from the reflected field
**Throws:** IllegalAccessException

- if access checking fails
**Throws:** NullPointerException

- if the argument is null

- unreflectSetter

```java
public
MethodHandle
unreflectSetter​(
Field
f)
throws
IllegalAccessException
```

Produces a method handle giving write access to a reflected field.
The type of the method handle will have a void return type.
If the field is static, the method handle will take a single
argument, of the field's value type, the value to be stored.
Otherwise, the two arguments will be the instance containing
the field, and the value to be stored.
If the field's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

If the field is static, and
if the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:** f

- the reflected field
**Returns:** a method handle which can store values into the reflected field
**Throws:** IllegalAccessException

- if access checking fails
**Throws:** NullPointerException

- if the argument is null

- unreflectVarHandle

```java
public
VarHandle
unreflectVarHandle​(
Field
f)
throws
IllegalAccessException
```

Produces a VarHandle giving access to a reflected field

f

of type

T

declared in a class of type

R

.
The VarHandle's variable type is

T

.
If the field is non-static the VarHandle has one coordinate type,

R

. Otherwise, the field is static, and the VarHandle has no
coordinate types.

Access checking is performed immediately on behalf of the lookup
class, regardless of the value of the field's

accessible

flag.

If the field is static, and if the returned VarHandle is operated
on, the field's declaring class will be initialized, if it has not
already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

**API Note:** Bitwise comparison of

float

values or

double

values,
as performed by the numeric and atomic update access modes, differ
from the primitive

==

operator and the

Float.equals(java.lang.Object)

and

Double.equals(java.lang.Object)

methods, specifically with respect to
comparing NaN values or comparing

-0.0

with

+0.0

.
Care should be taken when performing a compare and set or a compare
and exchange operation with such values since the operation may
unexpectedly fail.
There are many possible NaN values that are considered to be

NaN

in Java, although no IEEE 754 floating-point operation
provided by Java can distinguish between them. Operation failure can
occur if the expected or witness value is a NaN value and it is
transformed (perhaps in a platform specific manner) into another NaN
value, and thus has a different bitwise representation (see

Float.intBitsToFloat(int)

or

Double.longBitsToDouble(long)

for more
details).
The values

-0.0

and

+0.0

have different bitwise
representations but are considered equal when using the primitive

==

operator. Operation failure can occur if, for example, a
numeric algorithm computes an expected value to be say

-0.0

and previously computed the witness value to be say

+0.0

.
**Parameters:** f

- the reflected field, with a field of type

T

, and
a declaring class of type

R
**Returns:** a VarHandle giving access to non-static fields or a static
field
**Throws:** IllegalAccessException

- if access checking fails
**Throws:** NullPointerException

- if the argument is null
**Since:** 9

- revealDirect

```java
public
MethodHandleInfo
revealDirect​(
MethodHandle
target)
```

Cracks a

direct method handle

created by this lookup object or a similar one.
Security and access checks are performed to ensure that this lookup object
is capable of reproducing the target method handle.
This means that the cracking may fail if target is a direct method handle
but was created by an unrelated lookup object.
This can happen if the method handle is

caller sensitive

and was created by a lookup object for a different class.

**Parameters:** target

- a direct method handle to crack into symbolic reference components
**Returns:** a symbolic reference which can be used to reconstruct this method handle from this lookup object
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** IllegalArgumentException

- if the target is not a direct method handle or if access checking fails
**Throws:** NullPointerException

- if the target is

null
**Since:** 1.8
**See Also:** MethodHandleInfo

- hasPrivateAccess

```java
public boolean hasPrivateAccess()
```

Returns

true

if this lookup has

PRIVATE

access.

**Returns:** true

if this lookup has

PRIVATE

access.
**Since:** 9

---

#### Method Detail

lookupClass

```java
public
Class
<?> lookupClass()
```

Tells which class is performing the lookup. It is this class against
which checks are performed for visibility and access permissions.

The class implies a maximum level of access permission,
but the permissions may be additionally limited by the bitmask

lookupModes

, which controls whether non-public members
can be accessed.

**Returns:** the lookup class, on behalf of which this lookup object finds members

---

#### lookupClass

public

Class

<?> lookupClass()

Tells which class is performing the lookup. It is this class against
which checks are performed for visibility and access permissions.

The class implies a maximum level of access permission,
but the permissions may be additionally limited by the bitmask

lookupModes

, which controls whether non-public members
can be accessed.

The class implies a maximum level of access permission,
but the permissions may be additionally limited by the bitmask

lookupModes

, which controls whether non-public members
can be accessed.

lookupModes

```java
public int lookupModes()
```

Tells which access-protection classes of members this lookup object can produce.
The result is a bit-mask of the bits

PUBLIC (0x01)

,

PRIVATE (0x02)

,

PROTECTED (0x04)

,

PACKAGE (0x08)

,

MODULE (0x10)

,
and

UNCONDITIONAL (0x20)

.

A freshly-created lookup object
on the

caller's class

has
all possible bits set, except

UNCONDITIONAL

.
A lookup object on a new lookup class

created from a previous lookup object

may have some mode bits set to zero.
Mode bits can also be

directly cleared

.
Once cleared, mode bits cannot be restored from the downgraded lookup object.
The purpose of this is to restrict access via the new lookup object,
so that it can access only names which can be reached by the original
lookup object, and also by the new lookup class.

**Returns:** the lookup modes, which limit the kinds of access performed by this lookup object
**See Also:** in(java.lang.Class<?>)

,

dropLookupMode(int)

---

#### lookupModes

public int lookupModes()

Tells which access-protection classes of members this lookup object can produce.
The result is a bit-mask of the bits

PUBLIC (0x01)

,

PRIVATE (0x02)

,

PROTECTED (0x04)

,

PACKAGE (0x08)

,

MODULE (0x10)

,
and

UNCONDITIONAL (0x20)

.

A freshly-created lookup object
on the

caller's class

has
all possible bits set, except

UNCONDITIONAL

.
A lookup object on a new lookup class

created from a previous lookup object

may have some mode bits set to zero.
Mode bits can also be

directly cleared

.
Once cleared, mode bits cannot be restored from the downgraded lookup object.
The purpose of this is to restrict access via the new lookup object,
so that it can access only names which can be reached by the original
lookup object, and also by the new lookup class.

A freshly-created lookup object
on the

caller's class

has
all possible bits set, except

UNCONDITIONAL

.
A lookup object on a new lookup class

created from a previous lookup object

may have some mode bits set to zero.
Mode bits can also be

directly cleared

.
Once cleared, mode bits cannot be restored from the downgraded lookup object.
The purpose of this is to restrict access via the new lookup object,
so that it can access only names which can be reached by the original
lookup object, and also by the new lookup class.

in

```java
public
MethodHandles.Lookup
in​(
Class
<?> requestedLookupClass)
```

Creates a lookup on the specified new lookup class.
The resulting object will report the specified
class as its own

lookupClass

.

However, the resulting

Lookup

object is guaranteed
to have no more access capabilities than the original.
In particular, access capabilities can be lost as follows:

- If the old lookup class is in a

named

module, and
the new lookup class is in a different module

M

, then no members, not
even public members in

M

's exported packages, will be accessible.
The exception to this is when this lookup is

publicLookup

, in which case

PUBLIC

access is not lost.

If the old lookup class is in an unnamed module, and the new lookup class
is a different module then

MODULE

access is lost.

If the new lookup class differs from the old one then

UNCONDITIONAL

is lost.

If the new lookup class is in a different package
than the old one, protected and default (package) members will not be accessible.

If the new lookup class is not within the same package member
as the old one, private members will not be accessible, and protected members
will not be accessible by virtue of inheritance.
(Protected members may continue to be accessible because of package sharing.)

If the new lookup class is not accessible to the old lookup class,
then no members, not even public members, will be accessible.
(In all other cases, public members will continue to be accessible.)

The resulting lookup's capabilities for loading classes
(used during

findClass(java.lang.String)

invocations)
are determined by the lookup class' loader,
which may change due to this operation.

**Parameters:** requestedLookupClass

- the desired lookup class for the new lookup object
**Returns:** a lookup object which reports the desired lookup class, or the same object
if there is no change
**Throws:** NullPointerException

- if the argument is null

---

#### in

public

MethodHandles.Lookup

in​(

Class

<?> requestedLookupClass)

Creates a lookup on the specified new lookup class.
The resulting object will report the specified
class as its own

lookupClass

.

However, the resulting

Lookup

object is guaranteed
to have no more access capabilities than the original.
In particular, access capabilities can be lost as follows:

- If the old lookup class is in a

named

module, and
the new lookup class is in a different module

M

, then no members, not
even public members in

M

's exported packages, will be accessible.
The exception to this is when this lookup is

publicLookup

, in which case

PUBLIC

access is not lost.

If the old lookup class is in an unnamed module, and the new lookup class
is a different module then

MODULE

access is lost.

If the new lookup class differs from the old one then

UNCONDITIONAL

is lost.

If the new lookup class is in a different package
than the old one, protected and default (package) members will not be accessible.

If the new lookup class is not within the same package member
as the old one, private members will not be accessible, and protected members
will not be accessible by virtue of inheritance.
(Protected members may continue to be accessible because of package sharing.)

If the new lookup class is not accessible to the old lookup class,
then no members, not even public members, will be accessible.
(In all other cases, public members will continue to be accessible.)

The resulting lookup's capabilities for loading classes
(used during

findClass(java.lang.String)

invocations)
are determined by the lookup class' loader,
which may change due to this operation.

However, the resulting

Lookup

object is guaranteed
to have no more access capabilities than the original.
In particular, access capabilities can be lost as follows:

- If the old lookup class is in a

named

module, and
the new lookup class is in a different module

M

, then no members, not
even public members in

M

's exported packages, will be accessible.
The exception to this is when this lookup is

publicLookup

, in which case

PUBLIC

access is not lost.

If the old lookup class is in an unnamed module, and the new lookup class
is a different module then

MODULE

access is lost.

If the new lookup class differs from the old one then

UNCONDITIONAL

is lost.

If the new lookup class is in a different package
than the old one, protected and default (package) members will not be accessible.

If the new lookup class is not within the same package member
as the old one, private members will not be accessible, and protected members
will not be accessible by virtue of inheritance.
(Protected members may continue to be accessible because of package sharing.)

If the new lookup class is not accessible to the old lookup class,
then no members, not even public members, will be accessible.
(In all other cases, public members will continue to be accessible.)

The resulting lookup's capabilities for loading classes
(used during

findClass(java.lang.String)

invocations)
are determined by the lookup class' loader,
which may change due to this operation.

If the old lookup class is in a

named

module, and
the new lookup class is in a different module

M

, then no members, not
even public members in

M

's exported packages, will be accessible.
The exception to this is when this lookup is

publicLookup

, in which case

PUBLIC

access is not lost.

If the old lookup class is in an unnamed module, and the new lookup class
is a different module then

MODULE

access is lost.

If the new lookup class differs from the old one then

UNCONDITIONAL

is lost.

If the new lookup class is in a different package
than the old one, protected and default (package) members will not be accessible.

If the new lookup class is not within the same package member
as the old one, private members will not be accessible, and protected members
will not be accessible by virtue of inheritance.
(Protected members may continue to be accessible because of package sharing.)

If the new lookup class is not accessible to the old lookup class,
then no members, not even public members, will be accessible.
(In all other cases, public members will continue to be accessible.)

The resulting lookup's capabilities for loading classes
(used during

findClass(java.lang.String)

invocations)
are determined by the lookup class' loader,
which may change due to this operation.

dropLookupMode

```java
public
MethodHandles.Lookup
dropLookupMode​(int modeToDrop)
```

Creates a lookup on the same lookup class which this lookup object
finds members, but with a lookup mode that has lost the given lookup mode.
The lookup mode to drop is one of

PUBLIC

,

MODULE

,

PACKAGE

,

PROTECTED

or

PRIVATE

.

PROTECTED

and

UNCONDITIONAL

are always
dropped and so the resulting lookup mode will never have these access capabilities.
When dropping

PACKAGE

then the resulting lookup will not have

PACKAGE

or

PRIVATE

access. When dropping

MODULE

then the resulting lookup will
not have

MODULE

,

PACKAGE

, or

PRIVATE

access. If

PUBLIC

is dropped then the resulting lookup has no access.

**Parameters:** modeToDrop

- the lookup mode to drop
**Returns:** a lookup object which lacks the indicated mode, or the same object if there is no change
**Throws:** IllegalArgumentException

- if

modeToDrop

is not one of

PUBLIC

,

MODULE

,

PACKAGE

,

PROTECTED

,

PRIVATE

or

UNCONDITIONAL
**Since:** 9
**See Also:** MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

---

#### dropLookupMode

public

MethodHandles.Lookup

dropLookupMode​(int modeToDrop)

Creates a lookup on the same lookup class which this lookup object
finds members, but with a lookup mode that has lost the given lookup mode.
The lookup mode to drop is one of

PUBLIC

,

MODULE

,

PACKAGE

,

PROTECTED

or

PRIVATE

.

PROTECTED

and

UNCONDITIONAL

are always
dropped and so the resulting lookup mode will never have these access capabilities.
When dropping

PACKAGE

then the resulting lookup will not have

PACKAGE

or

PRIVATE

access. When dropping

MODULE

then the resulting lookup will
not have

MODULE

,

PACKAGE

, or

PRIVATE

access. If

PUBLIC

is dropped then the resulting lookup has no access.

defineClass

```java
public
Class
<?> defineClass​(byte[] bytes)
throws
IllegalAccessException
```

Defines a class to the same class loader and in the same runtime package and

protection domain

as this lookup's

lookup class

.

The

lookup modes

for this lookup must include

PACKAGE

access as default (package) members will be
accessible to the class. The

PACKAGE

lookup mode serves to authenticate
that the lookup object was created by a caller in the runtime package (or derived
from a lookup originally created by suitably privileged code to a target class in
the runtime package).

The

bytes

parameter is the class bytes of a valid class file (as defined
by the

The Java Virtual Machine Specification

) with a class name in the
same package as the lookup class.

This method does not run the class initializer. The class initializer may
run at a later time, as detailed in section 12.4 of the

The Java Language
Specification

.

If there is a security manager, its

checkPermission

method is first called
to check

RuntimePermission("defineClass")

.

**Parameters:** bytes

- the class bytes
**Returns:** the

Class

object for the class
**Throws:** IllegalArgumentException

- the bytes are for a class in a different package
to the lookup class
**Throws:** IllegalAccessException

- if this lookup does not have

PACKAGE

access
**Throws:** LinkageError

- if the class is malformed (

ClassFormatError

), cannot be
verified (

VerifyError

), is already defined, or another linkage error occurs
**Throws:** SecurityException

- if denied by the security manager
**Throws:** NullPointerException

- if

bytes

is

null
**Since:** 9
**See Also:** MethodHandles.privateLookupIn(java.lang.Class<?>, java.lang.invoke.MethodHandles.Lookup)

,

dropLookupMode(int)

,

ClassLoader.defineClass(String,byte[],int,int,ProtectionDomain)

---

#### defineClass

public

Class

<?> defineClass​(byte[] bytes)
throws

IllegalAccessException

Defines a class to the same class loader and in the same runtime package and

protection domain

as this lookup's

lookup class

.

The

lookup modes

for this lookup must include

PACKAGE

access as default (package) members will be
accessible to the class. The

PACKAGE

lookup mode serves to authenticate
that the lookup object was created by a caller in the runtime package (or derived
from a lookup originally created by suitably privileged code to a target class in
the runtime package).

The

bytes

parameter is the class bytes of a valid class file (as defined
by the

The Java Virtual Machine Specification

) with a class name in the
same package as the lookup class.

This method does not run the class initializer. The class initializer may
run at a later time, as detailed in section 12.4 of the

The Java Language
Specification

.

If there is a security manager, its

checkPermission

method is first called
to check

RuntimePermission("defineClass")

.

The

lookup modes

for this lookup must include

PACKAGE

access as default (package) members will be
accessible to the class. The

PACKAGE

lookup mode serves to authenticate
that the lookup object was created by a caller in the runtime package (or derived
from a lookup originally created by suitably privileged code to a target class in
the runtime package).

The

bytes

parameter is the class bytes of a valid class file (as defined
by the

The Java Virtual Machine Specification

) with a class name in the
same package as the lookup class.

This method does not run the class initializer. The class initializer may
run at a later time, as detailed in section 12.4 of the

The Java Language
Specification

.

If there is a security manager, its

checkPermission

method is first called
to check

RuntimePermission("defineClass")

.

toString

```java
public
String
toString()
```

Displays the name of the class from which lookups are to be made.
(The name is the one reported by

Class.getName

.)
If there are restrictions on the access permitted to this lookup,
this is indicated by adding a suffix to the class name, consisting
of a slash and a keyword. The keyword represents the strongest
allowed access, and is chosen as follows:

- If no access is allowed, the suffix is "/noaccess".

If only public access to types in exported packages is allowed, the suffix is "/public".

If only public access and unconditional access are allowed, the suffix is "/publicLookup".

If only public and module access are allowed, the suffix is "/module".

If only public, module and package access are allowed, the suffix is "/package".

If only public, module, package, and private access are allowed, the suffix is "/private".

If none of the above cases apply, it is the case that full
access (public, module, package, private, and protected) is allowed.
In this case, no suffix is added.
This is true only of an object obtained originally from

MethodHandles.lookup

.
Objects created by

Lookup.in

always have restricted access, and will display a suffix.

(It may seem strange that protected access should be
stronger than private access. Viewed independently from
package access, protected access is the first to be lost,
because it requires a direct subclass relationship between
caller and callee.)

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.
**See Also:** in(java.lang.Class<?>)

---

#### toString

public

String

toString()

Displays the name of the class from which lookups are to be made.
(The name is the one reported by

Class.getName

.)
If there are restrictions on the access permitted to this lookup,
this is indicated by adding a suffix to the class name, consisting
of a slash and a keyword. The keyword represents the strongest
allowed access, and is chosen as follows:

- If no access is allowed, the suffix is "/noaccess".

If only public access to types in exported packages is allowed, the suffix is "/public".

If only public access and unconditional access are allowed, the suffix is "/publicLookup".

If only public and module access are allowed, the suffix is "/module".

If only public, module and package access are allowed, the suffix is "/package".

If only public, module, package, and private access are allowed, the suffix is "/private".

If none of the above cases apply, it is the case that full
access (public, module, package, private, and protected) is allowed.
In this case, no suffix is added.
This is true only of an object obtained originally from

MethodHandles.lookup

.
Objects created by

Lookup.in

always have restricted access, and will display a suffix.

(It may seem strange that protected access should be
stronger than private access. Viewed independently from
package access, protected access is the first to be lost,
because it requires a direct subclass relationship between
caller and callee.)

If no access is allowed, the suffix is "/noaccess".

If only public access to types in exported packages is allowed, the suffix is "/public".

If only public access and unconditional access are allowed, the suffix is "/publicLookup".

If only public and module access are allowed, the suffix is "/module".

If only public, module and package access are allowed, the suffix is "/package".

If only public, module, package, and private access are allowed, the suffix is "/private".

(It may seem strange that protected access should be
stronger than private access. Viewed independently from
package access, protected access is the first to be lost,
because it requires a direct subclass relationship between
caller and callee.)

findStatic

```java
public
MethodHandle
findStatic​(
Class
<?> refc,

String
name,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces a method handle for a static method.
The type of the method handle will be that of the method.
(Since static methods do not take receivers, there is no
additional receiver argument inserted into the method handle type,
as there would be with

findVirtual

or

findSpecial

.)
The method and all its argument types must be accessible to the lookup object.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_asList = publicLookup().findStatic(Arrays.class,
"asList", methodType(List.class, Object[].class));
assertEquals("[x, y]", MH_asList.invoke("x", "y").toString());
```

**Parameters:** refc

- the class from which the method is accessed
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the method does not exist
**Throws:** IllegalAccessException

- if access checking fails,
or if the method is not

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

---

#### findStatic

public

MethodHandle

findStatic​(

Class

<?> refc,

String

name,

MethodType

type)
throws

NoSuchMethodException

,

IllegalAccessException

Produces a method handle for a static method.
The type of the method handle will be that of the method.
(Since static methods do not take receivers, there is no
additional receiver argument inserted into the method handle type,
as there would be with

findVirtual

or

findSpecial

.)
The method and all its argument types must be accessible to the lookup object.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_asList = publicLookup().findStatic(Arrays.class,
"asList", methodType(List.class, Object[].class));
assertEquals("[x, y]", MH_asList.invoke("x", "y").toString());
```

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_asList = publicLookup().findStatic(Arrays.class,
"asList", methodType(List.class, Object[].class));
assertEquals("[x, y]", MH_asList.invoke("x", "y").toString());
```

If the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_asList = publicLookup().findStatic(Arrays.class,
"asList", methodType(List.class, Object[].class));
assertEquals("[x, y]", MH_asList.invoke("x", "y").toString());
```

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_asList = publicLookup().findStatic(Arrays.class,
"asList", methodType(List.class, Object[].class));
assertEquals("[x, y]", MH_asList.invoke("x", "y").toString());
```

import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_asList = publicLookup().findStatic(Arrays.class,
"asList", methodType(List.class, Object[].class));
assertEquals("[x, y]", MH_asList.invoke("x", "y").toString());

findVirtual

```java
public
MethodHandle
findVirtual​(
Class
<?> refc,

String
name,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces a method handle for a virtual method.
The type of the method handle will be that of the method,
with the receiver type (usually

refc

) prepended.
The method and all its argument types must be accessible to the lookup object.

When called, the handle will treat the first argument as a receiver
and, for non-private methods, dispatch on the receiver's type to determine which method
implementation to enter.
For private methods the named method in

refc

will be invoked on the receiver.
(The dispatching action is identical with that performed by an

invokevirtual

or

invokeinterface

instruction.)

The first argument will be of type

refc

if the lookup
class has full privileges to access the member. Otherwise
the member must be

protected

and the first argument
will be restricted in type to the lookup class.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

Because of the general

equivalence

between

invokevirtual

instructions and method handles produced by

findVirtual

,
if the class is

MethodHandle

and the name string is

invokeExact

or

invoke

, the resulting
method handle is equivalent to one produced by

MethodHandles.exactInvoker

or

MethodHandles.invoker

with the same

type

argument.

If the class is

VarHandle

and the name string corresponds to
the name of a signature-polymorphic access mode method, the resulting
method handle is equivalent to one produced by

MethodHandles.varHandleInvoker(java.lang.invoke.VarHandle.AccessMode, java.lang.invoke.MethodType)

with
the access mode corresponding to the name string and with the same

type

arguments.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_concat = publicLookup().findVirtual(String.class,
"concat", methodType(String.class, String.class));
MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
"hashCode", methodType(int.class));
MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
"hashCode", methodType(int.class));
assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
// interface method:
MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
"subSequence", methodType(CharSequence.class, int.class, int.class));
assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
// constructor "internal method" must be accessed differently:
MethodType MT_newString = methodType(void.class); //()V for new String()
try { assertEquals("impossible", lookup()
.findVirtual(String.class, "<init>", MT_newString));
} catch (NoSuchMethodException ex) { } // OK
MethodHandle MH_newString = publicLookup()
.findConstructor(String.class, MT_newString);
assertEquals("", (String) MH_newString.invokeExact());
```

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method, with the receiver argument omitted
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the method does not exist
**Throws:** IllegalAccessException

- if access checking fails,
or if the method is

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

---

#### findVirtual

public

MethodHandle

findVirtual​(

Class

<?> refc,

String

name,

MethodType

type)
throws

NoSuchMethodException

,

IllegalAccessException

Produces a method handle for a virtual method.
The type of the method handle will be that of the method,
with the receiver type (usually

refc

) prepended.
The method and all its argument types must be accessible to the lookup object.

When called, the handle will treat the first argument as a receiver
and, for non-private methods, dispatch on the receiver's type to determine which method
implementation to enter.
For private methods the named method in

refc

will be invoked on the receiver.
(The dispatching action is identical with that performed by an

invokevirtual

or

invokeinterface

instruction.)

The first argument will be of type

refc

if the lookup
class has full privileges to access the member. Otherwise
the member must be

protected

and the first argument
will be restricted in type to the lookup class.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

Because of the general

equivalence

between

invokevirtual

instructions and method handles produced by

findVirtual

,
if the class is

MethodHandle

and the name string is

invokeExact

or

invoke

, the resulting
method handle is equivalent to one produced by

MethodHandles.exactInvoker

or

MethodHandles.invoker

with the same

type

argument.

If the class is

VarHandle

and the name string corresponds to
the name of a signature-polymorphic access mode method, the resulting
method handle is equivalent to one produced by

MethodHandles.varHandleInvoker(java.lang.invoke.VarHandle.AccessMode, java.lang.invoke.MethodType)

with
the access mode corresponding to the name string and with the same

type

arguments.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_concat = publicLookup().findVirtual(String.class,
"concat", methodType(String.class, String.class));
MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
"hashCode", methodType(int.class));
MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
"hashCode", methodType(int.class));
assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
// interface method:
MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
"subSequence", methodType(CharSequence.class, int.class, int.class));
assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
// constructor "internal method" must be accessed differently:
MethodType MT_newString = methodType(void.class); //()V for new String()
try { assertEquals("impossible", lookup()
.findVirtual(String.class, "<init>", MT_newString));
} catch (NoSuchMethodException ex) { } // OK
MethodHandle MH_newString = publicLookup()
.findConstructor(String.class, MT_newString);
assertEquals("", (String) MH_newString.invokeExact());
```

When called, the handle will treat the first argument as a receiver
and, for non-private methods, dispatch on the receiver's type to determine which method
implementation to enter.
For private methods the named method in

refc

will be invoked on the receiver.
(The dispatching action is identical with that performed by an

invokevirtual

or

invokeinterface

instruction.)

The first argument will be of type

refc

if the lookup
class has full privileges to access the member. Otherwise
the member must be

protected

and the first argument
will be restricted in type to the lookup class.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

Because of the general

equivalence

between

invokevirtual

instructions and method handles produced by

findVirtual

,
if the class is

MethodHandle

and the name string is

invokeExact

or

invoke

, the resulting
method handle is equivalent to one produced by

MethodHandles.exactInvoker

or

MethodHandles.invoker

with the same

type

argument.

If the class is

VarHandle

and the name string corresponds to
the name of a signature-polymorphic access mode method, the resulting
method handle is equivalent to one produced by

MethodHandles.varHandleInvoker(java.lang.invoke.VarHandle.AccessMode, java.lang.invoke.MethodType)

with
the access mode corresponding to the name string and with the same

type

arguments.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_concat = publicLookup().findVirtual(String.class,
"concat", methodType(String.class, String.class));
MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
"hashCode", methodType(int.class));
MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
"hashCode", methodType(int.class));
assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
// interface method:
MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
"subSequence", methodType(CharSequence.class, int.class, int.class));
assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
// constructor "internal method" must be accessed differently:
MethodType MT_newString = methodType(void.class); //()V for new String()
try { assertEquals("impossible", lookup()
.findVirtual(String.class, "<init>", MT_newString));
} catch (NoSuchMethodException ex) { } // OK
MethodHandle MH_newString = publicLookup()
.findConstructor(String.class, MT_newString);
assertEquals("", (String) MH_newString.invokeExact());
```

The first argument will be of type

refc

if the lookup
class has full privileges to access the member. Otherwise
the member must be

protected

and the first argument
will be restricted in type to the lookup class.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

Because of the general

equivalence

between

invokevirtual

instructions and method handles produced by

findVirtual

,
if the class is

MethodHandle

and the name string is

invokeExact

or

invoke

, the resulting
method handle is equivalent to one produced by

MethodHandles.exactInvoker

or

MethodHandles.invoker

with the same

type

argument.

If the class is

VarHandle

and the name string corresponds to
the name of a signature-polymorphic access mode method, the resulting
method handle is equivalent to one produced by

MethodHandles.varHandleInvoker(java.lang.invoke.VarHandle.AccessMode, java.lang.invoke.MethodType)

with
the access mode corresponding to the name string and with the same

type

arguments.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_concat = publicLookup().findVirtual(String.class,
"concat", methodType(String.class, String.class));
MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
"hashCode", methodType(int.class));
MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
"hashCode", methodType(int.class));
assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
// interface method:
MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
"subSequence", methodType(CharSequence.class, int.class, int.class));
assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
// constructor "internal method" must be accessed differently:
MethodType MT_newString = methodType(void.class); //()V for new String()
try { assertEquals("impossible", lookup()
.findVirtual(String.class, "<init>", MT_newString));
} catch (NoSuchMethodException ex) { } // OK
MethodHandle MH_newString = publicLookup()
.findConstructor(String.class, MT_newString);
assertEquals("", (String) MH_newString.invokeExact());
```

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

Because of the general

equivalence

between

invokevirtual

instructions and method handles produced by

findVirtual

,
if the class is

MethodHandle

and the name string is

invokeExact

or

invoke

, the resulting
method handle is equivalent to one produced by

MethodHandles.exactInvoker

or

MethodHandles.invoker

with the same

type

argument.

If the class is

VarHandle

and the name string corresponds to
the name of a signature-polymorphic access mode method, the resulting
method handle is equivalent to one produced by

MethodHandles.varHandleInvoker(java.lang.invoke.VarHandle.AccessMode, java.lang.invoke.MethodType)

with
the access mode corresponding to the name string and with the same

type

arguments.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_concat = publicLookup().findVirtual(String.class,
"concat", methodType(String.class, String.class));
MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
"hashCode", methodType(int.class));
MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
"hashCode", methodType(int.class));
assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
// interface method:
MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
"subSequence", methodType(CharSequence.class, int.class, int.class));
assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
// constructor "internal method" must be accessed differently:
MethodType MT_newString = methodType(void.class); //()V for new String()
try { assertEquals("impossible", lookup()
.findVirtual(String.class, "<init>", MT_newString));
} catch (NoSuchMethodException ex) { } // OK
MethodHandle MH_newString = publicLookup()
.findConstructor(String.class, MT_newString);
assertEquals("", (String) MH_newString.invokeExact());
```

Because of the general

equivalence

between

invokevirtual

instructions and method handles produced by

findVirtual

,
if the class is

MethodHandle

and the name string is

invokeExact

or

invoke

, the resulting
method handle is equivalent to one produced by

MethodHandles.exactInvoker

or

MethodHandles.invoker

with the same

type

argument.

If the class is

VarHandle

and the name string corresponds to
the name of a signature-polymorphic access mode method, the resulting
method handle is equivalent to one produced by

MethodHandles.varHandleInvoker(java.lang.invoke.VarHandle.AccessMode, java.lang.invoke.MethodType)

with
the access mode corresponding to the name string and with the same

type

arguments.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_concat = publicLookup().findVirtual(String.class,
"concat", methodType(String.class, String.class));
MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
"hashCode", methodType(int.class));
MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
"hashCode", methodType(int.class));
assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
// interface method:
MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
"subSequence", methodType(CharSequence.class, int.class, int.class));
assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
// constructor "internal method" must be accessed differently:
MethodType MT_newString = methodType(void.class); //()V for new String()
try { assertEquals("impossible", lookup()
.findVirtual(String.class, "<init>", MT_newString));
} catch (NoSuchMethodException ex) { } // OK
MethodHandle MH_newString = publicLookup()
.findConstructor(String.class, MT_newString);
assertEquals("", (String) MH_newString.invokeExact());
```

If the class is

VarHandle

and the name string corresponds to
the name of a signature-polymorphic access mode method, the resulting
method handle is equivalent to one produced by

MethodHandles.varHandleInvoker(java.lang.invoke.VarHandle.AccessMode, java.lang.invoke.MethodType)

with
the access mode corresponding to the name string and with the same

type

arguments.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_concat = publicLookup().findVirtual(String.class,
"concat", methodType(String.class, String.class));
MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
"hashCode", methodType(int.class));
MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
"hashCode", methodType(int.class));
assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
// interface method:
MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
"subSequence", methodType(CharSequence.class, int.class, int.class));
assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
// constructor "internal method" must be accessed differently:
MethodType MT_newString = methodType(void.class); //()V for new String()
try { assertEquals("impossible", lookup()
.findVirtual(String.class, "<init>", MT_newString));
} catch (NoSuchMethodException ex) { } // OK
MethodHandle MH_newString = publicLookup()
.findConstructor(String.class, MT_newString);
assertEquals("", (String) MH_newString.invokeExact());
```

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_concat = publicLookup().findVirtual(String.class,
"concat", methodType(String.class, String.class));
MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
"hashCode", methodType(int.class));
MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
"hashCode", methodType(int.class));
assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
// interface method:
MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
"subSequence", methodType(CharSequence.class, int.class, int.class));
assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
// constructor "internal method" must be accessed differently:
MethodType MT_newString = methodType(void.class); //()V for new String()
try { assertEquals("impossible", lookup()
.findVirtual(String.class, "<init>", MT_newString));
} catch (NoSuchMethodException ex) { } // OK
MethodHandle MH_newString = publicLookup()
.findConstructor(String.class, MT_newString);
assertEquals("", (String) MH_newString.invokeExact());
```

import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_concat = publicLookup().findVirtual(String.class,
"concat", methodType(String.class, String.class));
MethodHandle MH_hashCode = publicLookup().findVirtual(Object.class,
"hashCode", methodType(int.class));
MethodHandle MH_hashCode_String = publicLookup().findVirtual(String.class,
"hashCode", methodType(int.class));
assertEquals("xy", (String) MH_concat.invokeExact("x", "y"));
assertEquals("xy".hashCode(), (int) MH_hashCode.invokeExact((Object)"xy"));
assertEquals("xy".hashCode(), (int) MH_hashCode_String.invokeExact("xy"));
// interface method:
MethodHandle MH_subSequence = publicLookup().findVirtual(CharSequence.class,
"subSequence", methodType(CharSequence.class, int.class, int.class));
assertEquals("def", MH_subSequence.invoke("abcdefghi", 3, 6).toString());
// constructor "internal method" must be accessed differently:
MethodType MT_newString = methodType(void.class); //()V for new String()
try { assertEquals("impossible", lookup()
.findVirtual(String.class, "<init>", MT_newString));
} catch (NoSuchMethodException ex) { } // OK
MethodHandle MH_newString = publicLookup()
.findConstructor(String.class, MT_newString);
assertEquals("", (String) MH_newString.invokeExact());

findConstructor

```java
public
MethodHandle
findConstructor​(
Class
<?> refc,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces a method handle which creates an object and initializes it, using
the constructor of the specified type.
The parameter types of the method handle will be those of the constructor,
while the return type will be a reference to the constructor's class.
The constructor and all its argument types must be accessible to the lookup object.

The requested type must have a return type of

void

.
(This is consistent with the JVM's treatment of constructor type descriptors.)

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_newArrayList = publicLookup().findConstructor(
ArrayList.class, methodType(void.class, Collection.class));
Collection orig = Arrays.asList("x", "y");
Collection copy = (ArrayList) MH_newArrayList.invokeExact(orig);
assert(orig != copy);
assertEquals(orig, copy);
// a variable-arity constructor:
MethodHandle MH_newProcessBuilder = publicLookup().findConstructor(
ProcessBuilder.class, methodType(void.class, String[].class));
ProcessBuilder pb = (ProcessBuilder)
MH_newProcessBuilder.invoke("x", "y", "z");
assertEquals("[x, y, z]", pb.command().toString());
```

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** type

- the type of the method, with the receiver argument omitted, and a void return type
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the constructor does not exist
**Throws:** IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

---

#### findConstructor

public

MethodHandle

findConstructor​(

Class

<?> refc,

MethodType

type)
throws

NoSuchMethodException

,

IllegalAccessException

Produces a method handle which creates an object and initializes it, using
the constructor of the specified type.
The parameter types of the method handle will be those of the constructor,
while the return type will be a reference to the constructor's class.
The constructor and all its argument types must be accessible to the lookup object.

The requested type must have a return type of

void

.
(This is consistent with the JVM's treatment of constructor type descriptors.)

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_newArrayList = publicLookup().findConstructor(
ArrayList.class, methodType(void.class, Collection.class));
Collection orig = Arrays.asList("x", "y");
Collection copy = (ArrayList) MH_newArrayList.invokeExact(orig);
assert(orig != copy);
assertEquals(orig, copy);
// a variable-arity constructor:
MethodHandle MH_newProcessBuilder = publicLookup().findConstructor(
ProcessBuilder.class, methodType(void.class, String[].class));
ProcessBuilder pb = (ProcessBuilder)
MH_newProcessBuilder.invoke("x", "y", "z");
assertEquals("[x, y, z]", pb.command().toString());
```

The requested type must have a return type of

void

.
(This is consistent with the JVM's treatment of constructor type descriptors.)

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_newArrayList = publicLookup().findConstructor(
ArrayList.class, methodType(void.class, Collection.class));
Collection orig = Arrays.asList("x", "y");
Collection copy = (ArrayList) MH_newArrayList.invokeExact(orig);
assert(orig != copy);
assertEquals(orig, copy);
// a variable-arity constructor:
MethodHandle MH_newProcessBuilder = publicLookup().findConstructor(
ProcessBuilder.class, methodType(void.class, String[].class));
ProcessBuilder pb = (ProcessBuilder)
MH_newProcessBuilder.invoke("x", "y", "z");
assertEquals("[x, y, z]", pb.command().toString());
```

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_newArrayList = publicLookup().findConstructor(
ArrayList.class, methodType(void.class, Collection.class));
Collection orig = Arrays.asList("x", "y");
Collection copy = (ArrayList) MH_newArrayList.invokeExact(orig);
assert(orig != copy);
assertEquals(orig, copy);
// a variable-arity constructor:
MethodHandle MH_newProcessBuilder = publicLookup().findConstructor(
ProcessBuilder.class, methodType(void.class, String[].class));
ProcessBuilder pb = (ProcessBuilder)
MH_newProcessBuilder.invoke("x", "y", "z");
assertEquals("[x, y, z]", pb.command().toString());
```

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_newArrayList = publicLookup().findConstructor(
ArrayList.class, methodType(void.class, Collection.class));
Collection orig = Arrays.asList("x", "y");
Collection copy = (ArrayList) MH_newArrayList.invokeExact(orig);
assert(orig != copy);
assertEquals(orig, copy);
// a variable-arity constructor:
MethodHandle MH_newProcessBuilder = publicLookup().findConstructor(
ProcessBuilder.class, methodType(void.class, String[].class));
ProcessBuilder pb = (ProcessBuilder)
MH_newProcessBuilder.invoke("x", "y", "z");
assertEquals("[x, y, z]", pb.command().toString());
```

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_newArrayList = publicLookup().findConstructor(
ArrayList.class, methodType(void.class, Collection.class));
Collection orig = Arrays.asList("x", "y");
Collection copy = (ArrayList) MH_newArrayList.invokeExact(orig);
assert(orig != copy);
assertEquals(orig, copy);
// a variable-arity constructor:
MethodHandle MH_newProcessBuilder = publicLookup().findConstructor(
ProcessBuilder.class, methodType(void.class, String[].class));
ProcessBuilder pb = (ProcessBuilder)
MH_newProcessBuilder.invoke("x", "y", "z");
assertEquals("[x, y, z]", pb.command().toString());
```

import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle MH_newArrayList = publicLookup().findConstructor(
ArrayList.class, methodType(void.class, Collection.class));
Collection orig = Arrays.asList("x", "y");
Collection copy = (ArrayList) MH_newArrayList.invokeExact(orig);
assert(orig != copy);
assertEquals(orig, copy);
// a variable-arity constructor:
MethodHandle MH_newProcessBuilder = publicLookup().findConstructor(
ProcessBuilder.class, methodType(void.class, String[].class));
ProcessBuilder pb = (ProcessBuilder)
MH_newProcessBuilder.invoke("x", "y", "z");
assertEquals("[x, y, z]", pb.command().toString());

findClass

```java
public
Class
<?> findClass​(
String
targetName)
throws
ClassNotFoundException
,

IllegalAccessException
```

Looks up a class by name from the lookup context defined by this

Lookup

object. The static
initializer of the class is not run.

The lookup context here is determined by the

lookup class

, its class
loader, and the

lookup modes

. In particular, the method first attempts to
load the requested class, and then determines whether the class is accessible to this lookup object.

**Parameters:** targetName

- the fully qualified name of the class to be looked up.
**Returns:** the requested class.
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** LinkageError

- if the linkage fails
**Throws:** ClassNotFoundException

- if the class cannot be loaded by the lookup class' loader.
**Throws:** IllegalAccessException

- if the class is not accessible, using the allowed access
modes.
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Since:** 9

---

#### findClass

public

Class

<?> findClass​(

String

targetName)
throws

ClassNotFoundException

,

IllegalAccessException

Looks up a class by name from the lookup context defined by this

Lookup

object. The static
initializer of the class is not run.

The lookup context here is determined by the

lookup class

, its class
loader, and the

lookup modes

. In particular, the method first attempts to
load the requested class, and then determines whether the class is accessible to this lookup object.

The lookup context here is determined by the

lookup class

, its class
loader, and the

lookup modes

. In particular, the method first attempts to
load the requested class, and then determines whether the class is accessible to this lookup object.

accessClass

```java
public
Class
<?> accessClass​(
Class
<?> targetClass)
throws
IllegalAccessException
```

Determines if a class can be accessed from the lookup context defined by this

Lookup

object. The
static initializer of the class is not run.

The lookup context here is determined by the

lookup class

and the

lookup modes

.

**Parameters:** targetClass

- the class to be access-checked
**Returns:** the class that has been access-checked
**Throws:** IllegalAccessException

- if the class is not accessible from the lookup class, using the allowed access
modes.
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Since:** 9

---

#### accessClass

public

Class

<?> accessClass​(

Class

<?> targetClass)
throws

IllegalAccessException

Determines if a class can be accessed from the lookup context defined by this

Lookup

object. The
static initializer of the class is not run.

The lookup context here is determined by the

lookup class

and the

lookup modes

.

The lookup context here is determined by the

lookup class

and the

lookup modes

.

findSpecial

```java
public
MethodHandle
findSpecial​(
Class
<?> refc,

String
name,

MethodType
type,

Class
<?> specialCaller)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces an early-bound method handle for a virtual method.
It will bypass checks for overriding methods on the receiver,

as if called

from an

invokespecial

instruction from within the explicitly specified

specialCaller

.
The type of the method handle will be that of the method,
with a suitably restricted receiver type prepended.
(The receiver type will be

specialCaller

or a subtype.)
The method and all its argument types must be accessible
to the lookup object.

Before method resolution,
if the explicitly specified caller class is not identical with the
lookup class, or if this lookup object does not have

private access

privileges, the access fails.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

(Note: JVM internal methods named

"<init>"

are not visible to this API,
even though the

invokespecial

instruction can refer to them
in special circumstances. Use

findConstructor

to access instance initialization methods in a safe manner.)

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
static class Listie extends ArrayList {
public String toString() { return "[wee Listie]"; }
static Lookup lookup() { return MethodHandles.lookup(); }
}
...
// no access to constructor via invokeSpecial:
MethodHandle MH_newListie = Listie.lookup()
.findConstructor(Listie.class, methodType(void.class));
Listie l = (Listie) MH_newListie.invokeExact();
try { assertEquals("impossible", Listie.lookup().findSpecial(
Listie.class, "<init>", methodType(void.class), Listie.class));
} catch (NoSuchMethodException ex) { } // OK
// access to super and self methods via invokeSpecial:
MethodHandle MH_super = Listie.lookup().findSpecial(
ArrayList.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_this = Listie.lookup().findSpecial(
Listie.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_duper = Listie.lookup().findSpecial(
Object.class, "toString" , methodType(String.class), Listie.class);
assertEquals("[]", (String) MH_super.invokeExact(l));
assertEquals(""+l, (String) MH_this.invokeExact(l));
assertEquals("[]", (String) MH_duper.invokeExact(l)); // ArrayList method
try { assertEquals("inaccessible", Listie.lookup().findSpecial(
String.class, "toString", methodType(String.class), Listie.class));
} catch (IllegalAccessException ex) { } // OK
Listie subl = new Listie() { public String toString() { return "[subclass]"; } };
assertEquals(""+l, (String) MH_this.invokeExact(subl)); // Listie method
```

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the name of the method (which must not be "<init>")
**Parameters:** type

- the type of the method, with the receiver argument omitted
**Parameters:** specialCaller

- the proposed calling class to perform the

invokespecial
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the method does not exist
**Throws:** IllegalAccessException

- if access checking fails,
or if the method is

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

---

#### findSpecial

public

MethodHandle

findSpecial​(

Class

<?> refc,

String

name,

MethodType

type,

Class

<?> specialCaller)
throws

NoSuchMethodException

,

IllegalAccessException

Produces an early-bound method handle for a virtual method.
It will bypass checks for overriding methods on the receiver,

as if called

from an

invokespecial

instruction from within the explicitly specified

specialCaller

.
The type of the method handle will be that of the method,
with a suitably restricted receiver type prepended.
(The receiver type will be

specialCaller

or a subtype.)
The method and all its argument types must be accessible
to the lookup object.

Before method resolution,
if the explicitly specified caller class is not identical with the
lookup class, or if this lookup object does not have

private access

privileges, the access fails.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

(Note: JVM internal methods named

"<init>"

are not visible to this API,
even though the

invokespecial

instruction can refer to them
in special circumstances. Use

findConstructor

to access instance initialization methods in a safe manner.)

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
static class Listie extends ArrayList {
public String toString() { return "[wee Listie]"; }
static Lookup lookup() { return MethodHandles.lookup(); }
}
...
// no access to constructor via invokeSpecial:
MethodHandle MH_newListie = Listie.lookup()
.findConstructor(Listie.class, methodType(void.class));
Listie l = (Listie) MH_newListie.invokeExact();
try { assertEquals("impossible", Listie.lookup().findSpecial(
Listie.class, "<init>", methodType(void.class), Listie.class));
} catch (NoSuchMethodException ex) { } // OK
// access to super and self methods via invokeSpecial:
MethodHandle MH_super = Listie.lookup().findSpecial(
ArrayList.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_this = Listie.lookup().findSpecial(
Listie.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_duper = Listie.lookup().findSpecial(
Object.class, "toString" , methodType(String.class), Listie.class);
assertEquals("[]", (String) MH_super.invokeExact(l));
assertEquals(""+l, (String) MH_this.invokeExact(l));
assertEquals("[]", (String) MH_duper.invokeExact(l)); // ArrayList method
try { assertEquals("inaccessible", Listie.lookup().findSpecial(
String.class, "toString", methodType(String.class), Listie.class));
} catch (IllegalAccessException ex) { } // OK
Listie subl = new Listie() { public String toString() { return "[subclass]"; } };
assertEquals(""+l, (String) MH_this.invokeExact(subl)); // Listie method
```

Before method resolution,
if the explicitly specified caller class is not identical with the
lookup class, or if this lookup object does not have

private access

privileges, the access fails.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

(Note: JVM internal methods named

"<init>"

are not visible to this API,
even though the

invokespecial

instruction can refer to them
in special circumstances. Use

findConstructor

to access instance initialization methods in a safe manner.)

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
static class Listie extends ArrayList {
public String toString() { return "[wee Listie]"; }
static Lookup lookup() { return MethodHandles.lookup(); }
}
...
// no access to constructor via invokeSpecial:
MethodHandle MH_newListie = Listie.lookup()
.findConstructor(Listie.class, methodType(void.class));
Listie l = (Listie) MH_newListie.invokeExact();
try { assertEquals("impossible", Listie.lookup().findSpecial(
Listie.class, "<init>", methodType(void.class), Listie.class));
} catch (NoSuchMethodException ex) { } // OK
// access to super and self methods via invokeSpecial:
MethodHandle MH_super = Listie.lookup().findSpecial(
ArrayList.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_this = Listie.lookup().findSpecial(
Listie.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_duper = Listie.lookup().findSpecial(
Object.class, "toString" , methodType(String.class), Listie.class);
assertEquals("[]", (String) MH_super.invokeExact(l));
assertEquals(""+l, (String) MH_this.invokeExact(l));
assertEquals("[]", (String) MH_duper.invokeExact(l)); // ArrayList method
try { assertEquals("inaccessible", Listie.lookup().findSpecial(
String.class, "toString", methodType(String.class), Listie.class));
} catch (IllegalAccessException ex) { } // OK
Listie subl = new Listie() { public String toString() { return "[subclass]"; } };
assertEquals(""+l, (String) MH_this.invokeExact(subl)); // Listie method
```

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

(Note: JVM internal methods named

"<init>"

are not visible to this API,
even though the

invokespecial

instruction can refer to them
in special circumstances. Use

findConstructor

to access instance initialization methods in a safe manner.)

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
static class Listie extends ArrayList {
public String toString() { return "[wee Listie]"; }
static Lookup lookup() { return MethodHandles.lookup(); }
}
...
// no access to constructor via invokeSpecial:
MethodHandle MH_newListie = Listie.lookup()
.findConstructor(Listie.class, methodType(void.class));
Listie l = (Listie) MH_newListie.invokeExact();
try { assertEquals("impossible", Listie.lookup().findSpecial(
Listie.class, "<init>", methodType(void.class), Listie.class));
} catch (NoSuchMethodException ex) { } // OK
// access to super and self methods via invokeSpecial:
MethodHandle MH_super = Listie.lookup().findSpecial(
ArrayList.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_this = Listie.lookup().findSpecial(
Listie.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_duper = Listie.lookup().findSpecial(
Object.class, "toString" , methodType(String.class), Listie.class);
assertEquals("[]", (String) MH_super.invokeExact(l));
assertEquals(""+l, (String) MH_this.invokeExact(l));
assertEquals("[]", (String) MH_duper.invokeExact(l)); // ArrayList method
try { assertEquals("inaccessible", Listie.lookup().findSpecial(
String.class, "toString", methodType(String.class), Listie.class));
} catch (IllegalAccessException ex) { } // OK
Listie subl = new Listie() { public String toString() { return "[subclass]"; } };
assertEquals(""+l, (String) MH_this.invokeExact(subl)); // Listie method
```

(Note: JVM internal methods named

"<init>"

are not visible to this API,
even though the

invokespecial

instruction can refer to them
in special circumstances. Use

findConstructor

to access instance initialization methods in a safe manner.)

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
static class Listie extends ArrayList {
public String toString() { return "[wee Listie]"; }
static Lookup lookup() { return MethodHandles.lookup(); }
}
...
// no access to constructor via invokeSpecial:
MethodHandle MH_newListie = Listie.lookup()
.findConstructor(Listie.class, methodType(void.class));
Listie l = (Listie) MH_newListie.invokeExact();
try { assertEquals("impossible", Listie.lookup().findSpecial(
Listie.class, "<init>", methodType(void.class), Listie.class));
} catch (NoSuchMethodException ex) { } // OK
// access to super and self methods via invokeSpecial:
MethodHandle MH_super = Listie.lookup().findSpecial(
ArrayList.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_this = Listie.lookup().findSpecial(
Listie.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_duper = Listie.lookup().findSpecial(
Object.class, "toString" , methodType(String.class), Listie.class);
assertEquals("[]", (String) MH_super.invokeExact(l));
assertEquals(""+l, (String) MH_this.invokeExact(l));
assertEquals("[]", (String) MH_duper.invokeExact(l)); // ArrayList method
try { assertEquals("inaccessible", Listie.lookup().findSpecial(
String.class, "toString", methodType(String.class), Listie.class));
} catch (IllegalAccessException ex) { } // OK
Listie subl = new Listie() { public String toString() { return "[subclass]"; } };
assertEquals(""+l, (String) MH_this.invokeExact(subl)); // Listie method
```

Example:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
static class Listie extends ArrayList {
public String toString() { return "[wee Listie]"; }
static Lookup lookup() { return MethodHandles.lookup(); }
}
...
// no access to constructor via invokeSpecial:
MethodHandle MH_newListie = Listie.lookup()
.findConstructor(Listie.class, methodType(void.class));
Listie l = (Listie) MH_newListie.invokeExact();
try { assertEquals("impossible", Listie.lookup().findSpecial(
Listie.class, "<init>", methodType(void.class), Listie.class));
} catch (NoSuchMethodException ex) { } // OK
// access to super and self methods via invokeSpecial:
MethodHandle MH_super = Listie.lookup().findSpecial(
ArrayList.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_this = Listie.lookup().findSpecial(
Listie.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_duper = Listie.lookup().findSpecial(
Object.class, "toString" , methodType(String.class), Listie.class);
assertEquals("[]", (String) MH_super.invokeExact(l));
assertEquals(""+l, (String) MH_this.invokeExact(l));
assertEquals("[]", (String) MH_duper.invokeExact(l)); // ArrayList method
try { assertEquals("inaccessible", Listie.lookup().findSpecial(
String.class, "toString", methodType(String.class), Listie.class));
} catch (IllegalAccessException ex) { } // OK
Listie subl = new Listie() { public String toString() { return "[subclass]"; } };
assertEquals(""+l, (String) MH_this.invokeExact(subl)); // Listie method
```

import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
static class Listie extends ArrayList {
public String toString() { return "[wee Listie]"; }
static Lookup lookup() { return MethodHandles.lookup(); }
}
...
// no access to constructor via invokeSpecial:
MethodHandle MH_newListie = Listie.lookup()
.findConstructor(Listie.class, methodType(void.class));
Listie l = (Listie) MH_newListie.invokeExact();
try { assertEquals("impossible", Listie.lookup().findSpecial(
Listie.class, "<init>", methodType(void.class), Listie.class));
} catch (NoSuchMethodException ex) { } // OK
// access to super and self methods via invokeSpecial:
MethodHandle MH_super = Listie.lookup().findSpecial(
ArrayList.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_this = Listie.lookup().findSpecial(
Listie.class, "toString" , methodType(String.class), Listie.class);
MethodHandle MH_duper = Listie.lookup().findSpecial(
Object.class, "toString" , methodType(String.class), Listie.class);
assertEquals("[]", (String) MH_super.invokeExact(l));
assertEquals(""+l, (String) MH_this.invokeExact(l));
assertEquals("[]", (String) MH_duper.invokeExact(l)); // ArrayList method
try { assertEquals("inaccessible", Listie.lookup().findSpecial(
String.class, "toString", methodType(String.class), Listie.class));
} catch (IllegalAccessException ex) { } // OK
Listie subl = new Listie() { public String toString() { return "[subclass]"; } };
assertEquals(""+l, (String) MH_this.invokeExact(subl)); // Listie method

findGetter

```java
public
MethodHandle
findGetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a method handle giving read access to a non-static field.
The type of the method handle will have a return type of the field's
value type.
The method handle's single argument will be the instance containing
the field.
Access checking is performed immediately on behalf of the lookup class.

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type
**Returns:** a method handle which can load values from the field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**See Also:** findVarHandle(Class, String, Class)

---

#### findGetter

public

MethodHandle

findGetter​(

Class

<?> refc,

String

name,

Class

<?> type)
throws

NoSuchFieldException

,

IllegalAccessException

Produces a method handle giving read access to a non-static field.
The type of the method handle will have a return type of the field's
value type.
The method handle's single argument will be the instance containing
the field.
Access checking is performed immediately on behalf of the lookup class.

findSetter

```java
public
MethodHandle
findSetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a method handle giving write access to a non-static field.
The type of the method handle will have a void return type.
The method handle will take two arguments, the instance containing
the field, and the value to be stored.
The second argument will be of the field's value type.
Access checking is performed immediately on behalf of the lookup class.

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type
**Returns:** a method handle which can store values into the field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**See Also:** findVarHandle(Class, String, Class)

---

#### findSetter

public

MethodHandle

findSetter​(

Class

<?> refc,

String

name,

Class

<?> type)
throws

NoSuchFieldException

,

IllegalAccessException

Produces a method handle giving write access to a non-static field.
The type of the method handle will have a void return type.
The method handle will take two arguments, the instance containing
the field, and the value to be stored.
The second argument will be of the field's value type.
Access checking is performed immediately on behalf of the lookup class.

findVarHandle

```java
public
VarHandle
findVarHandle​(
Class
<?> recv,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a VarHandle giving access to a non-static field

name

of type

type

declared in a class of type

recv

.
The VarHandle's variable type is

type

and it has one
coordinate type,

recv

.

Access checking is performed immediately on behalf of the lookup
class.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

**API Note:** Bitwise comparison of

float

values or

double

values,
as performed by the numeric and atomic update access modes, differ
from the primitive

==

operator and the

Float.equals(java.lang.Object)

and

Double.equals(java.lang.Object)

methods, specifically with respect to
comparing NaN values or comparing

-0.0

with

+0.0

.
Care should be taken when performing a compare and set or a compare
and exchange operation with such values since the operation may
unexpectedly fail.
There are many possible NaN values that are considered to be

NaN

in Java, although no IEEE 754 floating-point operation
provided by Java can distinguish between them. Operation failure can
occur if the expected or witness value is a NaN value and it is
transformed (perhaps in a platform specific manner) into another NaN
value, and thus has a different bitwise representation (see

Float.intBitsToFloat(int)

or

Double.longBitsToDouble(long)

for more
details).
The values

-0.0

and

+0.0

have different bitwise
representations but are considered equal when using the primitive

==

operator. Operation failure can occur if, for example, a
numeric algorithm computes an expected value to be say

-0.0

and previously computed the witness value to be say

+0.0

.
**Parameters:** recv

- the receiver class, of type

R

, that declares the
non-static field
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type, of type

T
**Returns:** a VarHandle giving access to non-static fields.
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**Since:** 9

---

#### findVarHandle

public

VarHandle

findVarHandle​(

Class

<?> recv,

String

name,

Class

<?> type)
throws

NoSuchFieldException

,

IllegalAccessException

Produces a VarHandle giving access to a non-static field

name

of type

type

declared in a class of type

recv

.
The VarHandle's variable type is

type

and it has one
coordinate type,

recv

.

Access checking is performed immediately on behalf of the lookup
class.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

Access checking is performed immediately on behalf of the lookup
class.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

findStaticGetter

```java
public
MethodHandle
findStaticGetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a method handle giving read access to a static field.
The type of the method handle will have a return type of the field's
value type.
The method handle will take no arguments.
Access checking is performed immediately on behalf of the lookup class.

If the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type
**Returns:** a method handle which can load values from the field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is not

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

---

#### findStaticGetter

public

MethodHandle

findStaticGetter​(

Class

<?> refc,

String

name,

Class

<?> type)
throws

NoSuchFieldException

,

IllegalAccessException

Produces a method handle giving read access to a static field.
The type of the method handle will have a return type of the field's
value type.
The method handle will take no arguments.
Access checking is performed immediately on behalf of the lookup class.

If the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

If the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

findStaticSetter

```java
public
MethodHandle
findStaticSetter​(
Class
<?> refc,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a method handle giving write access to a static field.
The type of the method handle will have a void return type.
The method handle will take a single
argument, of the field's value type, the value to be stored.
Access checking is performed immediately on behalf of the lookup class.

If the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:** refc

- the class or interface from which the method is accessed
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type
**Returns:** a method handle which can store values into the field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is not

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null

---

#### findStaticSetter

public

MethodHandle

findStaticSetter​(

Class

<?> refc,

String

name,

Class

<?> type)
throws

NoSuchFieldException

,

IllegalAccessException

Produces a method handle giving write access to a static field.
The type of the method handle will have a void return type.
The method handle will take a single
argument, of the field's value type, the value to be stored.
Access checking is performed immediately on behalf of the lookup class.

If the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

If the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

findStaticVarHandle

```java
public
VarHandle
findStaticVarHandle​(
Class
<?> decl,

String
name,

Class
<?> type)
throws
NoSuchFieldException
,

IllegalAccessException
```

Produces a VarHandle giving access to a static field

name

of
type

type

declared in a class of type

decl

.
The VarHandle's variable type is

type

and it has no
coordinate types.

Access checking is performed immediately on behalf of the lookup
class.

If the returned VarHandle is operated on, the declaring class will be
initialized, if it has not already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

, then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

**API Note:** Bitwise comparison of

float

values or

double

values,
as performed by the numeric and atomic update access modes, differ
from the primitive

==

operator and the

Float.equals(java.lang.Object)

and

Double.equals(java.lang.Object)

methods, specifically with respect to
comparing NaN values or comparing

-0.0

with

+0.0

.
Care should be taken when performing a compare and set or a compare
and exchange operation with such values since the operation may
unexpectedly fail.
There are many possible NaN values that are considered to be

NaN

in Java, although no IEEE 754 floating-point operation
provided by Java can distinguish between them. Operation failure can
occur if the expected or witness value is a NaN value and it is
transformed (perhaps in a platform specific manner) into another NaN
value, and thus has a different bitwise representation (see

Float.intBitsToFloat(int)

or

Double.longBitsToDouble(long)

for more
details).
The values

-0.0

and

+0.0

have different bitwise
representations but are considered equal when using the primitive

==

operator. Operation failure can occur if, for example, a
numeric algorithm computes an expected value to be say

-0.0

and previously computed the witness value to be say

+0.0

.
**Parameters:** decl

- the class that declares the static field
**Parameters:** name

- the field's name
**Parameters:** type

- the field's type, of type

T
**Returns:** a VarHandle giving access to a static field
**Throws:** NoSuchFieldException

- if the field does not exist
**Throws:** IllegalAccessException

- if access checking fails, or if the field is not

static
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**Since:** 9

---

#### findStaticVarHandle

public

VarHandle

findStaticVarHandle​(

Class

<?> decl,

String

name,

Class

<?> type)
throws

NoSuchFieldException

,

IllegalAccessException

Produces a VarHandle giving access to a static field

name

of
type

type

declared in a class of type

decl

.
The VarHandle's variable type is

type

and it has no
coordinate types.

Access checking is performed immediately on behalf of the lookup
class.

If the returned VarHandle is operated on, the declaring class will be
initialized, if it has not already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

, then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

Access checking is performed immediately on behalf of the lookup
class.

If the returned VarHandle is operated on, the declaring class will be
initialized, if it has not already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

, then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

If the returned VarHandle is operated on, the declaring class will be
initialized, if it has not already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

, then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

, then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

, then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

bind

```java
public
MethodHandle
bind​(
Object
receiver,

String
name,

MethodType
type)
throws
NoSuchMethodException
,

IllegalAccessException
```

Produces an early-bound method handle for a non-static method.
The receiver must have a supertype

defc

in which a method
of the given name and type is accessible to the lookup class.
The method and all its argument types must be accessible to the lookup object.
The type of the method handle will be that of the method,
without any insertion of an additional receiver parameter.
The given receiver will be bound into the method handle,
so that every call to the method handle will invoke the
requested method on the given receiver.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set

and

the trailing array argument is not the only argument.
(If the trailing array argument is the only argument,
the given receiver value will be bound to it.)

This is almost equivalent to the following code, with some differences noted below:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle mh0 = lookup().findVirtual(defc, name, type);
MethodHandle mh1 = mh0.bindTo(receiver);
mh1 = mh1.withVarargs(mh0.isVarargsCollector());
return mh1;
```

where

defc

is either

receiver.getClass()

or a super
type of that class, in which the requested method is accessible
to the lookup class.
(Unlike

bind

,

bindTo

does not preserve variable arity.
Also,

bindTo

may throw a

ClassCastException

in instances where

bind

would
throw an

IllegalAccessException

, as in the case where the member is

protected

and
the receiver is restricted by

findVirtual

to the lookup class.)

**Parameters:** receiver

- the object from which the method is accessed
**Parameters:** name

- the name of the method
**Parameters:** type

- the type of the method, with the receiver argument omitted
**Returns:** the desired method handle
**Throws:** NoSuchMethodException

- if the method does not exist
**Throws:** IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** NullPointerException

- if any argument is null
**See Also:** MethodHandle.bindTo(java.lang.Object)

,

findVirtual(java.lang.Class<?>, java.lang.String, java.lang.invoke.MethodType)

---

#### bind

public

MethodHandle

bind​(

Object

receiver,

String

name,

MethodType

type)
throws

NoSuchMethodException

,

IllegalAccessException

Produces an early-bound method handle for a non-static method.
The receiver must have a supertype

defc

in which a method
of the given name and type is accessible to the lookup class.
The method and all its argument types must be accessible to the lookup object.
The type of the method handle will be that of the method,
without any insertion of an additional receiver parameter.
The given receiver will be bound into the method handle,
so that every call to the method handle will invoke the
requested method on the given receiver.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set

and

the trailing array argument is not the only argument.
(If the trailing array argument is the only argument,
the given receiver value will be bound to it.)

This is almost equivalent to the following code, with some differences noted below:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle mh0 = lookup().findVirtual(defc, name, type);
MethodHandle mh1 = mh0.bindTo(receiver);
mh1 = mh1.withVarargs(mh0.isVarargsCollector());
return mh1;
```

where

defc

is either

receiver.getClass()

or a super
type of that class, in which the requested method is accessible
to the lookup class.
(Unlike

bind

,

bindTo

does not preserve variable arity.
Also,

bindTo

may throw a

ClassCastException

in instances where

bind

would
throw an

IllegalAccessException

, as in the case where the member is

protected

and
the receiver is restricted by

findVirtual

to the lookup class.)

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set

and

the trailing array argument is not the only argument.
(If the trailing array argument is the only argument,
the given receiver value will be bound to it.)

This is almost equivalent to the following code, with some differences noted below:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle mh0 = lookup().findVirtual(defc, name, type);
MethodHandle mh1 = mh0.bindTo(receiver);
mh1 = mh1.withVarargs(mh0.isVarargsCollector());
return mh1;
```

where

defc

is either

receiver.getClass()

or a super
type of that class, in which the requested method is accessible
to the lookup class.
(Unlike

bind

,

bindTo

does not preserve variable arity.
Also,

bindTo

may throw a

ClassCastException

in instances where

bind

would
throw an

IllegalAccessException

, as in the case where the member is

protected

and
the receiver is restricted by

findVirtual

to the lookup class.)

This is almost equivalent to the following code, with some differences noted below:

```java
import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle mh0 = lookup().findVirtual(defc, name, type);
MethodHandle mh1 = mh0.bindTo(receiver);
mh1 = mh1.withVarargs(mh0.isVarargsCollector());
return mh1;
```

where

defc

is either

receiver.getClass()

or a super
type of that class, in which the requested method is accessible
to the lookup class.
(Unlike

bind

,

bindTo

does not preserve variable arity.
Also,

bindTo

may throw a

ClassCastException

in instances where

bind

would
throw an

IllegalAccessException

, as in the case where the member is

protected

and
the receiver is restricted by

findVirtual

to the lookup class.)

import static java.lang.invoke.MethodHandles.*;
import static java.lang.invoke.MethodType.*;
...
MethodHandle mh0 = lookup().findVirtual(defc, name, type);
MethodHandle mh1 = mh0.bindTo(receiver);
mh1 = mh1.withVarargs(mh0.isVarargsCollector());
return mh1;

unreflect

```java
public
MethodHandle
unreflect​(
Method
m)
throws
IllegalAccessException
```

Makes a

direct method handle

to

m

, if the lookup class has permission.
If

m

is non-static, the receiver argument is treated as an initial argument.
If

m

is virtual, overriding is respected on every call.
Unlike the Core Reflection API, exceptions are

not

wrapped.
The type of the method handle will be that of the method,
with the receiver type prepended (but only if it is non-static).
If the method's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.
If

m

is not public, do not share the resulting handle with untrusted parties.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

If

m

is static, and
if the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

**Parameters:** m

- the reflected method
**Returns:** a method handle which can invoke the reflected method
**Throws:** IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** NullPointerException

- if the argument is null

---

#### unreflect

public

MethodHandle

unreflect​(

Method

m)
throws

IllegalAccessException

Makes a

direct method handle

to

m

, if the lookup class has permission.
If

m

is non-static, the receiver argument is treated as an initial argument.
If

m

is virtual, overriding is respected on every call.
Unlike the Core Reflection API, exceptions are

not

wrapped.
The type of the method handle will be that of the method,
with the receiver type prepended (but only if it is non-static).
If the method's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.
If

m

is not public, do not share the resulting handle with untrusted parties.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

If

m

is static, and
if the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

If

m

is static, and
if the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

If

m

is static, and
if the returned method handle is invoked, the method's class will
be initialized, if it has not already been initialized.

unreflectSpecial

```java
public
MethodHandle
unreflectSpecial​(
Method
m,

Class
<?> specialCaller)
throws
IllegalAccessException
```

Produces a method handle for a reflected method.
It will bypass checks for overriding methods on the receiver,

as if called

from an

invokespecial

instruction from within the explicitly specified

specialCaller

.
The type of the method handle will be that of the method,
with a suitably restricted receiver type prepended.
(The receiver type will be

specialCaller

or a subtype.)
If the method's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class,
as if

invokespecial

instruction were being linked.

Before method resolution,
if the explicitly specified caller class is not identical with the
lookup class, or if this lookup object does not have

private access

privileges, the access fails.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

**Parameters:** m

- the reflected method
**Parameters:** specialCaller

- the class nominally calling the method
**Returns:** a method handle which can invoke the reflected method
**Throws:** IllegalAccessException

- if access checking fails,
or if the method is

static

,
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** NullPointerException

- if any argument is null

---

#### unreflectSpecial

public

MethodHandle

unreflectSpecial​(

Method

m,

Class

<?> specialCaller)
throws

IllegalAccessException

Produces a method handle for a reflected method.
It will bypass checks for overriding methods on the receiver,

as if called

from an

invokespecial

instruction from within the explicitly specified

specialCaller

.
The type of the method handle will be that of the method,
with a suitably restricted receiver type prepended.
(The receiver type will be

specialCaller

or a subtype.)
If the method's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class,
as if

invokespecial

instruction were being linked.

Before method resolution,
if the explicitly specified caller class is not identical with the
lookup class, or if this lookup object does not have

private access

privileges, the access fails.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

Before method resolution,
if the explicitly specified caller class is not identical with the
lookup class, or if this lookup object does not have

private access

privileges, the access fails.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

The returned method handle will have

variable arity

if and only if
the method's variable arity modifier bit (

0x0080

) is set.

unreflectConstructor

```java
public
MethodHandle
unreflectConstructor​(
Constructor
<?> c)
throws
IllegalAccessException
```

Produces a method handle for a reflected constructor.
The type of the method handle will be that of the constructor,
with the return type changed to the declaring class.
The method handle will perform a

newInstance

operation,
creating a new instance of the constructor's class on the
arguments passed to the method handle.

If the constructor's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

**Parameters:** c

- the reflected constructor
**Returns:** a method handle which can invoke the reflected constructor
**Throws:** IllegalAccessException

- if access checking fails
or if the method's variable arity modifier bit
is set and

asVarargsCollector

fails
**Throws:** NullPointerException

- if the argument is null

---

#### unreflectConstructor

public

MethodHandle

unreflectConstructor​(

Constructor

<?> c)
throws

IllegalAccessException

Produces a method handle for a reflected constructor.
The type of the method handle will be that of the constructor,
with the return type changed to the declaring class.
The method handle will perform a

newInstance

operation,
creating a new instance of the constructor's class on the
arguments passed to the method handle.

If the constructor's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

If the constructor's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

The returned method handle will have

variable arity

if and only if
the constructor's variable arity modifier bit (

0x0080

) is set.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

If the returned method handle is invoked, the constructor's class will
be initialized, if it has not already been initialized.

unreflectGetter

```java
public
MethodHandle
unreflectGetter​(
Field
f)
throws
IllegalAccessException
```

Produces a method handle giving read access to a reflected field.
The type of the method handle will have a return type of the field's
value type.
If the field is static, the method handle will take no arguments.
Otherwise, its single argument will be the instance containing
the field.
If the field's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

If the field is static, and
if the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:** f

- the reflected field
**Returns:** a method handle which can load values from the reflected field
**Throws:** IllegalAccessException

- if access checking fails
**Throws:** NullPointerException

- if the argument is null

---

#### unreflectGetter

public

MethodHandle

unreflectGetter​(

Field

f)
throws

IllegalAccessException

Produces a method handle giving read access to a reflected field.
The type of the method handle will have a return type of the field's
value type.
If the field is static, the method handle will take no arguments.
Otherwise, its single argument will be the instance containing
the field.
If the field's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

If the field is static, and
if the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

If the field is static, and
if the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

unreflectSetter

```java
public
MethodHandle
unreflectSetter​(
Field
f)
throws
IllegalAccessException
```

Produces a method handle giving write access to a reflected field.
The type of the method handle will have a void return type.
If the field is static, the method handle will take a single
argument, of the field's value type, the value to be stored.
Otherwise, the two arguments will be the instance containing
the field, and the value to be stored.
If the field's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

If the field is static, and
if the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

**Parameters:** f

- the reflected field
**Returns:** a method handle which can store values into the reflected field
**Throws:** IllegalAccessException

- if access checking fails
**Throws:** NullPointerException

- if the argument is null

---

#### unreflectSetter

public

MethodHandle

unreflectSetter​(

Field

f)
throws

IllegalAccessException

Produces a method handle giving write access to a reflected field.
The type of the method handle will have a void return type.
If the field is static, the method handle will take a single
argument, of the field's value type, the value to be stored.
Otherwise, the two arguments will be the instance containing
the field, and the value to be stored.
If the field's

accessible

flag is not set,
access checking is performed immediately on behalf of the lookup class.

If the field is static, and
if the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

If the field is static, and
if the returned method handle is invoked, the field's class will
be initialized, if it has not already been initialized.

unreflectVarHandle

```java
public
VarHandle
unreflectVarHandle​(
Field
f)
throws
IllegalAccessException
```

Produces a VarHandle giving access to a reflected field

f

of type

T

declared in a class of type

R

.
The VarHandle's variable type is

T

.
If the field is non-static the VarHandle has one coordinate type,

R

. Otherwise, the field is static, and the VarHandle has no
coordinate types.

Access checking is performed immediately on behalf of the lookup
class, regardless of the value of the field's

accessible

flag.

If the field is static, and if the returned VarHandle is operated
on, the field's declaring class will be initialized, if it has not
already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

**API Note:** Bitwise comparison of

float

values or

double

values,
as performed by the numeric and atomic update access modes, differ
from the primitive

==

operator and the

Float.equals(java.lang.Object)

and

Double.equals(java.lang.Object)

methods, specifically with respect to
comparing NaN values or comparing

-0.0

with

+0.0

.
Care should be taken when performing a compare and set or a compare
and exchange operation with such values since the operation may
unexpectedly fail.
There are many possible NaN values that are considered to be

NaN

in Java, although no IEEE 754 floating-point operation
provided by Java can distinguish between them. Operation failure can
occur if the expected or witness value is a NaN value and it is
transformed (perhaps in a platform specific manner) into another NaN
value, and thus has a different bitwise representation (see

Float.intBitsToFloat(int)

or

Double.longBitsToDouble(long)

for more
details).
The values

-0.0

and

+0.0

have different bitwise
representations but are considered equal when using the primitive

==

operator. Operation failure can occur if, for example, a
numeric algorithm computes an expected value to be say

-0.0

and previously computed the witness value to be say

+0.0

.
**Parameters:** f

- the reflected field, with a field of type

T

, and
a declaring class of type

R
**Returns:** a VarHandle giving access to non-static fields or a static
field
**Throws:** IllegalAccessException

- if access checking fails
**Throws:** NullPointerException

- if the argument is null
**Since:** 9

---

#### unreflectVarHandle

public

VarHandle

unreflectVarHandle​(

Field

f)
throws

IllegalAccessException

Produces a VarHandle giving access to a reflected field

f

of type

T

declared in a class of type

R

.
The VarHandle's variable type is

T

.
If the field is non-static the VarHandle has one coordinate type,

R

. Otherwise, the field is static, and the VarHandle has no
coordinate types.

Access checking is performed immediately on behalf of the lookup
class, regardless of the value of the field's

accessible

flag.

If the field is static, and if the returned VarHandle is operated
on, the field's declaring class will be initialized, if it has not
already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

Access checking is performed immediately on behalf of the lookup
class, regardless of the value of the field's

accessible

flag.

If the field is static, and if the returned VarHandle is operated
on, the field's declaring class will be initialized, if it has not
already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

If the field is static, and if the returned VarHandle is operated
on, the field's declaring class will be initialized, if it has not
already been initialized.

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

Certain access modes of the returned VarHandle are unsupported under
the following conditions:

- if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

if the field is declared

final

, then the write, atomic
update, numeric atomic update, and bitwise atomic update access
modes are unsupported.

if the field type is anything other than

byte

,

short

,

char

,

int

,

long

,

float

, or

double

then numeric atomic update
access modes are unsupported.

if the field type is anything other than

boolean

,

byte

,

short

,

char

,

int

or

long

then bitwise atomic update access modes are
unsupported.

If the field is declared

volatile

then the returned VarHandle
will override access to the field (effectively ignore the

volatile

declaration) in accordance to its specified
access modes.

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

If the field type is

float

or

double

then numeric
and atomic update access modes compare values using their bitwise
representation (see

Float.floatToRawIntBits(float)

and

Double.doubleToRawLongBits(double)

, respectively).

revealDirect

```java
public
MethodHandleInfo
revealDirect​(
MethodHandle
target)
```

Cracks a

direct method handle

created by this lookup object or a similar one.
Security and access checks are performed to ensure that this lookup object
is capable of reproducing the target method handle.
This means that the cracking may fail if target is a direct method handle
but was created by an unrelated lookup object.
This can happen if the method handle is

caller sensitive

and was created by a lookup object for a different class.

**Parameters:** target

- a direct method handle to crack into symbolic reference components
**Returns:** a symbolic reference which can be used to reconstruct this method handle from this lookup object
**Throws:** SecurityException

- if a security manager is present and it

refuses access
**Throws:** IllegalArgumentException

- if the target is not a direct method handle or if access checking fails
**Throws:** NullPointerException

- if the target is

null
**Since:** 1.8
**See Also:** MethodHandleInfo

---

#### revealDirect

public

MethodHandleInfo

revealDirect​(

MethodHandle

target)

Cracks a

direct method handle

created by this lookup object or a similar one.
Security and access checks are performed to ensure that this lookup object
is capable of reproducing the target method handle.
This means that the cracking may fail if target is a direct method handle
but was created by an unrelated lookup object.
This can happen if the method handle is

caller sensitive

and was created by a lookup object for a different class.

hasPrivateAccess

```java
public boolean hasPrivateAccess()
```

Returns

true

if this lookup has

PRIVATE

access.

**Returns:** true

if this lookup has

PRIVATE

access.
**Since:** 9

---

#### hasPrivateAccess

public boolean hasPrivateAccess()

Returns

true

if this lookup has

PRIVATE

access.

---

