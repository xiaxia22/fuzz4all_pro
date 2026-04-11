# Interface DriverAction

**Source:** `java.sql\java\sql\DriverAction.html`

### Class Description

```java
public interface
DriverAction
```

An interface that must be implemented when a

Driver

wants to be
notified by

DriverManager

.

A

DriverAction

implementation is not intended to be used
directly by applications. A JDBC Driver may choose
to create its

DriverAction

implementation in a private class
to avoid it being called directly.

The JDBC driver's static initialization block must call

DriverManager.registerDriver(java.sql.Driver, java.sql.DriverAction)

in order
to inform

DriverManager

which

DriverAction

implementation to
call when the JDBC driver is de-registered.

**Since:** 1.8

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void deregister()

Method called by

DriverManager.deregisterDriver(Driver)

to notify the JDBC driver that it was de-registered.

The

deregister

method is intended only to be used by JDBC Drivers
and not by applications. JDBC drivers are recommended to not implement

DriverAction

in a public class. If there are active
connections to the database at the time that the

deregister

method is called, it is implementation specific as to whether the
connections are closed or allowed to continue. Once this method is
called, it is implementation specific as to whether the driver may
limit the ability to create new connections to the database, invoke
other

Driver

methods or throw a

SQLException

.
Consult your JDBC driver's documentation for additional information
on its behavior.

**See Also:**
- DriverManager.registerDriver(java.sql.Driver, java.sql.DriverAction)

,

DriverManager.deregisterDriver(Driver)

**Since:**
- 1.8

---

### Additional Sections

#### Interface DriverAction

```java
public interface
DriverAction
```

An interface that must be implemented when a

Driver

wants to be
notified by

DriverManager

.

A

DriverAction

implementation is not intended to be used
directly by applications. A JDBC Driver may choose
to create its

DriverAction

implementation in a private class
to avoid it being called directly.

The JDBC driver's static initialization block must call

DriverManager.registerDriver(java.sql.Driver, java.sql.DriverAction)

in order
to inform

DriverManager

which

DriverAction

implementation to
call when the JDBC driver is de-registered.

**Since:** 1.8

public interface

DriverAction

An interface that must be implemented when a

Driver

wants to be
notified by

DriverManager

.

A

DriverAction

implementation is not intended to be used
directly by applications. A JDBC Driver may choose
to create its

DriverAction

implementation in a private class
to avoid it being called directly.

The JDBC driver's static initialization block must call

DriverManager.registerDriver(java.sql.Driver, java.sql.DriverAction)

in order
to inform

DriverManager

which

DriverAction

implementation to
call when the JDBC driver is de-registered.

A

DriverAction

implementation is not intended to be used
directly by applications. A JDBC Driver may choose
to create its

DriverAction

implementation in a private class
to avoid it being called directly.

The JDBC driver's static initialization block must call

DriverManager.registerDriver(java.sql.Driver, java.sql.DriverAction)

in order
to inform

DriverManager

which

DriverAction

implementation to
call when the JDBC driver is de-registered.

The JDBC driver's static initialization block must call

DriverManager.registerDriver(java.sql.Driver, java.sql.DriverAction)

in order
to inform

DriverManager

which

DriverAction

implementation to
call when the JDBC driver is de-registered.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

deregister

()

Method called by

DriverManager.deregisterDriver(Driver)

to notify the JDBC driver that it was de-registered.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

deregister

()

Method called by

DriverManager.deregisterDriver(Driver)

to notify the JDBC driver that it was de-registered.

---

#### Method Summary

Method called by

DriverManager.deregisterDriver(Driver)

to notify the JDBC driver that it was de-registered.

============ METHOD DETAIL ==========

- Method Detail

- deregister

```java
void deregister()
```

Method called by

DriverManager.deregisterDriver(Driver)

to notify the JDBC driver that it was de-registered.

The

deregister

method is intended only to be used by JDBC Drivers
and not by applications. JDBC drivers are recommended to not implement

DriverAction

in a public class. If there are active
connections to the database at the time that the

deregister

method is called, it is implementation specific as to whether the
connections are closed or allowed to continue. Once this method is
called, it is implementation specific as to whether the driver may
limit the ability to create new connections to the database, invoke
other

Driver

methods or throw a

SQLException

.
Consult your JDBC driver's documentation for additional information
on its behavior.

**Since:** 1.8
**See Also:** DriverManager.registerDriver(java.sql.Driver, java.sql.DriverAction)

,

DriverManager.deregisterDriver(Driver)

Method Detail

- deregister

```java
void deregister()
```

Method called by

DriverManager.deregisterDriver(Driver)

to notify the JDBC driver that it was de-registered.

The

deregister

method is intended only to be used by JDBC Drivers
and not by applications. JDBC drivers are recommended to not implement

DriverAction

in a public class. If there are active
connections to the database at the time that the

deregister

method is called, it is implementation specific as to whether the
connections are closed or allowed to continue. Once this method is
called, it is implementation specific as to whether the driver may
limit the ability to create new connections to the database, invoke
other

Driver

methods or throw a

SQLException

.
Consult your JDBC driver's documentation for additional information
on its behavior.

**Since:** 1.8
**See Also:** DriverManager.registerDriver(java.sql.Driver, java.sql.DriverAction)

,

DriverManager.deregisterDriver(Driver)

---

#### Method Detail

deregister

```java
void deregister()
```

Method called by

DriverManager.deregisterDriver(Driver)

to notify the JDBC driver that it was de-registered.

The

deregister

method is intended only to be used by JDBC Drivers
and not by applications. JDBC drivers are recommended to not implement

DriverAction

in a public class. If there are active
connections to the database at the time that the

deregister

method is called, it is implementation specific as to whether the
connections are closed or allowed to continue. Once this method is
called, it is implementation specific as to whether the driver may
limit the ability to create new connections to the database, invoke
other

Driver

methods or throw a

SQLException

.
Consult your JDBC driver's documentation for additional information
on its behavior.

**Since:** 1.8
**See Also:** DriverManager.registerDriver(java.sql.Driver, java.sql.DriverAction)

,

DriverManager.deregisterDriver(Driver)

---

#### deregister

void deregister()

Method called by

DriverManager.deregisterDriver(Driver)

to notify the JDBC driver that it was de-registered.

The

deregister

method is intended only to be used by JDBC Drivers
and not by applications. JDBC drivers are recommended to not implement

DriverAction

in a public class. If there are active
connections to the database at the time that the

deregister

method is called, it is implementation specific as to whether the
connections are closed or allowed to continue. Once this method is
called, it is implementation specific as to whether the driver may
limit the ability to create new connections to the database, invoke
other

Driver

methods or throw a

SQLException

.
Consult your JDBC driver's documentation for additional information
on its behavior.

The

deregister

method is intended only to be used by JDBC Drivers
and not by applications. JDBC drivers are recommended to not implement

DriverAction

in a public class. If there are active
connections to the database at the time that the

deregister

method is called, it is implementation specific as to whether the
connections are closed or allowed to continue. Once this method is
called, it is implementation specific as to whether the driver may
limit the ability to create new connections to the database, invoke
other

Driver

methods or throw a

SQLException

.
Consult your JDBC driver's documentation for additional information
on its behavior.

---

