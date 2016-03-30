#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-hitimes
Version  : 1.2.3
Release  : 7
URL      : https://rubygems.org/downloads/hitimes-1.2.3.gem
Source0  : https://rubygems.org/downloads/hitimes-1.2.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : ISC
Requires: rubygem-hitimes-lib
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
## hitimes
* [Homepage](http://github.com/copiousfreetime/hitimes)
* [Github project](http://github.com.org/copiousfreetime/hitimes)
* email jeremy at copiousfreetime dot org
* `git clone url git://github.com/copiousfreetime/hitimes.git`

%package lib
Summary: lib components for the rubygem-hitimes package.
Group: Libraries

%description lib
lib components for the rubygem-hitimes package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n hitimes-1.2.3
gem spec %{SOURCE0} -l --ruby > rubygem-hitimes.gemspec

%build
gem build rubygem-hitimes.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
hitimes-1.2.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/hitimes-1.2.2 && ruby -I.:lib:spec -e 'Dir.glob "./spec/*spec.rb", &method(:require)' && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/hitimes-1.2.3.gem
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/hitimes-1.2.3/gem.build_complete
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/hitimes-1.2.3/gem_make.out
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/hitimes-1.2.3/mkmf.log
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/HISTORY.md
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/README.md
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/examples/benchmarks.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/examples/stats.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/.RUBYARCHDIR.-.hitimes.-.2.3.time
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes.c
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes.o
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes_instant_clock_gettime.c
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes_instant_clock_gettime.o
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes_instant_osx.c
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes_instant_osx.o
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes_instant_windows.c
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes_instant_windows.o
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes_interval.c
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes_interval.h
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes_interval.o
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes_stats.c
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes_stats.h
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes_stats.o
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/java/src/hitimes/Hitimes.java
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/java/src/hitimes/HitimesInterval.java
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/java/src/hitimes/HitimesService.java
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/java/src/hitimes/HitimesStats.java
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/lib/hitimes.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/lib/hitimes/metric.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/lib/hitimes/mutexed_stats.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/lib/hitimes/paths.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/lib/hitimes/stats.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/lib/hitimes/timed_metric.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/lib/hitimes/timed_value_metric.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/lib/hitimes/value_metric.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/lib/hitimes/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/spec/hitimes_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/spec/interval_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/spec/metric_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/spec/mutex_stats_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/spec/paths_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/spec/stats_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/spec/timed_metric_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/spec/timed_value_metric_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/spec/value_metric_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/spec/version_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/tasks/default.rake
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/tasks/extension.rake
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/tasks/this.rb
/usr/lib64/ruby/gems/2.3.0/specifications/hitimes-1.2.3.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/hitimes-1.2.3/hitimes/2.3/hitimes.so
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/ext/hitimes/c/hitimes.so
/usr/lib64/ruby/gems/2.3.0/gems/hitimes-1.2.3/lib/hitimes/2.3/hitimes.so
