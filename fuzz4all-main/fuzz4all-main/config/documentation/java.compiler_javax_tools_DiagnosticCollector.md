# Class DiagnosticCollector<S>

**Source:** `java.compiler\javax\tools\DiagnosticCollector.html`

### Class Description

```java
public final class
DiagnosticCollector<S>

extends
Object

implements
DiagnosticListener
<S>
```

Provides an easy way to collect diagnostics in a list.

**Type Parameters:** S

- the type of source objects used by diagnostics received
by this object

---

### Field Details

*No entries found.*

### Constructor Details

#### public DiagnosticCollector()

*No description found.*

---

### Method Details

#### public
List
<
Diagnostic
<? extends
S
>> getDiagnostics()

Returns a list view of diagnostics collected by this object.

**Returns:**
- a list view of diagnostics

---

### Additional Sections

#### Class DiagnosticCollector<S>

java.lang.Object

- javax.tools.DiagnosticCollector<S>

javax.tools.DiagnosticCollector<S>

**Type Parameters:** S

- the type of source objects used by diagnostics received
by this object

**All Implemented Interfaces:** DiagnosticListener

<S>

```java
public final class
DiagnosticCollector<S>

extends
Object

implements
DiagnosticListener
<S>
```

Provides an easy way to collect diagnostics in a list.

**Since:** 1.6

public final class

DiagnosticCollector<S>

extends

Object

implements

DiagnosticListener

<S>

Provides an easy way to collect diagnostics in a list.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DiagnosticCollector

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

Diagnostic

<? extends

S

>>

getDiagnostics

()

Returns a list view of diagnostics collected by this object.

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

- Methods declared in interface javax.tools.

DiagnosticListener

report

Constructor Summary

Constructors

Constructor

Description

DiagnosticCollector

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

List

<

Diagnostic

<? extends

S

>>

getDiagnostics

()

Returns a list view of diagnostics collected by this object.

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

- Methods declared in interface javax.tools.

DiagnosticListener

report

---

#### Method Summary

Returns a list view of diagnostics collected by this object.

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

Methods declared in interface javax.tools.

DiagnosticListener

report

---

#### Methods declared in interface javax.tools. DiagnosticListener

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DiagnosticCollector

```java
public DiagnosticCollector()
```

============ METHOD DETAIL ==========

- Method Detail

- getDiagnostics

```java
public
List
<
Diagnostic
<? extends
S
>> getDiagnostics()
```

Returns a list view of diagnostics collected by this object.

**Returns:** a list view of diagnostics

Constructor Detail

- DiagnosticCollector

```java
public DiagnosticCollector()
```

---

#### Constructor Detail

DiagnosticCollector

```java
public DiagnosticCollector()
```

---

#### DiagnosticCollector

public DiagnosticCollector()

Method Detail

- getDiagnostics

```java
public
List
<
Diagnostic
<? extends
S
>> getDiagnostics()
```

Returns a list view of diagnostics collected by this object.

**Returns:** a list view of diagnostics

---

#### Method Detail

getDiagnostics

```java
public
List
<
Diagnostic
<? extends
S
>> getDiagnostics()
```

Returns a list view of diagnostics collected by this object.

**Returns:** a list view of diagnostics

---

#### getDiagnostics

public

List

<

Diagnostic

<? extends

S

>> getDiagnostics()

Returns a list view of diagnostics collected by this object.

---

