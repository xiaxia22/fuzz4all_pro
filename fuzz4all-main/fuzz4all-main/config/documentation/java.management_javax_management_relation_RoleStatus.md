# Class RoleStatus

**Source:** `java.management\javax\management\relation\RoleStatus.html`

### Class Description

```java
public class
RoleStatus

extends
Object
```

This class describes the various problems which can be encountered when
accessing a role.

**Since:** 1.5

---

### Field Details

#### public static final int NO_ROLE_WITH_NAME

Problem type when trying to access an unknown role.

**See Also:**
- Constant Field Values

---

#### public static final int ROLE_NOT_READABLE

Problem type when trying to read a non-readable attribute.

**See Also:**
- Constant Field Values

---

#### public static final int ROLE_NOT_WRITABLE

Problem type when trying to update a non-writable attribute.

**See Also:**
- Constant Field Values

---

#### public static final int LESS_THAN_MIN_ROLE_DEGREE

Problem type when trying to set a role value with less ObjectNames than
the minimum expected cardinality.

**See Also:**
- Constant Field Values

---

#### public static final int MORE_THAN_MAX_ROLE_DEGREE

Problem type when trying to set a role value with more ObjectNames than
the maximum expected cardinality.

**See Also:**
- Constant Field Values

---

#### public static final int REF_MBEAN_OF_INCORRECT_CLASS

Problem type when trying to set a role value including the ObjectName of
a MBean not of the class expected for that role.

**See Also:**
- Constant Field Values

---

#### public static final int REF_MBEAN_NOT_REGISTERED

Problem type when trying to set a role value including the ObjectName of
a MBean not registered in the MBean Server.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public RoleStatus()

*No description found.*

---

### Method Details

#### public static boolean isRoleStatus​(int status)

Returns true if given value corresponds to a known role status, false
otherwise.

**Parameters:**
- status

- a status code.

**Returns:**
- true if this value is a known role status.

---

### Additional Sections

#### Class RoleStatus

java.lang.Object

- javax.management.relation.RoleStatus

javax.management.relation.RoleStatus

```java
public class
RoleStatus

extends
Object
```

This class describes the various problems which can be encountered when
accessing a role.

**Since:** 1.5

public class

RoleStatus

extends

Object

This class describes the various problems which can be encountered when
accessing a role.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

LESS_THAN_MIN_ROLE_DEGREE

Problem type when trying to set a role value with less ObjectNames than
the minimum expected cardinality.

static int

MORE_THAN_MAX_ROLE_DEGREE

Problem type when trying to set a role value with more ObjectNames than
the maximum expected cardinality.

static int

NO_ROLE_WITH_NAME

Problem type when trying to access an unknown role.

static int

REF_MBEAN_NOT_REGISTERED

Problem type when trying to set a role value including the ObjectName of
a MBean not registered in the MBean Server.

static int

REF_MBEAN_OF_INCORRECT_CLASS

Problem type when trying to set a role value including the ObjectName of
a MBean not of the class expected for that role.

static int

ROLE_NOT_READABLE

Problem type when trying to read a non-readable attribute.

static int

ROLE_NOT_WRITABLE

Problem type when trying to update a non-writable attribute.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RoleStatus

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static boolean

isRoleStatus

​(int status)

Returns true if given value corresponds to a known role status, false
otherwise.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

LESS_THAN_MIN_ROLE_DEGREE

Problem type when trying to set a role value with less ObjectNames than
the minimum expected cardinality.

static int

MORE_THAN_MAX_ROLE_DEGREE

Problem type when trying to set a role value with more ObjectNames than
the maximum expected cardinality.

static int

NO_ROLE_WITH_NAME

Problem type when trying to access an unknown role.

static int

REF_MBEAN_NOT_REGISTERED

Problem type when trying to set a role value including the ObjectName of
a MBean not registered in the MBean Server.

static int

REF_MBEAN_OF_INCORRECT_CLASS

Problem type when trying to set a role value including the ObjectName of
a MBean not of the class expected for that role.

static int

ROLE_NOT_READABLE

Problem type when trying to read a non-readable attribute.

static int

ROLE_NOT_WRITABLE

Problem type when trying to update a non-writable attribute.

---

#### Field Summary

Problem type when trying to set a role value with less ObjectNames than
the minimum expected cardinality.

Problem type when trying to set a role value with more ObjectNames than
the maximum expected cardinality.

Problem type when trying to access an unknown role.

Problem type when trying to set a role value including the ObjectName of
a MBean not registered in the MBean Server.

Problem type when trying to set a role value including the ObjectName of
a MBean not of the class expected for that role.

Problem type when trying to read a non-readable attribute.

Problem type when trying to update a non-writable attribute.

Constructor Summary

Constructors

Constructor

Description

RoleStatus

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static boolean

isRoleStatus

​(int status)

Returns true if given value corresponds to a known role status, false
otherwise.

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

Returns true if given value corresponds to a known role status, false
otherwise.

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

============ FIELD DETAIL ===========

- Field Detail

- NO_ROLE_WITH_NAME

```java
public static final int NO_ROLE_WITH_NAME
```

Problem type when trying to access an unknown role.

**See Also:** Constant Field Values

- ROLE_NOT_READABLE

```java
public static final int ROLE_NOT_READABLE
```

Problem type when trying to read a non-readable attribute.

**See Also:** Constant Field Values

- ROLE_NOT_WRITABLE

```java
public static final int ROLE_NOT_WRITABLE
```

Problem type when trying to update a non-writable attribute.

**See Also:** Constant Field Values

- LESS_THAN_MIN_ROLE_DEGREE

```java
public static final int LESS_THAN_MIN_ROLE_DEGREE
```

Problem type when trying to set a role value with less ObjectNames than
the minimum expected cardinality.

**See Also:** Constant Field Values

- MORE_THAN_MAX_ROLE_DEGREE

```java
public static final int MORE_THAN_MAX_ROLE_DEGREE
```

Problem type when trying to set a role value with more ObjectNames than
the maximum expected cardinality.

**See Also:** Constant Field Values

- REF_MBEAN_OF_INCORRECT_CLASS

```java
public static final int REF_MBEAN_OF_INCORRECT_CLASS
```

Problem type when trying to set a role value including the ObjectName of
a MBean not of the class expected for that role.

**See Also:** Constant Field Values

- REF_MBEAN_NOT_REGISTERED

```java
public static final int REF_MBEAN_NOT_REGISTERED
```

Problem type when trying to set a role value including the ObjectName of
a MBean not registered in the MBean Server.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RoleStatus

```java
public RoleStatus()
```

============ METHOD DETAIL ==========

- Method Detail

- isRoleStatus

```java
public static boolean isRoleStatus​(int status)
```

Returns true if given value corresponds to a known role status, false
otherwise.

**Parameters:** status

- a status code.
**Returns:** true if this value is a known role status.

Field Detail

- NO_ROLE_WITH_NAME

```java
public static final int NO_ROLE_WITH_NAME
```

Problem type when trying to access an unknown role.

**See Also:** Constant Field Values

- ROLE_NOT_READABLE

```java
public static final int ROLE_NOT_READABLE
```

Problem type when trying to read a non-readable attribute.

**See Also:** Constant Field Values

- ROLE_NOT_WRITABLE

```java
public static final int ROLE_NOT_WRITABLE
```

Problem type when trying to update a non-writable attribute.

**See Also:** Constant Field Values

- LESS_THAN_MIN_ROLE_DEGREE

```java
public static final int LESS_THAN_MIN_ROLE_DEGREE
```

Problem type when trying to set a role value with less ObjectNames than
the minimum expected cardinality.

**See Also:** Constant Field Values

- MORE_THAN_MAX_ROLE_DEGREE

```java
public static final int MORE_THAN_MAX_ROLE_DEGREE
```

Problem type when trying to set a role value with more ObjectNames than
the maximum expected cardinality.

**See Also:** Constant Field Values

- REF_MBEAN_OF_INCORRECT_CLASS

```java
public static final int REF_MBEAN_OF_INCORRECT_CLASS
```

Problem type when trying to set a role value including the ObjectName of
a MBean not of the class expected for that role.

**See Also:** Constant Field Values

- REF_MBEAN_NOT_REGISTERED

```java
public static final int REF_MBEAN_NOT_REGISTERED
```

Problem type when trying to set a role value including the ObjectName of
a MBean not registered in the MBean Server.

**See Also:** Constant Field Values

---

#### Field Detail

NO_ROLE_WITH_NAME

```java
public static final int NO_ROLE_WITH_NAME
```

Problem type when trying to access an unknown role.

**See Also:** Constant Field Values

---

#### NO_ROLE_WITH_NAME

public static final int NO_ROLE_WITH_NAME

Problem type when trying to access an unknown role.

ROLE_NOT_READABLE

```java
public static final int ROLE_NOT_READABLE
```

Problem type when trying to read a non-readable attribute.

**See Also:** Constant Field Values

---

#### ROLE_NOT_READABLE

public static final int ROLE_NOT_READABLE

Problem type when trying to read a non-readable attribute.

ROLE_NOT_WRITABLE

```java
public static final int ROLE_NOT_WRITABLE
```

Problem type when trying to update a non-writable attribute.

**See Also:** Constant Field Values

---

#### ROLE_NOT_WRITABLE

public static final int ROLE_NOT_WRITABLE

Problem type when trying to update a non-writable attribute.

LESS_THAN_MIN_ROLE_DEGREE

```java
public static final int LESS_THAN_MIN_ROLE_DEGREE
```

Problem type when trying to set a role value with less ObjectNames than
the minimum expected cardinality.

**See Also:** Constant Field Values

---

#### LESS_THAN_MIN_ROLE_DEGREE

public static final int LESS_THAN_MIN_ROLE_DEGREE

Problem type when trying to set a role value with less ObjectNames than
the minimum expected cardinality.

MORE_THAN_MAX_ROLE_DEGREE

```java
public static final int MORE_THAN_MAX_ROLE_DEGREE
```

Problem type when trying to set a role value with more ObjectNames than
the maximum expected cardinality.

**See Also:** Constant Field Values

---

#### MORE_THAN_MAX_ROLE_DEGREE

public static final int MORE_THAN_MAX_ROLE_DEGREE

Problem type when trying to set a role value with more ObjectNames than
the maximum expected cardinality.

REF_MBEAN_OF_INCORRECT_CLASS

```java
public static final int REF_MBEAN_OF_INCORRECT_CLASS
```

Problem type when trying to set a role value including the ObjectName of
a MBean not of the class expected for that role.

**See Also:** Constant Field Values

---

#### REF_MBEAN_OF_INCORRECT_CLASS

public static final int REF_MBEAN_OF_INCORRECT_CLASS

Problem type when trying to set a role value including the ObjectName of
a MBean not of the class expected for that role.

REF_MBEAN_NOT_REGISTERED

```java
public static final int REF_MBEAN_NOT_REGISTERED
```

Problem type when trying to set a role value including the ObjectName of
a MBean not registered in the MBean Server.

**See Also:** Constant Field Values

---

#### REF_MBEAN_NOT_REGISTERED

public static final int REF_MBEAN_NOT_REGISTERED

Problem type when trying to set a role value including the ObjectName of
a MBean not registered in the MBean Server.

Constructor Detail

- RoleStatus

```java
public RoleStatus()
```

---

#### Constructor Detail

RoleStatus

```java
public RoleStatus()
```

---

#### RoleStatus

public RoleStatus()

Method Detail

- isRoleStatus

```java
public static boolean isRoleStatus​(int status)
```

Returns true if given value corresponds to a known role status, false
otherwise.

**Parameters:** status

- a status code.
**Returns:** true if this value is a known role status.

---

#### Method Detail

isRoleStatus

```java
public static boolean isRoleStatus​(int status)
```

Returns true if given value corresponds to a known role status, false
otherwise.

**Parameters:** status

- a status code.
**Returns:** true if this value is a known role status.

---

#### isRoleStatus

public static boolean isRoleStatus​(int status)

Returns true if given value corresponds to a known role status, false
otherwise.

---

