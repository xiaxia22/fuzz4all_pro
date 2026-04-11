# Class InheritableThreadLocal<T>

**Source:** `java.base\java\lang\InheritableThreadLocal.html`

### Class Description

```java
public class
InheritableThreadLocal<T>

extends
ThreadLocal
<T>
```

This class extends

ThreadLocal

to provide inheritance of values
from parent thread to child thread: when a child thread is created, the
child receives initial values for all inheritable thread-local variables
for which the parent has values. Normally the child's values will be
identical to the parent's; however, the child's value can be made an
arbitrary function of the parent's by overriding the

childValue

method in this class.

Inheritable thread-local variables are used in preference to
ordinary thread-local variables when the per-thread-attribute being
maintained in the variable (e.g., User ID, Transaction ID) must be
automatically transmitted to any child threads that are created.

Note: During the creation of a new

thread

, it is
possible to

opt out

of receiving initial values for inheritable
thread-local variables.

**Since:** 1.2
**See Also:** ThreadLocal

---

### Field Details

*No entries found.*

### Constructor Details

#### public InheritableThreadLocal()

*No description found.*

---

### Method Details

#### protected
T
childValue​(
T
parentValue)

Computes the child's initial value for this inheritable thread-local
variable as a function of the parent's value at the time the child
thread is created. This method is called from within the parent
thread before the child is started.

This method merely returns its input argument, and should be overridden
if a different behavior is desired.

**Parameters:**
- parentValue

- the parent thread's value

**Returns:**
- the child thread's initial value

---

### Additional Sections

#### Class InheritableThreadLocal<T>

java.lang.Object

- java.lang.ThreadLocal

<T>
- - java.lang.InheritableThreadLocal<T>

java.lang.ThreadLocal

<T>

- java.lang.InheritableThreadLocal<T>

java.lang.InheritableThreadLocal<T>

```java
public class
InheritableThreadLocal<T>

extends
ThreadLocal
<T>
```

This class extends

ThreadLocal

to provide inheritance of values
from parent thread to child thread: when a child thread is created, the
child receives initial values for all inheritable thread-local variables
for which the parent has values. Normally the child's values will be
identical to the parent's; however, the child's value can be made an
arbitrary function of the parent's by overriding the

childValue

method in this class.

Inheritable thread-local variables are used in preference to
ordinary thread-local variables when the per-thread-attribute being
maintained in the variable (e.g., User ID, Transaction ID) must be
automatically transmitted to any child threads that are created.

Note: During the creation of a new

thread

, it is
possible to

opt out

of receiving initial values for inheritable
thread-local variables.

**Since:** 1.2
**See Also:** ThreadLocal

public class

InheritableThreadLocal<T>

extends

ThreadLocal

<T>

This class extends

ThreadLocal

to provide inheritance of values
from parent thread to child thread: when a child thread is created, the
child receives initial values for all inheritable thread-local variables
for which the parent has values. Normally the child's values will be
identical to the parent's; however, the child's value can be made an
arbitrary function of the parent's by overriding the

childValue

method in this class.

Inheritable thread-local variables are used in preference to
ordinary thread-local variables when the per-thread-attribute being
maintained in the variable (e.g., User ID, Transaction ID) must be
automatically transmitted to any child threads that are created.

Note: During the creation of a new

thread

, it is
possible to

opt out

of receiving initial values for inheritable
thread-local variables.

Inheritable thread-local variables are used in preference to
ordinary thread-local variables when the per-thread-attribute being
maintained in the variable (e.g., User ID, Transaction ID) must be
automatically transmitted to any child threads that are created.

Note: During the creation of a new

thread

, it is
possible to

opt out

of receiving initial values for inheritable
thread-local variables.

Note: During the creation of a new

thread

, it is
possible to

opt out

of receiving initial values for inheritable
thread-local variables.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InheritableThreadLocal

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

T

childValue

​(

T

parentValue)

Computes the child's initial value for this inheritable thread-local
variable as a function of the parent's value at the time the child
thread is created.

- Methods declared in class java.lang.

ThreadLocal

get

,

initialValue

,

remove

,

set

,

withInitial

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

InheritableThreadLocal

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

T

childValue

​(

T

parentValue)

Computes the child's initial value for this inheritable thread-local
variable as a function of the parent's value at the time the child
thread is created.

- Methods declared in class java.lang.

ThreadLocal

get

,

initialValue

,

remove

,

set

,

withInitial

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

Computes the child's initial value for this inheritable thread-local
variable as a function of the parent's value at the time the child
thread is created.

Methods declared in class java.lang.

ThreadLocal

get

,

initialValue

,

remove

,

set

,

withInitial

---

#### Methods declared in class java.lang. ThreadLocal

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

- InheritableThreadLocal

```java
public InheritableThreadLocal()
```

============ METHOD DETAIL ==========

- Method Detail

- childValue

```java
protected
T
childValue​(
T
parentValue)
```

Computes the child's initial value for this inheritable thread-local
variable as a function of the parent's value at the time the child
thread is created. This method is called from within the parent
thread before the child is started.

This method merely returns its input argument, and should be overridden
if a different behavior is desired.

**Parameters:** parentValue

- the parent thread's value
**Returns:** the child thread's initial value

Constructor Detail

- InheritableThreadLocal

```java
public InheritableThreadLocal()
```

---

#### Constructor Detail

InheritableThreadLocal

```java
public InheritableThreadLocal()
```

---

#### InheritableThreadLocal

public InheritableThreadLocal()

Method Detail

- childValue

```java
protected
T
childValue​(
T
parentValue)
```

Computes the child's initial value for this inheritable thread-local
variable as a function of the parent's value at the time the child
thread is created. This method is called from within the parent
thread before the child is started.

This method merely returns its input argument, and should be overridden
if a different behavior is desired.

**Parameters:** parentValue

- the parent thread's value
**Returns:** the child thread's initial value

---

#### Method Detail

childValue

```java
protected
T
childValue​(
T
parentValue)
```

Computes the child's initial value for this inheritable thread-local
variable as a function of the parent's value at the time the child
thread is created. This method is called from within the parent
thread before the child is started.

This method merely returns its input argument, and should be overridden
if a different behavior is desired.

**Parameters:** parentValue

- the parent thread's value
**Returns:** the child thread's initial value

---

#### childValue

protected

T

childValue​(

T

parentValue)

Computes the child's initial value for this inheritable thread-local
variable as a function of the parent's value at the time the child
thread is created. This method is called from within the parent
thread before the child is started.

This method merely returns its input argument, and should be overridden
if a different behavior is desired.

This method merely returns its input argument, and should be overridden
if a different behavior is desired.

---

