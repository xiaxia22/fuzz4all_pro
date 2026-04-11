# Class TerminalFactorySpi

**Source:** `java.smartcardio\javax\smartcardio\TerminalFactorySpi.html`

### Class Description

```java
public abstract class
TerminalFactorySpi

extends
Object
```

The TerminalFactorySpi class defines the service provider interface.
Applications do not access this class directly, instead see

TerminalFactory

.

Service providers that want to write a new implementation should define
a concrete subclass of TerminalFactorySpi with a constructor that takes
an

Object

as parameter. That class needs to be registered
in a

Provider

. The engine

type

is

TerminalFactory

.
Service providers also need to implement subclasses of the abstract classes

CardTerminals

,

CardTerminal

,

Card

,
and

CardChannel

.

For example:

```java
file MyProvider.java:

package com.somedomain.card;

import java.security.Provider;

public class MyProvider extends Provider {
public MyProvider() {
super("MyProvider", 1.0d, "Smart Card Example");
put("TerminalFactory.MyType", "com.somedomain.card.MySpi");
}
}

file MySpi.java

package com.somedomain.card;

import javax.smartcardio.*;

public class MySpi extends TerminalFactoySpi {
public MySpi(Object parameter) {
// initialize as appropriate
}
protected CardTerminals engineTerminals() {
// add implementation code here
}
}
```

**Since:** 1.6
**See Also:** TerminalFactory

,

Provider

---

### Field Details

*No entries found.*

### Constructor Details

#### protected TerminalFactorySpi()

Constructs a new TerminalFactorySpi object.

This class is part of the service provider interface and not accessed
directly by applications. Applications
should use TerminalFactory objects, which can be obtained by calling
one of the

TerminalFactory.getInstance()

methods.

Concrete subclasses should define a constructor that takes an

Object

as parameter. It will be invoked when an
application calls one of the

TerminalFactory.getInstance()

methods and receives the

params

object specified by the application.

---

### Method Details

#### protected abstract
CardTerminals
engineTerminals()

Returns the CardTerminals created by this factory.

**Returns:**
- the CardTerminals created by this factory.

---

### Additional Sections

#### Class TerminalFactorySpi

java.lang.Object

- javax.smartcardio.TerminalFactorySpi

javax.smartcardio.TerminalFactorySpi

```java
public abstract class
TerminalFactorySpi

extends
Object
```

The TerminalFactorySpi class defines the service provider interface.
Applications do not access this class directly, instead see

TerminalFactory

.

Service providers that want to write a new implementation should define
a concrete subclass of TerminalFactorySpi with a constructor that takes
an

Object

as parameter. That class needs to be registered
in a

Provider

. The engine

type

is

TerminalFactory

.
Service providers also need to implement subclasses of the abstract classes

CardTerminals

,

CardTerminal

,

Card

,
and

CardChannel

.

For example:

```java
file MyProvider.java:

package com.somedomain.card;

import java.security.Provider;

public class MyProvider extends Provider {
public MyProvider() {
super("MyProvider", 1.0d, "Smart Card Example");
put("TerminalFactory.MyType", "com.somedomain.card.MySpi");
}
}

file MySpi.java

package com.somedomain.card;

import javax.smartcardio.*;

public class MySpi extends TerminalFactoySpi {
public MySpi(Object parameter) {
// initialize as appropriate
}
protected CardTerminals engineTerminals() {
// add implementation code here
}
}
```

**Since:** 1.6
**See Also:** TerminalFactory

,

Provider

public abstract class

TerminalFactorySpi

extends

Object

The TerminalFactorySpi class defines the service provider interface.
Applications do not access this class directly, instead see

TerminalFactory

.

Service providers that want to write a new implementation should define
a concrete subclass of TerminalFactorySpi with a constructor that takes
an

Object

as parameter. That class needs to be registered
in a

Provider

. The engine

type

is

TerminalFactory

.
Service providers also need to implement subclasses of the abstract classes

CardTerminals

,

CardTerminal

,

Card

,
and

CardChannel

.

For example:

```java
file MyProvider.java:

package com.somedomain.card;

import java.security.Provider;

public class MyProvider extends Provider {
public MyProvider() {
super("MyProvider", 1.0d, "Smart Card Example");
put("TerminalFactory.MyType", "com.somedomain.card.MySpi");
}
}

file MySpi.java

package com.somedomain.card;

import javax.smartcardio.*;

public class MySpi extends TerminalFactoySpi {
public MySpi(Object parameter) {
// initialize as appropriate
}
protected CardTerminals engineTerminals() {
// add implementation code here
}
}
```

Service providers that want to write a new implementation should define
a concrete subclass of TerminalFactorySpi with a constructor that takes
an

Object

as parameter. That class needs to be registered
in a

Provider

. The engine

type

is

TerminalFactory

.
Service providers also need to implement subclasses of the abstract classes

CardTerminals

,

CardTerminal

,

Card

,
and

CardChannel

.

For example:

```java
file MyProvider.java:

package com.somedomain.card;

import java.security.Provider;

public class MyProvider extends Provider {
public MyProvider() {
super("MyProvider", 1.0d, "Smart Card Example");
put("TerminalFactory.MyType", "com.somedomain.card.MySpi");
}
}

file MySpi.java

package com.somedomain.card;

import javax.smartcardio.*;

public class MySpi extends TerminalFactoySpi {
public MySpi(Object parameter) {
// initialize as appropriate
}
protected CardTerminals engineTerminals() {
// add implementation code here
}
}
```

For example:

```java
file MyProvider.java:

package com.somedomain.card;

import java.security.Provider;

public class MyProvider extends Provider {
public MyProvider() {
super("MyProvider", 1.0d, "Smart Card Example");
put("TerminalFactory.MyType", "com.somedomain.card.MySpi");
}
}

file MySpi.java

package com.somedomain.card;

import javax.smartcardio.*;

public class MySpi extends TerminalFactoySpi {
public MySpi(Object parameter) {
// initialize as appropriate
}
protected CardTerminals engineTerminals() {
// add implementation code here
}
}
```

file MyProvider.java:

package com.somedomain.card;

import java.security.Provider;

public class MyProvider extends Provider {
public MyProvider() {
super("MyProvider", 1.0d, "Smart Card Example");
put("TerminalFactory.MyType", "com.somedomain.card.MySpi");
}
}

file MySpi.java

package com.somedomain.card;

import javax.smartcardio.*;

public class MySpi extends TerminalFactoySpi {
public MySpi(Object parameter) {
// initialize as appropriate
}
protected CardTerminals engineTerminals() {
// add implementation code here
}
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TerminalFactorySpi

()

Constructs a new TerminalFactorySpi object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

protected abstract

CardTerminals

engineTerminals

()

Returns the CardTerminals created by this factory.

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

TerminalFactorySpi

()

Constructs a new TerminalFactorySpi object.

---

#### Constructor Summary

Constructs a new TerminalFactorySpi object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

protected abstract

CardTerminals

engineTerminals

()

Returns the CardTerminals created by this factory.

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

Returns the CardTerminals created by this factory.

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

- TerminalFactorySpi

```java
protected TerminalFactorySpi()
```

Constructs a new TerminalFactorySpi object.

This class is part of the service provider interface and not accessed
directly by applications. Applications
should use TerminalFactory objects, which can be obtained by calling
one of the

TerminalFactory.getInstance()

methods.

Concrete subclasses should define a constructor that takes an

Object

as parameter. It will be invoked when an
application calls one of the

TerminalFactory.getInstance()

methods and receives the

params

object specified by the application.

============ METHOD DETAIL ==========

- Method Detail

- engineTerminals

```java
protected abstract
CardTerminals
engineTerminals()
```

Returns the CardTerminals created by this factory.

**Returns:** the CardTerminals created by this factory.

Constructor Detail

- TerminalFactorySpi

```java
protected TerminalFactorySpi()
```

Constructs a new TerminalFactorySpi object.

This class is part of the service provider interface and not accessed
directly by applications. Applications
should use TerminalFactory objects, which can be obtained by calling
one of the

TerminalFactory.getInstance()

methods.

Concrete subclasses should define a constructor that takes an

Object

as parameter. It will be invoked when an
application calls one of the

TerminalFactory.getInstance()

methods and receives the

params

object specified by the application.

---

#### Constructor Detail

TerminalFactorySpi

```java
protected TerminalFactorySpi()
```

Constructs a new TerminalFactorySpi object.

This class is part of the service provider interface and not accessed
directly by applications. Applications
should use TerminalFactory objects, which can be obtained by calling
one of the

TerminalFactory.getInstance()

methods.

Concrete subclasses should define a constructor that takes an

Object

as parameter. It will be invoked when an
application calls one of the

TerminalFactory.getInstance()

methods and receives the

params

object specified by the application.

---

#### TerminalFactorySpi

protected TerminalFactorySpi()

Constructs a new TerminalFactorySpi object.

This class is part of the service provider interface and not accessed
directly by applications. Applications
should use TerminalFactory objects, which can be obtained by calling
one of the

TerminalFactory.getInstance()

methods.

Concrete subclasses should define a constructor that takes an

Object

as parameter. It will be invoked when an
application calls one of the

TerminalFactory.getInstance()

methods and receives the

params

object specified by the application.

This class is part of the service provider interface and not accessed
directly by applications. Applications
should use TerminalFactory objects, which can be obtained by calling
one of the

TerminalFactory.getInstance()

methods.

Concrete subclasses should define a constructor that takes an

Object

as parameter. It will be invoked when an
application calls one of the

TerminalFactory.getInstance()

methods and receives the

params

object specified by the application.

Concrete subclasses should define a constructor that takes an

Object

as parameter. It will be invoked when an
application calls one of the

TerminalFactory.getInstance()

methods and receives the

params

object specified by the application.

Method Detail

- engineTerminals

```java
protected abstract
CardTerminals
engineTerminals()
```

Returns the CardTerminals created by this factory.

**Returns:** the CardTerminals created by this factory.

---

#### Method Detail

engineTerminals

```java
protected abstract
CardTerminals
engineTerminals()
```

Returns the CardTerminals created by this factory.

**Returns:** the CardTerminals created by this factory.

---

#### engineTerminals

protected abstract

CardTerminals

engineTerminals()

Returns the CardTerminals created by this factory.

---

