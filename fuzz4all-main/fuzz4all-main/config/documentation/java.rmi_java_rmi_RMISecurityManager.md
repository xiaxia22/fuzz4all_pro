# Class RMISecurityManager

**Source:** `java.rmi\java\rmi\RMISecurityManager.html`

### Class Description

```java
@Deprecated

public class
RMISecurityManager

extends
SecurityManager
```

RMISecurityManager

implements a policy identical to the policy
implemented by

SecurityManager

. RMI applications
should use the

SecurityManager

class or another appropriate

SecurityManager

implementation instead of this class. RMI's class
loader will download classes from remote locations only if a security
manager has been set.

**Implementation Note:** Applets typically run in a container that already has a security
manager, so there is generally no need for applets to set a security
manager. If you have a standalone application, you might need to set a

SecurityManager

in order to enable class downloading. This can be
done by adding the following to your code. (It needs to be executed before
RMI can download code from remote hosts, so it most likely needs to appear
in the

main

method of your application.)

```java
if (System.getSecurityManager() == null) {
System.setSecurityManager(new SecurityManager());
}
```
**Since:** 1.1

---

### Field Details

*No entries found.*

### Constructor Details

#### public RMISecurityManager()

Constructs a new

RMISecurityManager

.

**Since:**
- 1.1

---

### Method Details

*No entries found.*

### Additional Sections

#### Class RMISecurityManager

java.lang.Object

- java.lang.SecurityManager
- - java.rmi.RMISecurityManager

java.lang.SecurityManager

- java.rmi.RMISecurityManager

java.rmi.RMISecurityManager

```java
@Deprecated

public class
RMISecurityManager

extends
SecurityManager
```

Deprecated.

Use

SecurityManager

instead.

RMISecurityManager

implements a policy identical to the policy
implemented by

SecurityManager

. RMI applications
should use the

SecurityManager

class or another appropriate

SecurityManager

implementation instead of this class. RMI's class
loader will download classes from remote locations only if a security
manager has been set.

**Implementation Note:** Applets typically run in a container that already has a security
manager, so there is generally no need for applets to set a security
manager. If you have a standalone application, you might need to set a

SecurityManager

in order to enable class downloading. This can be
done by adding the following to your code. (It needs to be executed before
RMI can download code from remote hosts, so it most likely needs to appear
in the

main

method of your application.)

```java
if (System.getSecurityManager() == null) {
System.setSecurityManager(new SecurityManager());
}
```
**Since:** 1.1

@Deprecated

public class

RMISecurityManager

extends

SecurityManager

RMISecurityManager

implements a policy identical to the policy
implemented by

SecurityManager

. RMI applications
should use the

SecurityManager

class or another appropriate

SecurityManager

implementation instead of this class. RMI's class
loader will download classes from remote locations only if a security
manager has been set.

Applets typically run in a container that already has a security
manager, so there is generally no need for applets to set a security
manager. If you have a standalone application, you might need to set a

SecurityManager

in order to enable class downloading. This can be
done by adding the following to your code. (It needs to be executed before
RMI can download code from remote hosts, so it most likely needs to appear
in the

main

method of your application.)

```java
if (System.getSecurityManager() == null) {
System.setSecurityManager(new SecurityManager());
}
```

if (System.getSecurityManager() == null) {
System.setSecurityManager(new SecurityManager());
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RMISecurityManager

()

Deprecated.

Constructs a new

RMISecurityManager

.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

SecurityManager

checkAccept

,

checkAccess

,

checkAccess

,

checkConnect

,

checkConnect

,

checkCreateClassLoader

,

checkDelete

,

checkExec

,

checkExit

,

checkLink

,

checkListen

,

checkMulticast

,

checkMulticast

,

checkPackageAccess

,

checkPackageDefinition

,

checkPermission

,

checkPermission

,

checkPrintJobAccess

,

checkPropertiesAccess

,

checkPropertyAccess

,

checkRead

,

checkRead

,

checkRead

,

checkSecurityAccess

,

checkSetFactory

,

checkWrite

,

checkWrite

,

getClassContext

,

getSecurityContext

,

getThreadGroup

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

Constructor

Description

RMISecurityManager

()

Deprecated.

Constructs a new

RMISecurityManager

.

---

#### Constructor Summary

Deprecated.

Constructs a new

RMISecurityManager

.

Method Summary

- Methods declared in class java.lang.

SecurityManager

checkAccept

,

checkAccess

,

checkAccess

,

checkConnect

,

checkConnect

,

checkCreateClassLoader

,

checkDelete

,

checkExec

,

checkExit

,

checkLink

,

checkListen

,

checkMulticast

,

checkMulticast

,

checkPackageAccess

,

checkPackageDefinition

,

checkPermission

,

checkPermission

,

checkPrintJobAccess

,

checkPropertiesAccess

,

checkPropertyAccess

,

checkRead

,

checkRead

,

checkRead

,

checkSecurityAccess

,

checkSetFactory

,

checkWrite

,

checkWrite

,

getClassContext

,

getSecurityContext

,

getThreadGroup

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

Methods declared in class java.lang.

SecurityManager

checkAccept

,

checkAccess

,

checkAccess

,

checkConnect

,

checkConnect

,

checkCreateClassLoader

,

checkDelete

,

checkExec

,

checkExit

,

checkLink

,

checkListen

,

checkMulticast

,

checkMulticast

,

checkPackageAccess

,

checkPackageDefinition

,

checkPermission

,

checkPermission

,

checkPrintJobAccess

,

checkPropertiesAccess

,

checkPropertyAccess

,

checkRead

,

checkRead

,

checkRead

,

checkSecurityAccess

,

checkSetFactory

,

checkWrite

,

checkWrite

,

getClassContext

,

getSecurityContext

,

getThreadGroup

---

#### Methods declared in class java.lang. SecurityManager

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

- RMISecurityManager

```java
public RMISecurityManager()
```

Deprecated.

Constructs a new

RMISecurityManager

.

**Since:** 1.1

Constructor Detail

- RMISecurityManager

```java
public RMISecurityManager()
```

Deprecated.

Constructs a new

RMISecurityManager

.

**Since:** 1.1

---

#### Constructor Detail

RMISecurityManager

```java
public RMISecurityManager()
```

Deprecated.

Constructs a new

RMISecurityManager

.

**Since:** 1.1

---

#### RMISecurityManager

public RMISecurityManager()

Constructs a new

RMISecurityManager

.

---

