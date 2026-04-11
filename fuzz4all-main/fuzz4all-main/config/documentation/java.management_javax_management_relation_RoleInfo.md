# Class RoleInfo

**Source:** `java.management\javax\management\relation\RoleInfo.html`

### Class Description

```java
public class
RoleInfo

extends
Object

implements
Serializable
```

A RoleInfo object summarises a role in a relation type.

The

serialVersionUID

of this class is

2504952983494636987L

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int ROLE_CARDINALITY_INFINITY

To specify an unlimited cardinality.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public RoleInfo​(
String
roleName,

String
mbeanClassName,
boolean read,
boolean write,
int min,
int max,

String
descr)
throws
IllegalArgumentException
,

InvalidRoleInfoException
,

ClassNotFoundException
,

NotCompliantMBeanException

Constructor.

**Parameters:**
- roleName

- name of the role.
- mbeanClassName

- name of the class of MBean(s) expected to
be referenced in corresponding role. If an MBean

M

is in
this role, then the MBean server must return true for

isInstanceOf(M, mbeanClassName)

.
- read

- flag to indicate if the corresponding role
can be read
- write

- flag to indicate if the corresponding role
can be set
- min

- minimum degree for role, i.e. minimum number of
MBeans to provide in corresponding role
Must be less than or equal to

max

.
(ROLE_CARDINALITY_INFINITY for unlimited)
- max

- maximum degree for role, i.e. maximum number of
MBeans to provide in corresponding role
Must be greater than or equal to

min

(ROLE_CARDINALITY_INFINITY for unlimited)
- descr

- description of the role (can be null)

**Throws:**
- IllegalArgumentException

- if null parameter
- InvalidRoleInfoException

- if the minimum degree is
greater than the maximum degree.
- ClassNotFoundException

- As of JMX 1.2, this exception
can no longer be thrown. It is retained in the declaration of
this class for compatibility with existing code.
- NotCompliantMBeanException

- if the class mbeanClassName
is not a MBean class.

---

#### public RoleInfo​(
String
roleName,

String
mbeanClassName,
boolean read,
boolean write)
throws
IllegalArgumentException
,

ClassNotFoundException
,

NotCompliantMBeanException

Constructor.

**Parameters:**
- roleName

- name of the role
- mbeanClassName

- name of the class of MBean(s) expected to
be referenced in corresponding role. If an MBean

M

is in
this role, then the MBean server must return true for

isInstanceOf(M, mbeanClassName)

.
- read

- flag to indicate if the corresponding role
can be read
- write

- flag to indicate if the corresponding role
can be set

Minimum and maximum degrees defaulted to 1.

Description of role defaulted to null.

**Throws:**
- IllegalArgumentException

- if null parameter
- ClassNotFoundException

- As of JMX 1.2, this exception
can no longer be thrown. It is retained in the declaration of
this class for compatibility with existing code.
- NotCompliantMBeanException

- As of JMX 1.2, this
exception can no longer be thrown. It is retained in the
declaration of this class for compatibility with existing code.

---

#### public RoleInfo​(
String
roleName,

String
mbeanClassName)
throws
IllegalArgumentException
,

ClassNotFoundException
,

NotCompliantMBeanException

Constructor.

**Parameters:**
- roleName

- name of the role
- mbeanClassName

- name of the class of MBean(s) expected to
be referenced in corresponding role. If an MBean

M

is in
this role, then the MBean server must return true for

isInstanceOf(M, mbeanClassName)

.

IsReadable and IsWritable defaulted to true.

Minimum and maximum degrees defaulted to 1.

Description of role defaulted to null.

**Throws:**
- IllegalArgumentException

- if null parameter
- ClassNotFoundException

- As of JMX 1.2, this exception
can no longer be thrown. It is retained in the declaration of
this class for compatibility with existing code.
- NotCompliantMBeanException

- As of JMX 1.2, this
exception can no longer be thrown. It is retained in the
declaration of this class for compatibility with existing code.

---

#### public RoleInfo​(
RoleInfo
roleInfo)
throws
IllegalArgumentException

Copy constructor.

**Parameters:**
- roleInfo

- the

RoleInfo

instance to be copied.

**Throws:**
- IllegalArgumentException

- if null parameter

---

### Method Details

#### public
String
getName()

Returns the name of the role.

**Returns:**
- the name of the role.

---

#### public boolean isReadable()

Returns read access mode for the role (true if it is readable).

**Returns:**
- true if the role is readable.

---

#### public boolean isWritable()

Returns write access mode for the role (true if it is writable).

**Returns:**
- true if the role is writable.

---

#### public
String
getDescription()

Returns description text for the role.

**Returns:**
- the description of the role.

---

#### public int getMinDegree()

Returns minimum degree for corresponding role reference.

**Returns:**
- the minimum degree.

---

#### public int getMaxDegree()

Returns maximum degree for corresponding role reference.

**Returns:**
- the maximum degree.

---

#### public
String
getRefMBeanClassName()

Returns name of type of MBean expected to be referenced in
corresponding role.

**Returns:**
- the name of the referenced type.

---

#### public boolean checkMinDegree​(int value)

Returns true if the

value

parameter is greater than or equal to
the expected minimum degree, false otherwise.

**Parameters:**
- value

- the value to be checked

**Returns:**
- true if greater than or equal to minimum degree, false otherwise.

---

#### public boolean checkMaxDegree​(int value)

Returns true if the

value

parameter is lower than or equal to
the expected maximum degree, false otherwise.

**Parameters:**
- value

- the value to be checked

**Returns:**
- true if lower than or equal to maximum degree, false otherwise.

---

#### public
String
toString()

Returns a string describing the role info.

**Overrides:**
- toString

in class

Object

**Returns:**
- a description of the role info.

---

### Additional Sections

#### Class RoleInfo

java.lang.Object

- javax.management.relation.RoleInfo

javax.management.relation.RoleInfo

**All Implemented Interfaces:** Serializable

```java
public class
RoleInfo

extends
Object

implements
Serializable
```

A RoleInfo object summarises a role in a relation type.

The

serialVersionUID

of this class is

2504952983494636987L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

RoleInfo

extends

Object

implements

Serializable

A RoleInfo object summarises a role in a relation type.

The

serialVersionUID

of this class is

2504952983494636987L

.

The

serialVersionUID

of this class is

2504952983494636987L

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ROLE_CARDINALITY_INFINITY

To specify an unlimited cardinality.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RoleInfo

​(

String

roleName,

String

mbeanClassName)

Constructor.

RoleInfo

​(

String

roleName,

String

mbeanClassName,
boolean read,
boolean write)

Constructor.

RoleInfo

​(

String

roleName,

String

mbeanClassName,
boolean read,
boolean write,
int min,
int max,

String

descr)

Constructor.

RoleInfo

​(

RoleInfo

roleInfo)

Copy constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

checkMaxDegree

​(int value)

Returns true if the

value

parameter is lower than or equal to
the expected maximum degree, false otherwise.

boolean

checkMinDegree

​(int value)

Returns true if the

value

parameter is greater than or equal to
the expected minimum degree, false otherwise.

String

getDescription

()

Returns description text for the role.

int

getMaxDegree

()

Returns maximum degree for corresponding role reference.

int

getMinDegree

()

Returns minimum degree for corresponding role reference.

String

getName

()

Returns the name of the role.

String

getRefMBeanClassName

()

Returns name of type of MBean expected to be referenced in
corresponding role.

boolean

isReadable

()

Returns read access mode for the role (true if it is readable).

boolean

isWritable

()

Returns write access mode for the role (true if it is writable).

String

toString

()

Returns a string describing the role info.

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

ROLE_CARDINALITY_INFINITY

To specify an unlimited cardinality.

---

#### Field Summary

To specify an unlimited cardinality.

Constructor Summary

Constructors

Constructor

Description

RoleInfo

​(

String

roleName,

String

mbeanClassName)

Constructor.

RoleInfo

​(

String

roleName,

String

mbeanClassName,
boolean read,
boolean write)

Constructor.

RoleInfo

​(

String

roleName,

String

mbeanClassName,
boolean read,
boolean write,
int min,
int max,

String

descr)

Constructor.

RoleInfo

​(

RoleInfo

roleInfo)

Copy constructor.

---

#### Constructor Summary

Constructor.

Copy constructor.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

checkMaxDegree

​(int value)

Returns true if the

value

parameter is lower than or equal to
the expected maximum degree, false otherwise.

boolean

checkMinDegree

​(int value)

Returns true if the

value

parameter is greater than or equal to
the expected minimum degree, false otherwise.

String

getDescription

()

Returns description text for the role.

int

getMaxDegree

()

Returns maximum degree for corresponding role reference.

int

getMinDegree

()

Returns minimum degree for corresponding role reference.

String

getName

()

Returns the name of the role.

String

getRefMBeanClassName

()

Returns name of type of MBean expected to be referenced in
corresponding role.

boolean

isReadable

()

Returns read access mode for the role (true if it is readable).

boolean

isWritable

()

Returns write access mode for the role (true if it is writable).

String

toString

()

Returns a string describing the role info.

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

Returns true if the

value

parameter is lower than or equal to
the expected maximum degree, false otherwise.

Returns true if the

value

parameter is greater than or equal to
the expected minimum degree, false otherwise.

Returns description text for the role.

Returns maximum degree for corresponding role reference.

Returns minimum degree for corresponding role reference.

Returns the name of the role.

Returns name of type of MBean expected to be referenced in
corresponding role.

Returns read access mode for the role (true if it is readable).

Returns write access mode for the role (true if it is writable).

Returns a string describing the role info.

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

- ROLE_CARDINALITY_INFINITY

```java
public static final int ROLE_CARDINALITY_INFINITY
```

To specify an unlimited cardinality.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RoleInfo

```java
public RoleInfo​(
String
roleName,

String
mbeanClassName,
boolean read,
boolean write,
int min,
int max,

String
descr)
throws
IllegalArgumentException
,

InvalidRoleInfoException
,

ClassNotFoundException
,

NotCompliantMBeanException
```

Constructor.

**Parameters:** roleName

- name of the role.
**Parameters:** mbeanClassName

- name of the class of MBean(s) expected to
be referenced in corresponding role. If an MBean

M

is in
this role, then the MBean server must return true for

isInstanceOf(M, mbeanClassName)

.
**Parameters:** read

- flag to indicate if the corresponding role
can be read
**Parameters:** write

- flag to indicate if the corresponding role
can be set
**Parameters:** min

- minimum degree for role, i.e. minimum number of
MBeans to provide in corresponding role
Must be less than or equal to

max

.
(ROLE_CARDINALITY_INFINITY for unlimited)
**Parameters:** max

- maximum degree for role, i.e. maximum number of
MBeans to provide in corresponding role
Must be greater than or equal to

min

(ROLE_CARDINALITY_INFINITY for unlimited)
**Parameters:** descr

- description of the role (can be null)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** InvalidRoleInfoException

- if the minimum degree is
greater than the maximum degree.
**Throws:** ClassNotFoundException

- As of JMX 1.2, this exception
can no longer be thrown. It is retained in the declaration of
this class for compatibility with existing code.
**Throws:** NotCompliantMBeanException

- if the class mbeanClassName
is not a MBean class.

- RoleInfo

```java
public RoleInfo​(
String
roleName,

String
mbeanClassName,
boolean read,
boolean write)
throws
IllegalArgumentException
,

ClassNotFoundException
,

NotCompliantMBeanException
```

Constructor.

**Parameters:** roleName

- name of the role
**Parameters:** mbeanClassName

- name of the class of MBean(s) expected to
be referenced in corresponding role. If an MBean

M

is in
this role, then the MBean server must return true for

isInstanceOf(M, mbeanClassName)

.
**Parameters:** read

- flag to indicate if the corresponding role
can be read
**Parameters:** write

- flag to indicate if the corresponding role
can be set

Minimum and maximum degrees defaulted to 1.

Description of role defaulted to null.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** ClassNotFoundException

- As of JMX 1.2, this exception
can no longer be thrown. It is retained in the declaration of
this class for compatibility with existing code.
**Throws:** NotCompliantMBeanException

- As of JMX 1.2, this
exception can no longer be thrown. It is retained in the
declaration of this class for compatibility with existing code.

- RoleInfo

```java
public RoleInfo​(
String
roleName,

String
mbeanClassName)
throws
IllegalArgumentException
,

ClassNotFoundException
,

NotCompliantMBeanException
```

Constructor.

**Parameters:** roleName

- name of the role
**Parameters:** mbeanClassName

- name of the class of MBean(s) expected to
be referenced in corresponding role. If an MBean

M

is in
this role, then the MBean server must return true for

isInstanceOf(M, mbeanClassName)

.

IsReadable and IsWritable defaulted to true.

Minimum and maximum degrees defaulted to 1.

Description of role defaulted to null.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** ClassNotFoundException

- As of JMX 1.2, this exception
can no longer be thrown. It is retained in the declaration of
this class for compatibility with existing code.
**Throws:** NotCompliantMBeanException

- As of JMX 1.2, this
exception can no longer be thrown. It is retained in the
declaration of this class for compatibility with existing code.

- RoleInfo

```java
public RoleInfo​(
RoleInfo
roleInfo)
throws
IllegalArgumentException
```

Copy constructor.

**Parameters:** roleInfo

- the

RoleInfo

instance to be copied.
**Throws:** IllegalArgumentException

- if null parameter

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns the name of the role.

**Returns:** the name of the role.

- isReadable

```java
public boolean isReadable()
```

Returns read access mode for the role (true if it is readable).

**Returns:** true if the role is readable.

- isWritable

```java
public boolean isWritable()
```

Returns write access mode for the role (true if it is writable).

**Returns:** true if the role is writable.

- getDescription

```java
public
String
getDescription()
```

Returns description text for the role.

**Returns:** the description of the role.

- getMinDegree

```java
public int getMinDegree()
```

Returns minimum degree for corresponding role reference.

**Returns:** the minimum degree.

- getMaxDegree

```java
public int getMaxDegree()
```

Returns maximum degree for corresponding role reference.

**Returns:** the maximum degree.

- getRefMBeanClassName

```java
public
String
getRefMBeanClassName()
```

Returns name of type of MBean expected to be referenced in
corresponding role.

**Returns:** the name of the referenced type.

- checkMinDegree

```java
public boolean checkMinDegree​(int value)
```

Returns true if the

value

parameter is greater than or equal to
the expected minimum degree, false otherwise.

**Parameters:** value

- the value to be checked
**Returns:** true if greater than or equal to minimum degree, false otherwise.

- checkMaxDegree

```java
public boolean checkMaxDegree​(int value)
```

Returns true if the

value

parameter is lower than or equal to
the expected maximum degree, false otherwise.

**Parameters:** value

- the value to be checked
**Returns:** true if lower than or equal to maximum degree, false otherwise.

- toString

```java
public
String
toString()
```

Returns a string describing the role info.

**Overrides:** toString

in class

Object
**Returns:** a description of the role info.

Field Detail

- ROLE_CARDINALITY_INFINITY

```java
public static final int ROLE_CARDINALITY_INFINITY
```

To specify an unlimited cardinality.

**See Also:** Constant Field Values

---

#### Field Detail

ROLE_CARDINALITY_INFINITY

```java
public static final int ROLE_CARDINALITY_INFINITY
```

To specify an unlimited cardinality.

**See Also:** Constant Field Values

---

#### ROLE_CARDINALITY_INFINITY

public static final int ROLE_CARDINALITY_INFINITY

To specify an unlimited cardinality.

Constructor Detail

- RoleInfo

```java
public RoleInfo​(
String
roleName,

String
mbeanClassName,
boolean read,
boolean write,
int min,
int max,

String
descr)
throws
IllegalArgumentException
,

InvalidRoleInfoException
,

ClassNotFoundException
,

NotCompliantMBeanException
```

Constructor.

**Parameters:** roleName

- name of the role.
**Parameters:** mbeanClassName

- name of the class of MBean(s) expected to
be referenced in corresponding role. If an MBean

M

is in
this role, then the MBean server must return true for

isInstanceOf(M, mbeanClassName)

.
**Parameters:** read

- flag to indicate if the corresponding role
can be read
**Parameters:** write

- flag to indicate if the corresponding role
can be set
**Parameters:** min

- minimum degree for role, i.e. minimum number of
MBeans to provide in corresponding role
Must be less than or equal to

max

.
(ROLE_CARDINALITY_INFINITY for unlimited)
**Parameters:** max

- maximum degree for role, i.e. maximum number of
MBeans to provide in corresponding role
Must be greater than or equal to

min

(ROLE_CARDINALITY_INFINITY for unlimited)
**Parameters:** descr

- description of the role (can be null)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** InvalidRoleInfoException

- if the minimum degree is
greater than the maximum degree.
**Throws:** ClassNotFoundException

- As of JMX 1.2, this exception
can no longer be thrown. It is retained in the declaration of
this class for compatibility with existing code.
**Throws:** NotCompliantMBeanException

- if the class mbeanClassName
is not a MBean class.

- RoleInfo

```java
public RoleInfo​(
String
roleName,

String
mbeanClassName,
boolean read,
boolean write)
throws
IllegalArgumentException
,

ClassNotFoundException
,

NotCompliantMBeanException
```

Constructor.

**Parameters:** roleName

- name of the role
**Parameters:** mbeanClassName

- name of the class of MBean(s) expected to
be referenced in corresponding role. If an MBean

M

is in
this role, then the MBean server must return true for

isInstanceOf(M, mbeanClassName)

.
**Parameters:** read

- flag to indicate if the corresponding role
can be read
**Parameters:** write

- flag to indicate if the corresponding role
can be set

Minimum and maximum degrees defaulted to 1.

Description of role defaulted to null.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** ClassNotFoundException

- As of JMX 1.2, this exception
can no longer be thrown. It is retained in the declaration of
this class for compatibility with existing code.
**Throws:** NotCompliantMBeanException

- As of JMX 1.2, this
exception can no longer be thrown. It is retained in the
declaration of this class for compatibility with existing code.

- RoleInfo

```java
public RoleInfo​(
String
roleName,

String
mbeanClassName)
throws
IllegalArgumentException
,

ClassNotFoundException
,

NotCompliantMBeanException
```

Constructor.

**Parameters:** roleName

- name of the role
**Parameters:** mbeanClassName

- name of the class of MBean(s) expected to
be referenced in corresponding role. If an MBean

M

is in
this role, then the MBean server must return true for

isInstanceOf(M, mbeanClassName)

.

IsReadable and IsWritable defaulted to true.

Minimum and maximum degrees defaulted to 1.

Description of role defaulted to null.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** ClassNotFoundException

- As of JMX 1.2, this exception
can no longer be thrown. It is retained in the declaration of
this class for compatibility with existing code.
**Throws:** NotCompliantMBeanException

- As of JMX 1.2, this
exception can no longer be thrown. It is retained in the
declaration of this class for compatibility with existing code.

- RoleInfo

```java
public RoleInfo​(
RoleInfo
roleInfo)
throws
IllegalArgumentException
```

Copy constructor.

**Parameters:** roleInfo

- the

RoleInfo

instance to be copied.
**Throws:** IllegalArgumentException

- if null parameter

---

#### Constructor Detail

RoleInfo

```java
public RoleInfo​(
String
roleName,

String
mbeanClassName,
boolean read,
boolean write,
int min,
int max,

String
descr)
throws
IllegalArgumentException
,

InvalidRoleInfoException
,

ClassNotFoundException
,

NotCompliantMBeanException
```

Constructor.

**Parameters:** roleName

- name of the role.
**Parameters:** mbeanClassName

- name of the class of MBean(s) expected to
be referenced in corresponding role. If an MBean

M

is in
this role, then the MBean server must return true for

isInstanceOf(M, mbeanClassName)

.
**Parameters:** read

- flag to indicate if the corresponding role
can be read
**Parameters:** write

- flag to indicate if the corresponding role
can be set
**Parameters:** min

- minimum degree for role, i.e. minimum number of
MBeans to provide in corresponding role
Must be less than or equal to

max

.
(ROLE_CARDINALITY_INFINITY for unlimited)
**Parameters:** max

- maximum degree for role, i.e. maximum number of
MBeans to provide in corresponding role
Must be greater than or equal to

min

(ROLE_CARDINALITY_INFINITY for unlimited)
**Parameters:** descr

- description of the role (can be null)
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** InvalidRoleInfoException

- if the minimum degree is
greater than the maximum degree.
**Throws:** ClassNotFoundException

- As of JMX 1.2, this exception
can no longer be thrown. It is retained in the declaration of
this class for compatibility with existing code.
**Throws:** NotCompliantMBeanException

- if the class mbeanClassName
is not a MBean class.

---

#### RoleInfo

public RoleInfo​(

String

roleName,

String

mbeanClassName,
boolean read,
boolean write,
int min,
int max,

String

descr)
throws

IllegalArgumentException

,

InvalidRoleInfoException

,

ClassNotFoundException

,

NotCompliantMBeanException

Constructor.

RoleInfo

```java
public RoleInfo​(
String
roleName,

String
mbeanClassName,
boolean read,
boolean write)
throws
IllegalArgumentException
,

ClassNotFoundException
,

NotCompliantMBeanException
```

Constructor.

**Parameters:** roleName

- name of the role
**Parameters:** mbeanClassName

- name of the class of MBean(s) expected to
be referenced in corresponding role. If an MBean

M

is in
this role, then the MBean server must return true for

isInstanceOf(M, mbeanClassName)

.
**Parameters:** read

- flag to indicate if the corresponding role
can be read
**Parameters:** write

- flag to indicate if the corresponding role
can be set

Minimum and maximum degrees defaulted to 1.

Description of role defaulted to null.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** ClassNotFoundException

- As of JMX 1.2, this exception
can no longer be thrown. It is retained in the declaration of
this class for compatibility with existing code.
**Throws:** NotCompliantMBeanException

- As of JMX 1.2, this
exception can no longer be thrown. It is retained in the
declaration of this class for compatibility with existing code.

---

#### RoleInfo

public RoleInfo​(

String

roleName,

String

mbeanClassName,
boolean read,
boolean write)
throws

IllegalArgumentException

,

ClassNotFoundException

,

NotCompliantMBeanException

Constructor.

Minimum and maximum degrees defaulted to 1.

Description of role defaulted to null.

Description of role defaulted to null.

RoleInfo

```java
public RoleInfo​(
String
roleName,

String
mbeanClassName)
throws
IllegalArgumentException
,

ClassNotFoundException
,

NotCompliantMBeanException
```

Constructor.

**Parameters:** roleName

- name of the role
**Parameters:** mbeanClassName

- name of the class of MBean(s) expected to
be referenced in corresponding role. If an MBean

M

is in
this role, then the MBean server must return true for

isInstanceOf(M, mbeanClassName)

.

IsReadable and IsWritable defaulted to true.

Minimum and maximum degrees defaulted to 1.

Description of role defaulted to null.
**Throws:** IllegalArgumentException

- if null parameter
**Throws:** ClassNotFoundException

- As of JMX 1.2, this exception
can no longer be thrown. It is retained in the declaration of
this class for compatibility with existing code.
**Throws:** NotCompliantMBeanException

- As of JMX 1.2, this
exception can no longer be thrown. It is retained in the
declaration of this class for compatibility with existing code.

---

#### RoleInfo

public RoleInfo​(

String

roleName,

String

mbeanClassName)
throws

IllegalArgumentException

,

ClassNotFoundException

,

NotCompliantMBeanException

Constructor.

IsReadable and IsWritable defaulted to true.

Minimum and maximum degrees defaulted to 1.

Description of role defaulted to null.

Minimum and maximum degrees defaulted to 1.

Description of role defaulted to null.

Description of role defaulted to null.

RoleInfo

```java
public RoleInfo​(
RoleInfo
roleInfo)
throws
IllegalArgumentException
```

Copy constructor.

**Parameters:** roleInfo

- the

RoleInfo

instance to be copied.
**Throws:** IllegalArgumentException

- if null parameter

---

#### RoleInfo

public RoleInfo​(

RoleInfo

roleInfo)
throws

IllegalArgumentException

Copy constructor.

Method Detail

- getName

```java
public
String
getName()
```

Returns the name of the role.

**Returns:** the name of the role.

- isReadable

```java
public boolean isReadable()
```

Returns read access mode for the role (true if it is readable).

**Returns:** true if the role is readable.

- isWritable

```java
public boolean isWritable()
```

Returns write access mode for the role (true if it is writable).

**Returns:** true if the role is writable.

- getDescription

```java
public
String
getDescription()
```

Returns description text for the role.

**Returns:** the description of the role.

- getMinDegree

```java
public int getMinDegree()
```

Returns minimum degree for corresponding role reference.

**Returns:** the minimum degree.

- getMaxDegree

```java
public int getMaxDegree()
```

Returns maximum degree for corresponding role reference.

**Returns:** the maximum degree.

- getRefMBeanClassName

```java
public
String
getRefMBeanClassName()
```

Returns name of type of MBean expected to be referenced in
corresponding role.

**Returns:** the name of the referenced type.

- checkMinDegree

```java
public boolean checkMinDegree​(int value)
```

Returns true if the

value

parameter is greater than or equal to
the expected minimum degree, false otherwise.

**Parameters:** value

- the value to be checked
**Returns:** true if greater than or equal to minimum degree, false otherwise.

- checkMaxDegree

```java
public boolean checkMaxDegree​(int value)
```

Returns true if the

value

parameter is lower than or equal to
the expected maximum degree, false otherwise.

**Parameters:** value

- the value to be checked
**Returns:** true if lower than or equal to maximum degree, false otherwise.

- toString

```java
public
String
toString()
```

Returns a string describing the role info.

**Overrides:** toString

in class

Object
**Returns:** a description of the role info.

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns the name of the role.

**Returns:** the name of the role.

---

#### getName

public

String

getName()

Returns the name of the role.

isReadable

```java
public boolean isReadable()
```

Returns read access mode for the role (true if it is readable).

**Returns:** true if the role is readable.

---

#### isReadable

public boolean isReadable()

Returns read access mode for the role (true if it is readable).

isWritable

```java
public boolean isWritable()
```

Returns write access mode for the role (true if it is writable).

**Returns:** true if the role is writable.

---

#### isWritable

public boolean isWritable()

Returns write access mode for the role (true if it is writable).

getDescription

```java
public
String
getDescription()
```

Returns description text for the role.

**Returns:** the description of the role.

---

#### getDescription

public

String

getDescription()

Returns description text for the role.

getMinDegree

```java
public int getMinDegree()
```

Returns minimum degree for corresponding role reference.

**Returns:** the minimum degree.

---

#### getMinDegree

public int getMinDegree()

Returns minimum degree for corresponding role reference.

getMaxDegree

```java
public int getMaxDegree()
```

Returns maximum degree for corresponding role reference.

**Returns:** the maximum degree.

---

#### getMaxDegree

public int getMaxDegree()

Returns maximum degree for corresponding role reference.

getRefMBeanClassName

```java
public
String
getRefMBeanClassName()
```

Returns name of type of MBean expected to be referenced in
corresponding role.

**Returns:** the name of the referenced type.

---

#### getRefMBeanClassName

public

String

getRefMBeanClassName()

Returns name of type of MBean expected to be referenced in
corresponding role.

checkMinDegree

```java
public boolean checkMinDegree​(int value)
```

Returns true if the

value

parameter is greater than or equal to
the expected minimum degree, false otherwise.

**Parameters:** value

- the value to be checked
**Returns:** true if greater than or equal to minimum degree, false otherwise.

---

#### checkMinDegree

public boolean checkMinDegree​(int value)

Returns true if the

value

parameter is greater than or equal to
the expected minimum degree, false otherwise.

checkMaxDegree

```java
public boolean checkMaxDegree​(int value)
```

Returns true if the

value

parameter is lower than or equal to
the expected maximum degree, false otherwise.

**Parameters:** value

- the value to be checked
**Returns:** true if lower than or equal to maximum degree, false otherwise.

---

#### checkMaxDegree

public boolean checkMaxDegree​(int value)

Returns true if the

value

parameter is lower than or equal to
the expected maximum degree, false otherwise.

toString

```java
public
String
toString()
```

Returns a string describing the role info.

**Overrides:** toString

in class

Object
**Returns:** a description of the role info.

---

#### toString

public

String

toString()

Returns a string describing the role info.

---

