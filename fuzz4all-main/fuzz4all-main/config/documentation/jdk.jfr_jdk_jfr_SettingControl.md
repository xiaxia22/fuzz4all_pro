# Class SettingControl

**Source:** `jdk.jfr\jdk\jfr\SettingControl.html`

### Class Description

```java
public abstract class
SettingControl

extends jdk.jfr.internal.Control
```

Base class to extend to create setting controls.

The following example shows a naive implementation of a setting control for
regular expressions:

```java
final class RegExpControl extends SettingControl {
private Pattern pattern = Pattern.compile(".*");

@Override
public void setValue(String value) {
this.pattern = Pattern.compile(value);
}

@Override
public String combine(Set<String> values) {
return String.join("|", values);
}

@Override
public String getValue() {
return pattern.toString();
}

public String matches(String s) {
return pattern.matcher(s).find();
}
}
```

The

setValue(String)

,

getValue()

and

combine(Set<String>)

methods are invoked when a setting value
changes, which typically happens when a recording is started or stopped. The

combine(Set<String>)

method is invoked to resolve what value to use
when multiple recordings are running at the same time.

The setting control must have a default constructor that can be invoked when
the event is registered.

To use a setting control with an event, add a method that returns a

boolean

value and takes the setting control as a parameter. Annotate
the method with the

@SettingDefinition

annotation. By default, the
method name is used as the setting name, but the name can be set explicitly
by using the

@Name

annotation. If the method returns

true

,
the event will be committed.

It is recommended that the

setValue(String)

method updates an
efficient data structure that can be quickly checked when the event is
committed.

The following example shows how to create an event that uses the
regular expression filter defined above.

```java
abstract class HTTPRequest extends Event {
@Label("Request URI")
protected String uri;

@Label("Servlet URI Filter")
@SettingDefinition
protected boolean uriFilter(RegExpControl regExp) {
return regExp.matches(uri);
}
}

@Label("HTTP Get Request")
class HTTPGetRequest extends HTTPRequest {
}

@Label("HTTP Post Request")
class HTTPPostRequest extends HTTPRequest {
}

class ExampleServlet extends HTTPServlet {
protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
HTTPGetRequest request = new HTTPGetRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}

protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
HTTPPostRequest request = new HTTPPostRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}
}
```

The following example shows how an event can be filtered by assigning the

"uriFilter"

setting with the specified regular expressions.

```java
Recording r = new Recording();
r.enable("HTTPGetRequest").with("uriFilter", "https://www.example.com/list/.*");
r.enable("HTTPPostRequest").with("uriFilter", "https://www.example.com/login/.*");
r.start();
```

**Since:** 9
**See Also:** SettingDefinition

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SettingControl()

Constructor for invocation by subclass constructors.

---

### Method Details

#### public abstract
String
combine​(
Set
<
String
> settingValues)

Combines the setting values for all running recordings into one value when
multiple recordings are running at the same time,

The semantics of how setting values are combined depends on the setting
control that is implemented, but all recordings should get at least all the
events they request.

This method should have no side effects, because the caller might cache values.
This method should never return

null

or throw an exception. If a
value is not valid for this setting control, the value should be ignored.

Examples:

if the setting control represents a threshold and three recordings are
running at the same time with the setting values

"10 ms"

,

"8 s"

, and

"1 ms"

, this method returns

"1 ms"

because it means that all recordings get at least all the requested data.

If the setting control represents a set of names and two recordings are
running at the same time with the setting values

"Smith, Jones"

and

"Jones,
Williams"

the returned value is

"Smith, Jones, Williams"

because all names would be accepted.

If the setting control represents a boolean condition and four recordings are
running at the same time with the following values

"true"

,

"false"

,

"false"

, and

"incorrect"

, this method returns

"true"

, because all
recordings get at least all the requested data.

**Specified by:**
- combine

in class

jdk.jfr.internal.Control

**Parameters:**
- settingValues

- the set of values, not

null

**Returns:**
- the value to use, not

null

---

#### public abstract void setValue​(
String
settingValue)

Sets the value for this setting.

If the setting value is not valid for this setting, this method
does not throw an exception. Instead, the value is ignored.

**Specified by:**
- setValue

in class

jdk.jfr.internal.Control

**Parameters:**
- settingValue

- the string value, not

null

---

#### public abstract
String
getValue()

Returns the currently used value for this setting, not

null

.

The value returned by this method is valid as an argument to both
the

setValue(String)

method and

combine(Set)

method.

This method is invoked when an event is registered to obtain the
default value. It is therefore important that a valid value can be
returned immediately after an instance of this class is created. It is
not valid to return

null

.

**Specified by:**
- getValue

in class

jdk.jfr.internal.Control

**Returns:**
- the setting value, not

null

---

### Additional Sections

#### Class SettingControl

java.lang.Object

- jdk.jfr.internal.Control
- - jdk.jfr.SettingControl

jdk.jfr.internal.Control

- jdk.jfr.SettingControl

jdk.jfr.SettingControl

```java
public abstract class
SettingControl

extends jdk.jfr.internal.Control
```

Base class to extend to create setting controls.

The following example shows a naive implementation of a setting control for
regular expressions:

```java
final class RegExpControl extends SettingControl {
private Pattern pattern = Pattern.compile(".*");

@Override
public void setValue(String value) {
this.pattern = Pattern.compile(value);
}

@Override
public String combine(Set<String> values) {
return String.join("|", values);
}

@Override
public String getValue() {
return pattern.toString();
}

public String matches(String s) {
return pattern.matcher(s).find();
}
}
```

The

setValue(String)

,

getValue()

and

combine(Set<String>)

methods are invoked when a setting value
changes, which typically happens when a recording is started or stopped. The

combine(Set<String>)

method is invoked to resolve what value to use
when multiple recordings are running at the same time.

The setting control must have a default constructor that can be invoked when
the event is registered.

To use a setting control with an event, add a method that returns a

boolean

value and takes the setting control as a parameter. Annotate
the method with the

@SettingDefinition

annotation. By default, the
method name is used as the setting name, but the name can be set explicitly
by using the

@Name

annotation. If the method returns

true

,
the event will be committed.

It is recommended that the

setValue(String)

method updates an
efficient data structure that can be quickly checked when the event is
committed.

The following example shows how to create an event that uses the
regular expression filter defined above.

```java
abstract class HTTPRequest extends Event {
@Label("Request URI")
protected String uri;

@Label("Servlet URI Filter")
@SettingDefinition
protected boolean uriFilter(RegExpControl regExp) {
return regExp.matches(uri);
}
}

@Label("HTTP Get Request")
class HTTPGetRequest extends HTTPRequest {
}

@Label("HTTP Post Request")
class HTTPPostRequest extends HTTPRequest {
}

class ExampleServlet extends HTTPServlet {
protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
HTTPGetRequest request = new HTTPGetRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}

protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
HTTPPostRequest request = new HTTPPostRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}
}
```

The following example shows how an event can be filtered by assigning the

"uriFilter"

setting with the specified regular expressions.

```java
Recording r = new Recording();
r.enable("HTTPGetRequest").with("uriFilter", "https://www.example.com/list/.*");
r.enable("HTTPPostRequest").with("uriFilter", "https://www.example.com/login/.*");
r.start();
```

**Since:** 9
**See Also:** SettingDefinition

public abstract class

SettingControl

extends jdk.jfr.internal.Control

Base class to extend to create setting controls.

The following example shows a naive implementation of a setting control for
regular expressions:

```java
final class RegExpControl extends SettingControl {
private Pattern pattern = Pattern.compile(".*");

@Override
public void setValue(String value) {
this.pattern = Pattern.compile(value);
}

@Override
public String combine(Set<String> values) {
return String.join("|", values);
}

@Override
public String getValue() {
return pattern.toString();
}

public String matches(String s) {
return pattern.matcher(s).find();
}
}
```

The

setValue(String)

,

getValue()

and

combine(Set<String>)

methods are invoked when a setting value
changes, which typically happens when a recording is started or stopped. The

combine(Set<String>)

method is invoked to resolve what value to use
when multiple recordings are running at the same time.

The setting control must have a default constructor that can be invoked when
the event is registered.

To use a setting control with an event, add a method that returns a

boolean

value and takes the setting control as a parameter. Annotate
the method with the

@SettingDefinition

annotation. By default, the
method name is used as the setting name, but the name can be set explicitly
by using the

@Name

annotation. If the method returns

true

,
the event will be committed.

It is recommended that the

setValue(String)

method updates an
efficient data structure that can be quickly checked when the event is
committed.

The following example shows how to create an event that uses the
regular expression filter defined above.

```java
abstract class HTTPRequest extends Event {
@Label("Request URI")
protected String uri;

@Label("Servlet URI Filter")
@SettingDefinition
protected boolean uriFilter(RegExpControl regExp) {
return regExp.matches(uri);
}
}

@Label("HTTP Get Request")
class HTTPGetRequest extends HTTPRequest {
}

@Label("HTTP Post Request")
class HTTPPostRequest extends HTTPRequest {
}

class ExampleServlet extends HTTPServlet {
protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
HTTPGetRequest request = new HTTPGetRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}

protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
HTTPPostRequest request = new HTTPPostRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}
}
```

The following example shows how an event can be filtered by assigning the

"uriFilter"

setting with the specified regular expressions.

```java
Recording r = new Recording();
r.enable("HTTPGetRequest").with("uriFilter", "https://www.example.com/list/.*");
r.enable("HTTPPostRequest").with("uriFilter", "https://www.example.com/login/.*");
r.start();
```

The following example shows a naive implementation of a setting control for
regular expressions:

```java
final class RegExpControl extends SettingControl {
private Pattern pattern = Pattern.compile(".*");

@Override
public void setValue(String value) {
this.pattern = Pattern.compile(value);
}

@Override
public String combine(Set<String> values) {
return String.join("|", values);
}

@Override
public String getValue() {
return pattern.toString();
}

public String matches(String s) {
return pattern.matcher(s).find();
}
}
```

The

setValue(String)

,

getValue()

and

combine(Set<String>)

methods are invoked when a setting value
changes, which typically happens when a recording is started or stopped. The

combine(Set<String>)

method is invoked to resolve what value to use
when multiple recordings are running at the same time.

The setting control must have a default constructor that can be invoked when
the event is registered.

To use a setting control with an event, add a method that returns a

boolean

value and takes the setting control as a parameter. Annotate
the method with the

@SettingDefinition

annotation. By default, the
method name is used as the setting name, but the name can be set explicitly
by using the

@Name

annotation. If the method returns

true

,
the event will be committed.

It is recommended that the

setValue(String)

method updates an
efficient data structure that can be quickly checked when the event is
committed.

The following example shows how to create an event that uses the
regular expression filter defined above.

```java
abstract class HTTPRequest extends Event {
@Label("Request URI")
protected String uri;

@Label("Servlet URI Filter")
@SettingDefinition
protected boolean uriFilter(RegExpControl regExp) {
return regExp.matches(uri);
}
}

@Label("HTTP Get Request")
class HTTPGetRequest extends HTTPRequest {
}

@Label("HTTP Post Request")
class HTTPPostRequest extends HTTPRequest {
}

class ExampleServlet extends HTTPServlet {
protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
HTTPGetRequest request = new HTTPGetRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}

protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
HTTPPostRequest request = new HTTPPostRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}
}
```

The following example shows how an event can be filtered by assigning the

"uriFilter"

setting with the specified regular expressions.

```java
Recording r = new Recording();
r.enable("HTTPGetRequest").with("uriFilter", "https://www.example.com/list/.*");
r.enable("HTTPPostRequest").with("uriFilter", "https://www.example.com/login/.*");
r.start();
```

final class RegExpControl extends SettingControl {
private Pattern pattern = Pattern.compile(".*");

@Override
public void setValue(String value) {
this.pattern = Pattern.compile(value);
}

@Override
public String combine(Set<String> values) {
return String.join("|", values);
}

@Override
public String getValue() {
return pattern.toString();
}

public String matches(String s) {
return pattern.matcher(s).find();
}
}

The setting control must have a default constructor that can be invoked when
the event is registered.

To use a setting control with an event, add a method that returns a

boolean

value and takes the setting control as a parameter. Annotate
the method with the

@SettingDefinition

annotation. By default, the
method name is used as the setting name, but the name can be set explicitly
by using the

@Name

annotation. If the method returns

true

,
the event will be committed.

It is recommended that the

setValue(String)

method updates an
efficient data structure that can be quickly checked when the event is
committed.

The following example shows how to create an event that uses the
regular expression filter defined above.

```java
abstract class HTTPRequest extends Event {
@Label("Request URI")
protected String uri;

@Label("Servlet URI Filter")
@SettingDefinition
protected boolean uriFilter(RegExpControl regExp) {
return regExp.matches(uri);
}
}

@Label("HTTP Get Request")
class HTTPGetRequest extends HTTPRequest {
}

@Label("HTTP Post Request")
class HTTPPostRequest extends HTTPRequest {
}

class ExampleServlet extends HTTPServlet {
protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
HTTPGetRequest request = new HTTPGetRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}

protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
HTTPPostRequest request = new HTTPPostRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}
}
```

The following example shows how an event can be filtered by assigning the

"uriFilter"

setting with the specified regular expressions.

```java
Recording r = new Recording();
r.enable("HTTPGetRequest").with("uriFilter", "https://www.example.com/list/.*");
r.enable("HTTPPostRequest").with("uriFilter", "https://www.example.com/login/.*");
r.start();
```

To use a setting control with an event, add a method that returns a

boolean

value and takes the setting control as a parameter. Annotate
the method with the

@SettingDefinition

annotation. By default, the
method name is used as the setting name, but the name can be set explicitly
by using the

@Name

annotation. If the method returns

true

,
the event will be committed.

It is recommended that the

setValue(String)

method updates an
efficient data structure that can be quickly checked when the event is
committed.

The following example shows how to create an event that uses the
regular expression filter defined above.

```java
abstract class HTTPRequest extends Event {
@Label("Request URI")
protected String uri;

@Label("Servlet URI Filter")
@SettingDefinition
protected boolean uriFilter(RegExpControl regExp) {
return regExp.matches(uri);
}
}

@Label("HTTP Get Request")
class HTTPGetRequest extends HTTPRequest {
}

@Label("HTTP Post Request")
class HTTPPostRequest extends HTTPRequest {
}

class ExampleServlet extends HTTPServlet {
protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
HTTPGetRequest request = new HTTPGetRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}

protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
HTTPPostRequest request = new HTTPPostRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}
}
```

The following example shows how an event can be filtered by assigning the

"uriFilter"

setting with the specified regular expressions.

```java
Recording r = new Recording();
r.enable("HTTPGetRequest").with("uriFilter", "https://www.example.com/list/.*");
r.enable("HTTPPostRequest").with("uriFilter", "https://www.example.com/login/.*");
r.start();
```

It is recommended that the

setValue(String)

method updates an
efficient data structure that can be quickly checked when the event is
committed.

The following example shows how to create an event that uses the
regular expression filter defined above.

```java
abstract class HTTPRequest extends Event {
@Label("Request URI")
protected String uri;

@Label("Servlet URI Filter")
@SettingDefinition
protected boolean uriFilter(RegExpControl regExp) {
return regExp.matches(uri);
}
}

@Label("HTTP Get Request")
class HTTPGetRequest extends HTTPRequest {
}

@Label("HTTP Post Request")
class HTTPPostRequest extends HTTPRequest {
}

class ExampleServlet extends HTTPServlet {
protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
HTTPGetRequest request = new HTTPGetRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}

protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
HTTPPostRequest request = new HTTPPostRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}
}
```

The following example shows how an event can be filtered by assigning the

"uriFilter"

setting with the specified regular expressions.

```java
Recording r = new Recording();
r.enable("HTTPGetRequest").with("uriFilter", "https://www.example.com/list/.*");
r.enable("HTTPPostRequest").with("uriFilter", "https://www.example.com/login/.*");
r.start();
```

The following example shows how to create an event that uses the
regular expression filter defined above.

```java
abstract class HTTPRequest extends Event {
@Label("Request URI")
protected String uri;

@Label("Servlet URI Filter")
@SettingDefinition
protected boolean uriFilter(RegExpControl regExp) {
return regExp.matches(uri);
}
}

@Label("HTTP Get Request")
class HTTPGetRequest extends HTTPRequest {
}

@Label("HTTP Post Request")
class HTTPPostRequest extends HTTPRequest {
}

class ExampleServlet extends HTTPServlet {
protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
HTTPGetRequest request = new HTTPGetRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}

protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
HTTPPostRequest request = new HTTPPostRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}
}
```

The following example shows how an event can be filtered by assigning the

"uriFilter"

setting with the specified regular expressions.

```java
Recording r = new Recording();
r.enable("HTTPGetRequest").with("uriFilter", "https://www.example.com/list/.*");
r.enable("HTTPPostRequest").with("uriFilter", "https://www.example.com/login/.*");
r.start();
```

abstract class HTTPRequest extends Event {
@Label("Request URI")
protected String uri;

@Label("Servlet URI Filter")
@SettingDefinition
protected boolean uriFilter(RegExpControl regExp) {
return regExp.matches(uri);
}
}

@Label("HTTP Get Request")
class HTTPGetRequest extends HTTPRequest {
}

@Label("HTTP Post Request")
class HTTPPostRequest extends HTTPRequest {
}

class ExampleServlet extends HTTPServlet {
protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
HTTPGetRequest request = new HTTPGetRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}

protected void doPost(HttpServletRequest req, HttpServletResponse resp) {
HTTPPostRequest request = new HTTPPostRequest();
request.begin();
request.uri = req.getRequestURI();
...
request.commit();
}
}

Recording r = new Recording();
r.enable("HTTPGetRequest").with("uriFilter", "https://www.example.com/list/.*");
r.enable("HTTPPostRequest").with("uriFilter", "https://www.example.com/login/.*");
r.start();

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SettingControl

()

Constructor for invocation by subclass constructors.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

combine

​(

Set

<

String

> settingValues)

Combines the setting values for all running recordings into one value when
multiple recordings are running at the same time,

abstract

String

getValue

()

Returns the currently used value for this setting, not

null

.

abstract void

setValue

​(

String

settingValue)

Sets the value for this setting.

- Methods declared in class jdk.jfr.internal.Control

clone

- Methods declared in class java.lang.

Object

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

SettingControl

()

Constructor for invocation by subclass constructors.

---

#### Constructor Summary

Constructor for invocation by subclass constructors.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

combine

​(

Set

<

String

> settingValues)

Combines the setting values for all running recordings into one value when
multiple recordings are running at the same time,

abstract

String

getValue

()

Returns the currently used value for this setting, not

null

.

abstract void

setValue

​(

String

settingValue)

Sets the value for this setting.

- Methods declared in class jdk.jfr.internal.Control

clone

- Methods declared in class java.lang.

Object

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

Combines the setting values for all running recordings into one value when
multiple recordings are running at the same time,

Returns the currently used value for this setting, not

null

.

Sets the value for this setting.

Methods declared in class jdk.jfr.internal.Control

clone

---

#### Methods declared in class jdk.jfr.internal.Control

Methods declared in class java.lang.

Object

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

- SettingControl

```java
protected SettingControl()
```

Constructor for invocation by subclass constructors.

============ METHOD DETAIL ==========

- Method Detail

- combine

```java
public abstract
String
combine​(
Set
<
String
> settingValues)
```

Combines the setting values for all running recordings into one value when
multiple recordings are running at the same time,

The semantics of how setting values are combined depends on the setting
control that is implemented, but all recordings should get at least all the
events they request.

This method should have no side effects, because the caller might cache values.
This method should never return

null

or throw an exception. If a
value is not valid for this setting control, the value should be ignored.

Examples:

if the setting control represents a threshold and three recordings are
running at the same time with the setting values

"10 ms"

,

"8 s"

, and

"1 ms"

, this method returns

"1 ms"

because it means that all recordings get at least all the requested data.

If the setting control represents a set of names and two recordings are
running at the same time with the setting values

"Smith, Jones"

and

"Jones,
Williams"

the returned value is

"Smith, Jones, Williams"

because all names would be accepted.

If the setting control represents a boolean condition and four recordings are
running at the same time with the following values

"true"

,

"false"

,

"false"

, and

"incorrect"

, this method returns

"true"

, because all
recordings get at least all the requested data.

**Specified by:** combine

in class

jdk.jfr.internal.Control
**Parameters:** settingValues

- the set of values, not

null
**Returns:** the value to use, not

null

- setValue

```java
public abstract void setValue​(
String
settingValue)
```

Sets the value for this setting.

If the setting value is not valid for this setting, this method
does not throw an exception. Instead, the value is ignored.

**Specified by:** setValue

in class

jdk.jfr.internal.Control
**Parameters:** settingValue

- the string value, not

null

- getValue

```java
public abstract
String
getValue()
```

Returns the currently used value for this setting, not

null

.

The value returned by this method is valid as an argument to both
the

setValue(String)

method and

combine(Set)

method.

This method is invoked when an event is registered to obtain the
default value. It is therefore important that a valid value can be
returned immediately after an instance of this class is created. It is
not valid to return

null

.

**Specified by:** getValue

in class

jdk.jfr.internal.Control
**Returns:** the setting value, not

null

Constructor Detail

- SettingControl

```java
protected SettingControl()
```

Constructor for invocation by subclass constructors.

---

#### Constructor Detail

SettingControl

```java
protected SettingControl()
```

Constructor for invocation by subclass constructors.

---

#### SettingControl

protected SettingControl()

Constructor for invocation by subclass constructors.

Method Detail

- combine

```java
public abstract
String
combine​(
Set
<
String
> settingValues)
```

Combines the setting values for all running recordings into one value when
multiple recordings are running at the same time,

The semantics of how setting values are combined depends on the setting
control that is implemented, but all recordings should get at least all the
events they request.

This method should have no side effects, because the caller might cache values.
This method should never return

null

or throw an exception. If a
value is not valid for this setting control, the value should be ignored.

Examples:

if the setting control represents a threshold and three recordings are
running at the same time with the setting values

"10 ms"

,

"8 s"

, and

"1 ms"

, this method returns

"1 ms"

because it means that all recordings get at least all the requested data.

If the setting control represents a set of names and two recordings are
running at the same time with the setting values

"Smith, Jones"

and

"Jones,
Williams"

the returned value is

"Smith, Jones, Williams"

because all names would be accepted.

If the setting control represents a boolean condition and four recordings are
running at the same time with the following values

"true"

,

"false"

,

"false"

, and

"incorrect"

, this method returns

"true"

, because all
recordings get at least all the requested data.

**Specified by:** combine

in class

jdk.jfr.internal.Control
**Parameters:** settingValues

- the set of values, not

null
**Returns:** the value to use, not

null

- setValue

```java
public abstract void setValue​(
String
settingValue)
```

Sets the value for this setting.

If the setting value is not valid for this setting, this method
does not throw an exception. Instead, the value is ignored.

**Specified by:** setValue

in class

jdk.jfr.internal.Control
**Parameters:** settingValue

- the string value, not

null

- getValue

```java
public abstract
String
getValue()
```

Returns the currently used value for this setting, not

null

.

The value returned by this method is valid as an argument to both
the

setValue(String)

method and

combine(Set)

method.

This method is invoked when an event is registered to obtain the
default value. It is therefore important that a valid value can be
returned immediately after an instance of this class is created. It is
not valid to return

null

.

**Specified by:** getValue

in class

jdk.jfr.internal.Control
**Returns:** the setting value, not

null

---

#### Method Detail

combine

```java
public abstract
String
combine​(
Set
<
String
> settingValues)
```

Combines the setting values for all running recordings into one value when
multiple recordings are running at the same time,

The semantics of how setting values are combined depends on the setting
control that is implemented, but all recordings should get at least all the
events they request.

This method should have no side effects, because the caller might cache values.
This method should never return

null

or throw an exception. If a
value is not valid for this setting control, the value should be ignored.

Examples:

if the setting control represents a threshold and three recordings are
running at the same time with the setting values

"10 ms"

,

"8 s"

, and

"1 ms"

, this method returns

"1 ms"

because it means that all recordings get at least all the requested data.

If the setting control represents a set of names and two recordings are
running at the same time with the setting values

"Smith, Jones"

and

"Jones,
Williams"

the returned value is

"Smith, Jones, Williams"

because all names would be accepted.

If the setting control represents a boolean condition and four recordings are
running at the same time with the following values

"true"

,

"false"

,

"false"

, and

"incorrect"

, this method returns

"true"

, because all
recordings get at least all the requested data.

**Specified by:** combine

in class

jdk.jfr.internal.Control
**Parameters:** settingValues

- the set of values, not

null
**Returns:** the value to use, not

null

---

#### combine

public abstract

String

combine​(

Set

<

String

> settingValues)

Combines the setting values for all running recordings into one value when
multiple recordings are running at the same time,

The semantics of how setting values are combined depends on the setting
control that is implemented, but all recordings should get at least all the
events they request.

This method should have no side effects, because the caller might cache values.
This method should never return

null

or throw an exception. If a
value is not valid for this setting control, the value should be ignored.

Examples:

if the setting control represents a threshold and three recordings are
running at the same time with the setting values

"10 ms"

,

"8 s"

, and

"1 ms"

, this method returns

"1 ms"

because it means that all recordings get at least all the requested data.

If the setting control represents a set of names and two recordings are
running at the same time with the setting values

"Smith, Jones"

and

"Jones,
Williams"

the returned value is

"Smith, Jones, Williams"

because all names would be accepted.

If the setting control represents a boolean condition and four recordings are
running at the same time with the following values

"true"

,

"false"

,

"false"

, and

"incorrect"

, this method returns

"true"

, because all
recordings get at least all the requested data.

The semantics of how setting values are combined depends on the setting
control that is implemented, but all recordings should get at least all the
events they request.

This method should have no side effects, because the caller might cache values.
This method should never return

null

or throw an exception. If a
value is not valid for this setting control, the value should be ignored.

Examples:

if the setting control represents a threshold and three recordings are
running at the same time with the setting values

"10 ms"

,

"8 s"

, and

"1 ms"

, this method returns

"1 ms"

because it means that all recordings get at least all the requested data.

If the setting control represents a set of names and two recordings are
running at the same time with the setting values

"Smith, Jones"

and

"Jones,
Williams"

the returned value is

"Smith, Jones, Williams"

because all names would be accepted.

If the setting control represents a boolean condition and four recordings are
running at the same time with the following values

"true"

,

"false"

,

"false"

, and

"incorrect"

, this method returns

"true"

, because all
recordings get at least all the requested data.

This method should have no side effects, because the caller might cache values.
This method should never return

null

or throw an exception. If a
value is not valid for this setting control, the value should be ignored.

Examples:

if the setting control represents a threshold and three recordings are
running at the same time with the setting values

"10 ms"

,

"8 s"

, and

"1 ms"

, this method returns

"1 ms"

because it means that all recordings get at least all the requested data.

If the setting control represents a set of names and two recordings are
running at the same time with the setting values

"Smith, Jones"

and

"Jones,
Williams"

the returned value is

"Smith, Jones, Williams"

because all names would be accepted.

If the setting control represents a boolean condition and four recordings are
running at the same time with the following values

"true"

,

"false"

,

"false"

, and

"incorrect"

, this method returns

"true"

, because all
recordings get at least all the requested data.

Examples:

if the setting control represents a threshold and three recordings are
running at the same time with the setting values

"10 ms"

,

"8 s"

, and

"1 ms"

, this method returns

"1 ms"

because it means that all recordings get at least all the requested data.

If the setting control represents a set of names and two recordings are
running at the same time with the setting values

"Smith, Jones"

and

"Jones,
Williams"

the returned value is

"Smith, Jones, Williams"

because all names would be accepted.

If the setting control represents a boolean condition and four recordings are
running at the same time with the following values

"true"

,

"false"

,

"false"

, and

"incorrect"

, this method returns

"true"

, because all
recordings get at least all the requested data.

if the setting control represents a threshold and three recordings are
running at the same time with the setting values

"10 ms"

,

"8 s"

, and

"1 ms"

, this method returns

"1 ms"

because it means that all recordings get at least all the requested data.

If the setting control represents a set of names and two recordings are
running at the same time with the setting values

"Smith, Jones"

and

"Jones,
Williams"

the returned value is

"Smith, Jones, Williams"

because all names would be accepted.

If the setting control represents a boolean condition and four recordings are
running at the same time with the following values

"true"

,

"false"

,

"false"

, and

"incorrect"

, this method returns

"true"

, because all
recordings get at least all the requested data.

If the setting control represents a set of names and two recordings are
running at the same time with the setting values

"Smith, Jones"

and

"Jones,
Williams"

the returned value is

"Smith, Jones, Williams"

because all names would be accepted.

If the setting control represents a boolean condition and four recordings are
running at the same time with the following values

"true"

,

"false"

,

"false"

, and

"incorrect"

, this method returns

"true"

, because all
recordings get at least all the requested data.

If the setting control represents a boolean condition and four recordings are
running at the same time with the following values

"true"

,

"false"

,

"false"

, and

"incorrect"

, this method returns

"true"

, because all
recordings get at least all the requested data.

setValue

```java
public abstract void setValue​(
String
settingValue)
```

Sets the value for this setting.

If the setting value is not valid for this setting, this method
does not throw an exception. Instead, the value is ignored.

**Specified by:** setValue

in class

jdk.jfr.internal.Control
**Parameters:** settingValue

- the string value, not

null

---

#### setValue

public abstract void setValue​(

String

settingValue)

Sets the value for this setting.

If the setting value is not valid for this setting, this method
does not throw an exception. Instead, the value is ignored.

If the setting value is not valid for this setting, this method
does not throw an exception. Instead, the value is ignored.

getValue

```java
public abstract
String
getValue()
```

Returns the currently used value for this setting, not

null

.

The value returned by this method is valid as an argument to both
the

setValue(String)

method and

combine(Set)

method.

This method is invoked when an event is registered to obtain the
default value. It is therefore important that a valid value can be
returned immediately after an instance of this class is created. It is
not valid to return

null

.

**Specified by:** getValue

in class

jdk.jfr.internal.Control
**Returns:** the setting value, not

null

---

#### getValue

public abstract

String

getValue()

Returns the currently used value for this setting, not

null

.

The value returned by this method is valid as an argument to both
the

setValue(String)

method and

combine(Set)

method.

This method is invoked when an event is registered to obtain the
default value. It is therefore important that a valid value can be
returned immediately after an instance of this class is created. It is
not valid to return

null

.

The value returned by this method is valid as an argument to both
the

setValue(String)

method and

combine(Set)

method.

This method is invoked when an event is registered to obtain the
default value. It is therefore important that a valid value can be
returned immediately after an instance of this class is created. It is
not valid to return

null

.

This method is invoked when an event is registered to obtain the
default value. It is therefore important that a valid value can be
returned immediately after an instance of this class is created. It is
not valid to return

null

.

---

