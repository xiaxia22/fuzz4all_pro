# Annotation Type SettingDefinition

**Source:** `jdk.jfr\jdk\jfr\SettingDefinition.html`

### Class Description

```java
@Retention
(
RUNTIME
)

@Target
(
METHOD
)
public @interface
SettingDefinition
```

Annotation that specifies that a method in an event class should be used to
filter out events.

For the method to be valid it must return a

SettingControl

and only have one
parameter, which should be a non-abstract subclass of

SettingControl

The return value of the method specifies whether the event is to be
written to the Flight Recorder system or not.

The following example shows how to annotate a method in an event class.

```java
class HelloWorld extend Event {

@Label("Message");
String message;

@SettingDefinition;
@Label("Message Filter");
public boolean filter(RegExpControl regExp) {
return regExp.matches(message);
}
}
```

For an example of how the setting controls are defined, see

SettingControl

.

**Since:** 9
**See Also:** SettingControl

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Annotation Type SettingDefinition

```java
@Retention
(
RUNTIME
)

@Target
(
METHOD
)
public @interface
SettingDefinition
```

Annotation that specifies that a method in an event class should be used to
filter out events.

For the method to be valid it must return a

SettingControl

and only have one
parameter, which should be a non-abstract subclass of

SettingControl

The return value of the method specifies whether the event is to be
written to the Flight Recorder system or not.

The following example shows how to annotate a method in an event class.

```java
class HelloWorld extend Event {

@Label("Message");
String message;

@SettingDefinition;
@Label("Message Filter");
public boolean filter(RegExpControl regExp) {
return regExp.matches(message);
}
}
```

For an example of how the setting controls are defined, see

SettingControl

.

**Since:** 9
**See Also:** SettingControl

@Retention

(

RUNTIME

)

@Target

(

METHOD

)
public @interface

SettingDefinition

Annotation that specifies that a method in an event class should be used to
filter out events.

For the method to be valid it must return a

SettingControl

and only have one
parameter, which should be a non-abstract subclass of

SettingControl

The return value of the method specifies whether the event is to be
written to the Flight Recorder system or not.

The following example shows how to annotate a method in an event class.

```java
class HelloWorld extend Event {

@Label("Message");
String message;

@SettingDefinition;
@Label("Message Filter");
public boolean filter(RegExpControl regExp) {
return regExp.matches(message);
}
}
```

For an example of how the setting controls are defined, see

SettingControl

.

For the method to be valid it must return a

SettingControl

and only have one
parameter, which should be a non-abstract subclass of

SettingControl

The return value of the method specifies whether the event is to be
written to the Flight Recorder system or not.

The following example shows how to annotate a method in an event class.

```java
class HelloWorld extend Event {

@Label("Message");
String message;

@SettingDefinition;
@Label("Message Filter");
public boolean filter(RegExpControl regExp) {
return regExp.matches(message);
}
}
```

For an example of how the setting controls are defined, see

SettingControl

.

The return value of the method specifies whether the event is to be
written to the Flight Recorder system or not.

The following example shows how to annotate a method in an event class.

```java
class HelloWorld extend Event {

@Label("Message");
String message;

@SettingDefinition;
@Label("Message Filter");
public boolean filter(RegExpControl regExp) {
return regExp.matches(message);
}
}
```

For an example of how the setting controls are defined, see

SettingControl

.

The following example shows how to annotate a method in an event class.

```java
class HelloWorld extend Event {

@Label("Message");
String message;

@SettingDefinition;
@Label("Message Filter");
public boolean filter(RegExpControl regExp) {
return regExp.matches(message);
}
}
```

For an example of how the setting controls are defined, see

SettingControl

.

class HelloWorld extend Event {

@Label("Message");
String message;

@SettingDefinition;
@Label("Message Filter");
public boolean filter(RegExpControl regExp) {
return regExp.matches(message);
}
}

---

