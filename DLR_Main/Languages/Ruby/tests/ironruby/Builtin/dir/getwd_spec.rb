require File.dirname(__FILE__) + '/../../spec_helper'
require File.dirname(__FILE__) + '/fixtures/common'
require File.dirname(__FILE__) + '/pwd_spec'

describe "Dir.pwd" do
  it_behaves_like @dir_pwd, :getwd
end
