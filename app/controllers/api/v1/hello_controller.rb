module Api
  module V1
    class HelloController < ApplicationController
      def index
        render json: { status: 200, message: 'Hello World! from api' }
      end
    end
  end
end
